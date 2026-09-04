"""Tests for the modernized accounting system — covers every COBOL business rule."""

import pytest
from decimal import Decimal

from accounting import (
    Account,
    AccountStatus,
    AccountType,
    TransactionResult,
    TransactionType,
    MAXIMUM_TRANSACTION,
    DAILY_LIMIT,
)


@pytest.fixture
def active_checking() -> Account:
    return Account(
        number="00001234",
        name="JOHN DOE",
        account_type=AccountType.CHECKING,
        balance=Decimal("5000.00"),
        status=AccountStatus.ACTIVE,
    )


@pytest.fixture
def frozen_account() -> Account:
    return Account(
        number="00005678",
        name="JANE SMITH",
        account_type=AccountType.SAVINGS,
        balance=Decimal("10000.00"),
        status=AccountStatus.FROZEN,
    )


@pytest.fixture
def closed_account() -> Account:
    return Account(
        number="00009999",
        name="OLD ACCOUNT",
        account_type=AccountType.BUSINESS,
        balance=Decimal("0.00"),
        status=AccountStatus.CLOSED,
    )


# ── View Balance ──────────────────────────────────────────────

class TestViewBalance:
    def test_view_active_account(self, active_checking: Account):
        info = active_checking.view_balance()
        assert info["account_number"] == "00001234"
        assert info["name"] == "JOHN DOE"
        assert info["account_type"] == "CHECKING"
        assert info["balance"] == Decimal("5000.00")
        assert info["status"] == "ACTIVE"

    def test_view_frozen_account_allowed(self, frozen_account: Account):
        info = frozen_account.view_balance()
        assert info["balance"] == Decimal("10000.00")

    def test_view_closed_account_rejected(self, closed_account: Account):
        with pytest.raises(ValueError, match="Account is closed"):
            closed_account.view_balance()

    def test_view_logs_inquiry(self, active_checking: Account):
        active_checking.view_balance()
        assert len(active_checking.transaction_log) == 1
        log = active_checking.transaction_log[0]
        assert log.transaction_type == TransactionType.INQUIRY
        assert log.result == TransactionResult.OK
        assert log.amount == Decimal("0.00")


# ── Credit ────────────────────────────────────────────────────

class TestCredit:
    def test_credit_increases_balance(self, active_checking: Account):
        new_balance = active_checking.credit(Decimal("1000.00"))
        assert new_balance == Decimal("6000.00")
        assert active_checking.balance == Decimal("6000.00")

    def test_credit_updates_last_activity(self, active_checking: Account):
        active_checking.credit(Decimal("100.00"))
        assert active_checking.last_activity is not None

    def test_credit_logs_transaction(self, active_checking: Account):
        active_checking.credit(Decimal("500.00"))
        log = active_checking.transaction_log[-1]
        assert log.transaction_type == TransactionType.CREDIT
        assert log.amount == Decimal("500.00")
        assert log.result == TransactionResult.OK
        assert log.new_balance == Decimal("5500.00")

    def test_credit_zero_rejected(self, active_checking: Account):
        with pytest.raises(ValueError, match="positive"):
            active_checking.credit(Decimal("0"))

    def test_credit_negative_rejected(self, active_checking: Account):
        with pytest.raises(ValueError, match="positive"):
            active_checking.credit(Decimal("-100.00"))

    def test_credit_exceeds_max_transaction(self, active_checking: Account):
        with pytest.raises(ValueError, match="maximum transaction"):
            active_checking.credit(MAXIMUM_TRANSACTION + Decimal("0.01"))

    def test_credit_at_max_transaction_succeeds(self, active_checking: Account):
        new_balance = active_checking.credit(MAXIMUM_TRANSACTION)
        assert new_balance == Decimal("5000.00") + MAXIMUM_TRANSACTION

    def test_credit_frozen_account_rejected(self, frozen_account: Account):
        with pytest.raises(ValueError, match="not active"):
            frozen_account.credit(Decimal("100.00"))

    def test_credit_closed_account_rejected(self, closed_account: Account):
        with pytest.raises(ValueError, match="not active"):
            closed_account.credit(Decimal("100.00"))


# ── Debit ─────────────────────────────────────────────────────

class TestDebit:
    def test_debit_decreases_balance(self, active_checking: Account):
        new_balance = active_checking.debit(Decimal("1000.00"))
        assert new_balance == Decimal("4000.00")
        assert active_checking.balance == Decimal("4000.00")

    def test_debit_updates_last_activity(self, active_checking: Account):
        active_checking.debit(Decimal("100.00"))
        assert active_checking.last_activity is not None

    def test_debit_logs_transaction(self, active_checking: Account):
        active_checking.debit(Decimal("500.00"))
        log = active_checking.transaction_log[-1]
        assert log.transaction_type == TransactionType.DEBIT
        assert log.amount == Decimal("500.00")
        assert log.result == TransactionResult.OK
        assert log.new_balance == Decimal("4500.00")

    def test_debit_zero_rejected(self, active_checking: Account):
        with pytest.raises(ValueError, match="positive"):
            active_checking.debit(Decimal("0"))

    def test_debit_negative_rejected(self, active_checking: Account):
        with pytest.raises(ValueError, match="positive"):
            active_checking.debit(Decimal("-100.00"))

    def test_debit_exceeds_max_transaction(self, active_checking: Account):
        with pytest.raises(ValueError, match="maximum transaction"):
            active_checking.debit(MAXIMUM_TRANSACTION + Decimal("0.01"))

    def test_debit_exceeds_daily_limit(self, active_checking: Account):
        with pytest.raises(ValueError, match="daily withdrawal"):
            active_checking.debit(DAILY_LIMIT + Decimal("0.01"))

    def test_debit_at_daily_limit_succeeds(self, active_checking: Account):
        active_checking.balance = Decimal("15000.00")
        new_balance = active_checking.debit(DAILY_LIMIT)
        assert new_balance == Decimal("15000.00") - DAILY_LIMIT

    def test_debit_insufficient_funds(self, active_checking: Account):
        with pytest.raises(ValueError, match="Insufficient funds"):
            active_checking.debit(Decimal("5000.01"))

    def test_debit_insufficient_funds_logs_failure(self, active_checking: Account):
        with pytest.raises(ValueError):
            active_checking.debit(Decimal("5000.01"))
        log = active_checking.transaction_log[-1]
        assert log.result == TransactionResult.FAIL

    def test_debit_exact_balance_succeeds(self, active_checking: Account):
        new_balance = active_checking.debit(Decimal("5000.00"))
        assert new_balance == Decimal("0.00")

    def test_debit_frozen_account_rejected(self, frozen_account: Account):
        with pytest.raises(ValueError, match="not active"):
            frozen_account.debit(Decimal("100.00"))

    def test_debit_closed_account_rejected(self, closed_account: Account):
        with pytest.raises(ValueError, match="not active"):
            closed_account.debit(Decimal("100.00"))


# ── Multiple Operations ──────────────────────────────────────

class TestMultipleOperations:
    def test_credit_then_debit(self, active_checking: Account):
        active_checking.credit(Decimal("2000.00"))
        active_checking.debit(Decimal("3000.00"))
        assert active_checking.balance == Decimal("4000.00")
        assert len(active_checking.transaction_log) == 2

    def test_multiple_credits(self, active_checking: Account):
        active_checking.credit(Decimal("1000.00"))
        active_checking.credit(Decimal("2000.00"))
        active_checking.credit(Decimal("3000.00"))
        assert active_checking.balance == Decimal("11000.00")

    def test_transaction_log_grows(self, active_checking: Account):
        active_checking.view_balance()
        active_checking.credit(Decimal("100.00"))
        active_checking.debit(Decimal("50.00"))
        assert len(active_checking.transaction_log) == 3
        assert active_checking.transaction_log[0].transaction_type == TransactionType.INQUIRY
        assert active_checking.transaction_log[1].transaction_type == TransactionType.CREDIT
        assert active_checking.transaction_log[2].transaction_type == TransactionType.DEBIT


# ── Account Types ─────────────────────────────────────────────

class TestAccountTypes:
    def test_checking_account(self):
        acct = Account("1", "Test", AccountType.CHECKING, Decimal("100.00"))
        assert acct.account_type == AccountType.CHECKING

    def test_savings_account(self):
        acct = Account("2", "Test", AccountType.SAVINGS, Decimal("100.00"))
        assert acct.account_type == AccountType.SAVINGS

    def test_business_account(self):
        acct = Account("3", "Test", AccountType.BUSINESS, Decimal("100.00"))
        assert acct.account_type == AccountType.BUSINESS

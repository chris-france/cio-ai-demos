"""Unit tests for the modernized accounting system."""

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


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def active_account() -> Account:
    return Account(
        number="00001234",
        name="Jane Doe",
        account_type=AccountType.CHECKING,
        balance=Decimal("5000.00"),
        status=AccountStatus.ACTIVE,
    )


@pytest.fixture
def frozen_account() -> Account:
    return Account(
        number="00005678",
        name="John Smith",
        account_type=AccountType.SAVINGS,
        balance=Decimal("2000.00"),
        status=AccountStatus.FROZEN,
    )


@pytest.fixture
def closed_account() -> Account:
    return Account(
        number="00009999",
        name="Old Corp",
        account_type=AccountType.BUSINESS,
        balance=Decimal("0.00"),
        status=AccountStatus.CLOSED,
    )


# ---------------------------------------------------------------------------
# Balance inquiry
# ---------------------------------------------------------------------------

class TestGetBalance:
    def test_returns_balance(self, active_account: Account):
        assert active_account.get_balance() == Decimal("5000.00")

    def test_logs_inquiry(self, active_account: Account):
        active_account.get_balance()
        assert len(active_account.transactions) == 1
        assert active_account.transactions[0].type == TransactionType.INQUIRY

    def test_closed_account_raises(self, closed_account: Account):
        with pytest.raises(ValueError, match="closed"):
            closed_account.get_balance()


# ---------------------------------------------------------------------------
# Credit (deposit)
# ---------------------------------------------------------------------------

class TestCredit:
    def test_credit_increases_balance(self, active_account: Account):
        new = active_account.credit(Decimal("500.00"))
        assert new == Decimal("5500.00")

    def test_credit_logs_transaction(self, active_account: Account):
        active_account.credit(Decimal("100"))
        tx = active_account.transactions[-1]
        assert tx.type == TransactionType.CREDIT
        assert tx.result == TransactionResult.OK
        assert tx.amount == Decimal("100.00")

    def test_credit_updates_last_activity(self, active_account: Account):
        assert active_account.last_activity is None
        active_account.credit(Decimal("1"))
        assert active_account.last_activity is not None

    def test_credit_zero_raises(self, active_account: Account):
        with pytest.raises(ValueError, match="positive"):
            active_account.credit(Decimal("0"))

    def test_credit_negative_raises(self, active_account: Account):
        with pytest.raises(ValueError, match="positive"):
            active_account.credit(Decimal("-50"))

    def test_credit_exceeds_max_transaction(self, active_account: Account):
        with pytest.raises(ValueError, match="maximum transaction"):
            active_account.credit(MAXIMUM_TRANSACTION + 1)

    def test_credit_frozen_account_raises(self, frozen_account: Account):
        with pytest.raises(ValueError, match="not active"):
            frozen_account.credit(Decimal("100"))

    def test_credit_closed_account_raises(self, closed_account: Account):
        with pytest.raises(ValueError, match="not active"):
            closed_account.credit(Decimal("100"))


# ---------------------------------------------------------------------------
# Debit (withdrawal)
# ---------------------------------------------------------------------------

class TestDebit:
    def test_debit_decreases_balance(self, active_account: Account):
        new = active_account.debit(Decimal("1000.00"))
        assert new == Decimal("4000.00")

    def test_debit_logs_transaction(self, active_account: Account):
        active_account.debit(Decimal("250"))
        tx = active_account.transactions[-1]
        assert tx.type == TransactionType.DEBIT
        assert tx.result == TransactionResult.OK

    def test_debit_zero_raises(self, active_account: Account):
        with pytest.raises(ValueError, match="positive"):
            active_account.debit(Decimal("0"))

    def test_debit_negative_raises(self, active_account: Account):
        with pytest.raises(ValueError, match="positive"):
            active_account.debit(Decimal("-10"))

    def test_debit_exceeds_max_transaction(self, active_account: Account):
        with pytest.raises(ValueError, match="maximum transaction"):
            active_account.debit(MAXIMUM_TRANSACTION + 1)

    def test_debit_exceeds_daily_limit(self, active_account: Account):
        with pytest.raises(ValueError, match="daily withdrawal"):
            active_account.debit(DAILY_LIMIT + 1)

    def test_debit_insufficient_funds(self, active_account: Account):
        with pytest.raises(ValueError, match="Insufficient"):
            active_account.debit(Decimal("5000.01"))

    def test_debit_insufficient_funds_logs_failure(self, active_account: Account):
        with pytest.raises(ValueError):
            active_account.debit(Decimal("5000.01"))
        tx = active_account.transactions[-1]
        assert tx.result == TransactionResult.FAIL

    def test_debit_frozen_account_raises(self, frozen_account: Account):
        with pytest.raises(ValueError, match="not active"):
            frozen_account.debit(Decimal("100"))

    def test_debit_closed_account_raises(self, closed_account: Account):
        with pytest.raises(ValueError, match="not active"):
            closed_account.debit(Decimal("100"))

    def test_debit_exact_balance_to_zero(self, active_account: Account):
        new = active_account.debit(Decimal("5000.00"))
        assert new == Decimal("0.00")


# ---------------------------------------------------------------------------
# Multiple operations
# ---------------------------------------------------------------------------

class TestMultipleOperations:
    def test_credit_then_debit(self, active_account: Account):
        active_account.credit(Decimal("1000"))
        active_account.debit(Decimal("2000"))
        assert active_account.balance == Decimal("4000.00")

    def test_transaction_history_length(self, active_account: Account):
        active_account.get_balance()
        active_account.credit(Decimal("100"))
        active_account.debit(Decimal("50"))
        assert len(active_account.transactions) == 3

    def test_decimal_precision(self, active_account: Account):
        active_account.credit(Decimal("0.1"))
        active_account.credit(Decimal("0.2"))
        # Should be 5000.30, not 5000.30000000000004
        assert active_account.balance == Decimal("5000.30")

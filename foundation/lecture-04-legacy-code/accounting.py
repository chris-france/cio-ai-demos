"""
Accounting System — Modernized from COBOL (1985) to Python
Original: LEGACY-CORP ACCOUNTING-SYSTEM V2.1
Migrated: 2026 via AI-assisted modernization
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum
from typing import List, Optional


class AccountType(Enum):
    CHECKING = "C"
    SAVINGS = "S"
    BUSINESS = "B"


class AccountStatus(Enum):
    ACTIVE = "A"
    FROZEN = "F"
    CLOSED = "X"


class TransactionType(Enum):
    CREDIT = "C"
    DEBIT = "D"
    INQUIRY = "I"


class TransactionResult(Enum):
    OK = "OK"
    FAIL = "FL"


# ---------------------------------------------------------------------------
# Limits (mirror the COBOL WORKING-STORAGE values)
# ---------------------------------------------------------------------------
MINIMUM_BALANCE = Decimal("0.00")
MAXIMUM_TRANSACTION = Decimal("50000.00")
DAILY_LIMIT = Decimal("10000.00")


# ---------------------------------------------------------------------------
# Transaction log entry
# ---------------------------------------------------------------------------
@dataclass
class Transaction:
    timestamp: datetime
    account_number: str
    type: TransactionType
    amount: Decimal
    result: TransactionResult
    new_balance: Decimal


# ---------------------------------------------------------------------------
# Account
# ---------------------------------------------------------------------------
@dataclass
class Account:
    number: str
    name: str
    account_type: AccountType
    balance: Decimal = Decimal("0.00")
    open_date: Optional[datetime] = None
    last_activity: Optional[datetime] = None
    status: AccountStatus = AccountStatus.ACTIVE
    transactions: List[Transaction] = field(default_factory=list)

    # -- helpers -------------------------------------------------------------

    def _quantize(self, amount: Decimal) -> Decimal:
        return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def _log(
        self,
        tx_type: TransactionType,
        amount: Decimal,
        result: TransactionResult,
    ) -> Transaction:
        tx = Transaction(
            timestamp=datetime.now(),
            account_number=self.number,
            type=tx_type,
            amount=self._quantize(amount),
            result=result,
            new_balance=self._quantize(self.balance),
        )
        self.transactions.append(tx)
        return tx

    # -- public API ----------------------------------------------------------

    def get_balance(self) -> Decimal:
        """Return the current balance (mirrors VIEW-BALANCE paragraph)."""
        if self.status == AccountStatus.CLOSED:
            raise ValueError("Account is closed.")
        self._log(TransactionType.INQUIRY, Decimal("0"), TransactionResult.OK)
        return self._quantize(self.balance)

    def credit(self, amount: Decimal) -> Decimal:
        """Deposit funds (mirrors CREDIT-ACCOUNT paragraph)."""
        amount = self._quantize(amount)

        if self.status != AccountStatus.ACTIVE:
            raise ValueError("Account is not active. Cannot credit.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > MAXIMUM_TRANSACTION:
            raise ValueError("Exceeds maximum transaction limit.")

        self.balance = self._quantize(self.balance + amount)
        self.last_activity = datetime.now()
        self._log(TransactionType.CREDIT, amount, TransactionResult.OK)
        return self._quantize(self.balance)

    def debit(self, amount: Decimal) -> Decimal:
        """Withdraw funds (mirrors DEBIT-ACCOUNT paragraph)."""
        amount = self._quantize(amount)

        if self.status != AccountStatus.ACTIVE:
            raise ValueError("Account is not active. Cannot debit.")
        if self.status == AccountStatus.FROZEN:
            raise ValueError("Account is frozen. Contact admin.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > MAXIMUM_TRANSACTION:
            raise ValueError("Exceeds maximum transaction limit.")
        if amount > DAILY_LIMIT:
            raise ValueError("Exceeds daily withdrawal limit.")
        if self.balance - amount < MINIMUM_BALANCE:
            self._log(TransactionType.DEBIT, amount, TransactionResult.FAIL)
            raise ValueError("Insufficient funds.")

        self.balance = self._quantize(self.balance - amount)
        self.last_activity = datetime.now()
        self._log(TransactionType.DEBIT, amount, TransactionResult.OK)
        return self._quantize(self.balance)

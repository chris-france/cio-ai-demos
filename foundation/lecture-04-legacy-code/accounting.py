"""
Modern Python equivalent of ACCOUNTING-SYSTEM (COBOL, 1985).

Preserves all original business rules:
- Account types: Checking, Savings, Business
- Account statuses: Active, Frozen, Closed
- Minimum balance: $0.00
- Maximum single transaction: $50,000.00
- Daily withdrawal limit: $10,000.00
- Credit requires Active status
- Debit requires Active status (not Frozen, not Closed)
- Debit checks sufficient funds (balance - amount >= minimum)
- Transaction log for all operations
"""

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional


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


MINIMUM_BALANCE = Decimal("0.00")
MAXIMUM_TRANSACTION = Decimal("50000.00")
DAILY_LIMIT = Decimal("10000.00")


@dataclass
class TransactionRecord:
    timestamp: datetime
    account_number: str
    transaction_type: TransactionType
    amount: Decimal
    result: TransactionResult
    new_balance: Decimal


@dataclass
class Account:
    number: str
    name: str
    account_type: AccountType
    balance: Decimal = Decimal("0.00")
    open_date: Optional[datetime] = None
    last_activity: Optional[datetime] = None
    status: AccountStatus = AccountStatus.ACTIVE
    transaction_log: list[TransactionRecord] = field(default_factory=list)

    def _log(
        self,
        trans_type: TransactionType,
        amount: Decimal,
        result: TransactionResult,
    ) -> TransactionRecord:
        record = TransactionRecord(
            timestamp=datetime.now(),
            account_number=self.number,
            transaction_type=trans_type,
            amount=amount,
            result=result,
            new_balance=self.balance,
        )
        self.transaction_log.append(record)
        return record

    def view_balance(self) -> dict:
        """View account balance. Account must not be closed."""
        if self.status == AccountStatus.CLOSED:
            raise ValueError("Account is closed.")

        self._log(TransactionType.INQUIRY, Decimal("0.00"), TransactionResult.OK)

        return {
            "account_number": self.number,
            "name": self.name,
            "account_type": self.account_type.name,
            "balance": self.balance,
            "status": self.status.name,
        }

    def credit(self, amount: Decimal) -> Decimal:
        """Apply a credit (deposit) to the account.

        Rules (from COBOL):
        - Account must be Active
        - Amount must be positive
        - Amount must not exceed maximum transaction limit ($50,000)
        """
        if self.status != AccountStatus.ACTIVE:
            raise ValueError("Account is not active. Cannot credit.")

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > MAXIMUM_TRANSACTION:
            raise ValueError("Exceeds maximum transaction limit.")

        self.balance += amount
        self.last_activity = datetime.now()
        self._log(TransactionType.CREDIT, amount, TransactionResult.OK)

        return self.balance

    def debit(self, amount: Decimal) -> Decimal:
        """Apply a debit (withdrawal) to the account.

        Rules (from COBOL):
        - Account must be Active (not Frozen, not Closed)
        - Amount must be positive
        - Amount must not exceed maximum transaction limit ($50,000)
        - Amount must not exceed daily withdrawal limit ($10,000)
        - Balance after debit must not fall below minimum ($0.00)
        """
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

        self.balance -= amount
        self.last_activity = datetime.now()
        self._log(TransactionType.DEBIT, amount, TransactionResult.OK)

        return self.balance

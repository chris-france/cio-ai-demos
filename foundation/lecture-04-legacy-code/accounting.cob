       IDENTIFICATION DIVISION.
       PROGRAM-ID. ACCOUNTING-SYSTEM.
       AUTHOR. LEGACY-CORP.
       DATE-WRITTEN. 1985-06-15.
      *
      * SIMPLE ACCOUNTING SYSTEM
      * HANDLES ACCOUNT BALANCES, CREDITS, AND DEBITS
      * MAINTAINS TRANSACTION LOG
      *
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT ACCOUNT-FILE ASSIGN TO 'ACCOUNTS.DAT'
               ORGANIZATION IS INDEXED
               ACCESS MODE IS DYNAMIC
               RECORD KEY IS ACCT-NUMBER
               FILE STATUS IS FILE-STATUS.

           SELECT TRANSACTION-LOG ASSIGN TO 'TRANSLOG.DAT'
               ORGANIZATION IS SEQUENTIAL
               FILE STATUS IS LOG-STATUS.

       DATA DIVISION.
       FILE SECTION.

       FD ACCOUNT-FILE.
       01 ACCOUNT-RECORD.
           05 ACCT-NUMBER          PIC 9(8).
           05 ACCT-NAME            PIC X(30).
           05 ACCT-TYPE            PIC X(1).
              88 CHECKING          VALUE 'C'.
              88 SAVINGS           VALUE 'S'.
              88 BUSINESS          VALUE 'B'.
           05 ACCT-BALANCE         PIC S9(9)V99.
           05 ACCT-OPEN-DATE       PIC 9(8).
           05 ACCT-LAST-ACTIVITY   PIC 9(8).
           05 ACCT-STATUS          PIC X(1).
              88 ACTIVE            VALUE 'A'.
              88 FROZEN            VALUE 'F'.
              88 CLOSED            VALUE 'X'.

       FD TRANSACTION-LOG.
       01 TRANS-RECORD.
           05 TRANS-DATE           PIC 9(8).
           05 TRANS-TIME           PIC 9(6).
           05 TRANS-ACCT           PIC 9(8).
           05 TRANS-TYPE           PIC X(1).
              88 TRANS-CREDIT      VALUE 'C'.
              88 TRANS-DEBIT       VALUE 'D'.
              88 TRANS-INQUIRY     VALUE 'I'.
           05 TRANS-AMOUNT         PIC S9(9)V99.
           05 TRANS-RESULT         PIC X(2).
              88 TRANS-OK          VALUE 'OK'.
              88 TRANS-FAIL        VALUE 'FL'.
           05 TRANS-NEW-BALANCE    PIC S9(9)V99.

       WORKING-STORAGE SECTION.
       01 FILE-STATUS              PIC X(2).
       01 LOG-STATUS               PIC X(2).
       01 WS-OPERATION             PIC X(1).
          88 OP-VIEW               VALUE 'V'.
          88 OP-CREDIT             VALUE 'C'.
          88 OP-DEBIT              VALUE 'D'.
          88 OP-QUIT               VALUE 'Q'.
       01 WS-AMOUNT                PIC S9(9)V99.
       01 WS-ACCT-NUM              PIC 9(8).
       01 WS-CONTINUE              PIC X(1).
       01 WS-DATE                  PIC 9(8).
       01 WS-TIME                  PIC 9(6).

       01 WS-MINIMUM-BALANCE       PIC S9(9)V99 VALUE 0.
       01 WS-MAXIMUM-TRANSACTION   PIC S9(9)V99 VALUE 50000.00.
       01 WS-DAILY-LIMIT           PIC S9(9)V99 VALUE 10000.00.

       01 WS-DISPLAY-BALANCE       PIC $$$,$$$,$$9.99-.

       PROCEDURE DIVISION.
       MAIN-PROGRAM.
           PERFORM INITIALIZE-SYSTEM
           PERFORM PROCESS-TRANSACTIONS
               UNTIL OP-QUIT
           PERFORM CLOSE-SYSTEM
           STOP RUN.

       INITIALIZE-SYSTEM.
           OPEN I-O ACCOUNT-FILE
           IF FILE-STATUS NOT = '00'
               DISPLAY 'ERROR: CANNOT OPEN ACCOUNT FILE'
               DISPLAY 'FILE STATUS: ' FILE-STATUS
               STOP RUN
           END-IF

           OPEN OUTPUT TRANSACTION-LOG
           IF LOG-STATUS NOT = '00'
               DISPLAY 'ERROR: CANNOT OPEN TRANSACTION LOG'
               STOP RUN
           END-IF

           DISPLAY '=================================='
           DISPLAY '  ACCOUNTING SYSTEM V2.1'
           DISPLAY '  LEGACY CORP - EST. 1985'
           DISPLAY '=================================='.

       PROCESS-TRANSACTIONS.
           DISPLAY ' '
           DISPLAY 'MENU:'
           DISPLAY '  V - VIEW BALANCE'
           DISPLAY '  C - CREDIT (DEPOSIT)'
           DISPLAY '  D - DEBIT (WITHDRAWAL)'
           DISPLAY '  Q - QUIT'
           DISPLAY ' '
           ACCEPT WS-OPERATION

           EVALUATE TRUE
               WHEN OP-VIEW
                   PERFORM VIEW-BALANCE
               WHEN OP-CREDIT
                   PERFORM CREDIT-ACCOUNT
               WHEN OP-DEBIT
                   PERFORM DEBIT-ACCOUNT
               WHEN OP-QUIT
                   DISPLAY 'GOODBYE.'
               WHEN OTHER
                   DISPLAY 'INVALID OPTION. TRY AGAIN.'
           END-EVALUATE.

       VIEW-BALANCE.
           DISPLAY 'ENTER ACCOUNT NUMBER: '
           ACCEPT WS-ACCT-NUM
           MOVE WS-ACCT-NUM TO ACCT-NUMBER
           READ ACCOUNT-FILE
               INVALID KEY
                   DISPLAY 'ACCOUNT NOT FOUND.'
                   PERFORM LOG-TRANSACTION-INQUIRY
                   EXIT PARAGRAPH
           END-READ

           IF CLOSED
               DISPLAY 'ACCOUNT IS CLOSED.'
               EXIT PARAGRAPH
           END-IF

           MOVE ACCT-BALANCE TO WS-DISPLAY-BALANCE
           DISPLAY '=================================='
           DISPLAY 'ACCOUNT: ' ACCT-NUMBER
           DISPLAY 'NAME:    ' ACCT-NAME
           DISPLAY 'TYPE:    ' ACCT-TYPE
           DISPLAY 'BALANCE: ' WS-DISPLAY-BALANCE
           DISPLAY 'STATUS:  ' ACCT-STATUS
           DISPLAY '=================================='

           PERFORM LOG-TRANSACTION-INQUIRY.

       CREDIT-ACCOUNT.
           DISPLAY 'ENTER ACCOUNT NUMBER: '
           ACCEPT WS-ACCT-NUM
           MOVE WS-ACCT-NUM TO ACCT-NUMBER
           READ ACCOUNT-FILE
               INVALID KEY
                   DISPLAY 'ACCOUNT NOT FOUND.'
                   EXIT PARAGRAPH
           END-READ

           IF NOT ACTIVE
               DISPLAY 'ACCOUNT IS NOT ACTIVE. CANNOT CREDIT.'
               EXIT PARAGRAPH
           END-IF

           DISPLAY 'ENTER CREDIT AMOUNT: '
           ACCEPT WS-AMOUNT

           IF WS-AMOUNT <= 0
               DISPLAY 'AMOUNT MUST BE POSITIVE.'
               EXIT PARAGRAPH
           END-IF

           IF WS-AMOUNT > WS-MAXIMUM-TRANSACTION
               DISPLAY 'EXCEEDS MAXIMUM TRANSACTION LIMIT.'
               EXIT PARAGRAPH
           END-IF

           ADD WS-AMOUNT TO ACCT-BALANCE
           ACCEPT WS-DATE FROM DATE YYYYMMDD
           MOVE WS-DATE TO ACCT-LAST-ACTIVITY

           REWRITE ACCOUNT-RECORD
               INVALID KEY
                   DISPLAY 'ERROR UPDATING ACCOUNT.'
                   EXIT PARAGRAPH
           END-REWRITE

           MOVE ACCT-BALANCE TO WS-DISPLAY-BALANCE
           DISPLAY 'CREDIT APPLIED. NEW BALANCE: '
               WS-DISPLAY-BALANCE

           PERFORM LOG-TRANSACTION-CREDIT.

       DEBIT-ACCOUNT.
           DISPLAY 'ENTER ACCOUNT NUMBER: '
           ACCEPT WS-ACCT-NUM
           MOVE WS-ACCT-NUM TO ACCT-NUMBER
           READ ACCOUNT-FILE
               INVALID KEY
                   DISPLAY 'ACCOUNT NOT FOUND.'
                   EXIT PARAGRAPH
           END-READ

           IF NOT ACTIVE
               DISPLAY 'ACCOUNT IS NOT ACTIVE. CANNOT DEBIT.'
               EXIT PARAGRAPH
           END-IF

           IF FROZEN
               DISPLAY 'ACCOUNT IS FROZEN. CONTACT ADMIN.'
               EXIT PARAGRAPH
           END-IF

           DISPLAY 'ENTER DEBIT AMOUNT: '
           ACCEPT WS-AMOUNT

           IF WS-AMOUNT <= 0
               DISPLAY 'AMOUNT MUST BE POSITIVE.'
               EXIT PARAGRAPH
           END-IF

           IF WS-AMOUNT > WS-MAXIMUM-TRANSACTION
               DISPLAY 'EXCEEDS MAXIMUM TRANSACTION LIMIT.'
               EXIT PARAGRAPH
           END-IF

           IF WS-AMOUNT > WS-DAILY-LIMIT
               DISPLAY 'EXCEEDS DAILY WITHDRAWAL LIMIT.'
               EXIT PARAGRAPH
           END-IF

           IF ACCT-BALANCE - WS-AMOUNT < WS-MINIMUM-BALANCE
               DISPLAY 'INSUFFICIENT FUNDS.'
               PERFORM LOG-TRANSACTION-FAILED
               EXIT PARAGRAPH
           END-IF

           SUBTRACT WS-AMOUNT FROM ACCT-BALANCE
           ACCEPT WS-DATE FROM DATE YYYYMMDD
           MOVE WS-DATE TO ACCT-LAST-ACTIVITY

           REWRITE ACCOUNT-RECORD
               INVALID KEY
                   DISPLAY 'ERROR UPDATING ACCOUNT.'
                   EXIT PARAGRAPH
           END-REWRITE

           MOVE ACCT-BALANCE TO WS-DISPLAY-BALANCE
           DISPLAY 'DEBIT APPLIED. NEW BALANCE: '
               WS-DISPLAY-BALANCE

           PERFORM LOG-TRANSACTION-DEBIT.

       LOG-TRANSACTION-INQUIRY.
           ACCEPT WS-DATE FROM DATE YYYYMMDD
           ACCEPT WS-TIME FROM TIME
           MOVE WS-DATE TO TRANS-DATE
           MOVE WS-TIME TO TRANS-TIME
           MOVE WS-ACCT-NUM TO TRANS-ACCT
           MOVE 'I' TO TRANS-TYPE
           MOVE 0 TO TRANS-AMOUNT
           MOVE 'OK' TO TRANS-RESULT
           MOVE ACCT-BALANCE TO TRANS-NEW-BALANCE
           WRITE TRANS-RECORD.

       LOG-TRANSACTION-CREDIT.
           ACCEPT WS-DATE FROM DATE YYYYMMDD
           ACCEPT WS-TIME FROM TIME
           MOVE WS-DATE TO TRANS-DATE
           MOVE WS-TIME TO TRANS-TIME
           MOVE WS-ACCT-NUM TO TRANS-ACCT
           MOVE 'C' TO TRANS-TYPE
           MOVE WS-AMOUNT TO TRANS-AMOUNT
           MOVE 'OK' TO TRANS-RESULT
           MOVE ACCT-BALANCE TO TRANS-NEW-BALANCE
           WRITE TRANS-RECORD.

       LOG-TRANSACTION-DEBIT.
           ACCEPT WS-DATE FROM DATE YYYYMMDD
           ACCEPT WS-TIME FROM TIME
           MOVE WS-DATE TO TRANS-DATE
           MOVE WS-TIME TO TRANS-TIME
           MOVE WS-ACCT-NUM TO TRANS-ACCT
           MOVE 'D' TO TRANS-TYPE
           MOVE WS-AMOUNT TO TRANS-AMOUNT
           MOVE 'OK' TO TRANS-RESULT
           MOVE ACCT-BALANCE TO TRANS-NEW-BALANCE
           WRITE TRANS-RECORD.

       LOG-TRANSACTION-FAILED.
           ACCEPT WS-DATE FROM DATE YYYYMMDD
           ACCEPT WS-TIME FROM TIME
           MOVE WS-DATE TO TRANS-DATE
           MOVE WS-TIME TO TRANS-TIME
           MOVE WS-ACCT-NUM TO TRANS-ACCT
           MOVE 'D' TO TRANS-TYPE
           MOVE WS-AMOUNT TO TRANS-AMOUNT
           MOVE 'FL' TO TRANS-RESULT
           MOVE ACCT-BALANCE TO TRANS-NEW-BALANCE
           WRITE TRANS-RECORD.

       CLOSE-SYSTEM.
           CLOSE ACCOUNT-FILE
           CLOSE TRANSACTION-LOG
           DISPLAY 'SYSTEM CLOSED. TRANSACTION LOG SAVED.'.

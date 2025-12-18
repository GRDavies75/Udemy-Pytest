Feature: Bank Transactions
    Tests pertaining to banking transactions like withdrawal, deposit


    Scenario: Withdrawal of money
        Given The account balance is 100
        When The account holder withdraws 30
        Then The account balance should be 70

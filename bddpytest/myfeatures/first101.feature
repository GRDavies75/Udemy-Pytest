Feature: Bank Transactions
    Tests pertaining to banking transactions like withdrawal, deposit


    Scenario: Withdrawal of money
        Given The account balance is 100
        When The account holder withdraws 30
        Then The account balance should be 70


    Scenario: Removal of items from set
        Given A set of 3 fruits
        When We remove a fruit from the set
        Then The set will have 2 fruits

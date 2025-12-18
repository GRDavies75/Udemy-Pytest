Feature: Fixtures and BDD Background on Python Set Datatype


    Background: Setting up data for test
    Given A datatype set
    And The set is not empty


    Scenario: Adding to a Set
        Given A set with 3 elements
        When We add 2 elements to the set
        Then The set should have 5 elements
    

    Scenario: Removing from a Set
        Given A set of 3 fruits
        When We remove a fruit from the set
        Then The set will have 2 fruits

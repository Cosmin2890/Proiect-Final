Feature: Check the My acount functionality

  Background:
    Given login: I am a user on the login page
    Given login: I accept all cookies
    Given acount: I fill in an email "myrbestphotos@gmail.com"
    Given acount: I fill in a password "testare1234"
    Given acount: I click the login button
    Given acount: Verify expected pages "https://www.tiriacauto.ro/account"

@account_test_1
  Scenario: I click Informatii personale and I change the lastname in Nume field
    When acount: I click the informatii personale button
    Then acount: I Change the lastname in "Popescu"
    Then acount: I click the Trimite button

@account_test_2
  Scenario: I click Informatii personale and I change the firstname in Prenume field
    When acount: I click the informatii personale button
    Then acount: I Change the firstname in "Adrian"
    Then acount: I click the Trimite button

@account_test_3
  Scenario: I click Masinile mele and verify if I haven't car registered
    When acount: I click the Masinile mele button
    Then acount: I verify the message if I have the car registered "Momentan nu ai nicio masina adaugata."

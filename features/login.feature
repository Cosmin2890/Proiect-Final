Feature: Check the Login functionality

  Background:
    Given login: I am a user on the login page
    Given login: I accept all cookies

@login_test
  Scenario: Enter wrong credentials and check the error
    When login: I fill in an email "email@mail.com"
    When login: I fill in a password "pass"
    When login: I click the login button
    Then login: It shown an error message "Datele de identificare nu pot fi confirmate."

@login_test_2
  Scenario: Enter good credentials and verify expected page
    When login: I fill in an email "myrbestphotos@gmail.com"
    When login: I fill in a password "testare1234"
    When login: I click the login button
    Then login: Verify expected pages "https://www.tiriacauto.ro/account"

@login_logout_test
  Scenario: Enter good credentials, verify expected page, logout and verify again expected page
    When login: I fill in an email "myrbestphotos@gmail.com"
    When login: I fill in a password "testare1234"
    When login: I click the login button
    Then login: Verify expected pages "https://www.tiriacauto.ro/account"
    Then logout: I click the logout button
    Then login: Verify expected pages "https://www.tiriacauto.ro/"


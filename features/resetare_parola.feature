Feature: Reseteaza parola

  Background:
    Given login: I am a user on the login page
    Given login: I accept all cookies


@recparola
  Scenario: Check validation error message when email is invalid format
    When login: I click on the Ai uitat parola link
    When ai_uitat_parola: I fill in my email "my_email@test"
    When ai_uitat_parola: I click on the Trimite button
    Then ai_uitat_parola: I verify the invalid email validation message "Nu exista user cu adresa de email specificata."


@recparola2
  Scenario: Check validation error message when email era is empty
    When login: I click on the Ai uitat parola link
    When ai_uitat_parola: I make sure the email input is cleared
    When ai_uitat_parola: I click on the Trimite button
    Then ai_uitat_parola: I verify the invalid email validation message "Campul 'Email' trebuie completat."


Feature: User Login
  As a registered user
  I want to log in to the application
  So that I can see the inventory

  Scenario: Successful login with standard user
    Given I open the Swag Labs login page
    When I enter username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I should be redirected to the inventory page

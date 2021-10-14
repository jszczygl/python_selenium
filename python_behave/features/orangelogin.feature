Feature: Orange login
  Scenario: Login with valid parameters
    Given Open chrome browser
    When Open orange homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then Successfully login

  Scenario Outline: Login with multiple parameters
    Given Open chrome browser
    When Open orange homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then Successfully login

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
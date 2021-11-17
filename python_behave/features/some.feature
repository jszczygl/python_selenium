Feature: orange logo
  Scenario: Logo is present on page
    Given launch chrome browser
    When orange homepage is opened
    Then verify that the logo is present
    And close browser
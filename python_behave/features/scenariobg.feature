Feature: orange login
  Background: common steps
    Given Open chrome browser1
    When Open orange homepage1
    And Enter username and password1
    And Click on login button1

  Scenario: login to app
    Then Successfully login1

  Scenario: search user
    When navigate to search page
    Then search page should be displayed

  Scenario: advanced search
    When navigate to advanced search page
    Then advanced search page should be displayed
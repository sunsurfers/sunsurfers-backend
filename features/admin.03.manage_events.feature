Feature: CRUDing of events
    As an admin
    I want to manage all sunsurfers events

    Scenario: managing events
        Given I am logged in as an administator in the admin panel
        When I go to events page
        Then I have permissions to create, read, update and delete events where susnurfers participiated

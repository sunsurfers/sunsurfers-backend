Feature: CRUDing of chats
	As an admin
	I want to manage all sunsurfers chats

    Scenario: managing events

        Given I am logged in as an administator in the admin panel

        When I go to chats page

        Then I have permissions to create, read, update and delete chats for sunsurfers

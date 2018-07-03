Feature: CRUDing of user
	As an admin
	I want to manage all users in the application

Scenario "Viewing all user"

Given I am logged in as an administator in the admin panel
and I am in the user view page

When I go to user index page

Then I see all refistered user in the system with the following attributes: Name, Second Name and Telegram username

Scenario "Edit user info"

Given I am logged in as an administator in the admin panel
and I am in the user view page

When Edit any attribute of the user
and click the button Save

Then User info updated

Scenario "Delete user"
Given I am logged in as an administator in the admin panel
and I am in the user tab

When Click the button Delete

Then System ask whether I really want to delete this user
and user has been deleted after confirmation
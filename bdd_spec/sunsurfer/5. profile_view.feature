Feature: profile view
  In order to learn about other sunsurfers
	As an sun surfer
	I want to view profile of a particular sunsurfer
	
Scenario "Openning a full profile of another user"
Given I am on the screen with the map with opened profile preview
When I click on view profile button
Then I see the screen with profile of another user with the next fields: name, second name, avatar, current city, timestamp of the location update, occupation, about, list of the events, links to the social networks

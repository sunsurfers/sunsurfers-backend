Feature: profile view
  In order to learn about other sunsurfers
	As an sun surfer
	I want to view profile of a particular sunsurfer
	
    Scenario: Openning a full profile of another user
        Given I am on the screen with the map with opened profile preview
        When I click on view profile button
        Then I see the screen with profile of another user with the next fields:
            """
            first_name, second_name, avatar, current_city, location_timestamp,
            update, occupation, about, events, social_networks_links
            """

Feature: Show sunsurfers on the map
	As an sunsurfer
	I want to see other sunsurfers on the map

Scenario "Opening map. Separate sunsurfers found"
Given There are no two or more sunsurfers with overlay

When I open the map tab

Then I see circles with avatars with the radius 10 km

Scenario "Opening map. Separate sunsurfers found and overlaying users found"

Given There are two or more sunsurfers with overlay

When I open the map tab

Then I see circles with avatars with the radius 10 km
And I see circle with the number of overlayed users

Scenario "Zooming overlayed sunsurfers"
Given I see on the map the circle with the number of overlayed users

When I zoom in the map

Then I overlay disappears and I see separate circles with avatars 


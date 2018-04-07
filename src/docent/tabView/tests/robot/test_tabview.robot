# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s docent.tabView -t test_tabview.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src docent.tabView.testing.DOCENT_TABVIEW_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_tabview.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a TabView
  Given a logged-in site administrator
    and an add tabview form
   When I type 'My TabView' into the title field
    and I submit the form
   Then a tabview with the title 'My TabView' has been created

Scenario: As a site administrator I can view a TabView
  Given a logged-in site administrator
    and a tabview 'My TabView'
   When I go to the tabview view
   Then I can see the tabview title 'My TabView'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add tabview form
  Go To  ${PLONE_URL}/++add++TabView

a tabview 'My TabView'
  Create content  type=TabView  id=my-tabview  title=My TabView


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the tabview view
  Go To  ${PLONE_URL}/my-tabview
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a tabview with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the tabview title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

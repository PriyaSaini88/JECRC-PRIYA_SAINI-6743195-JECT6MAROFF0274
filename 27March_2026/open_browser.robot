#four sections
## always use double spaces for commands
*** Settings ***
#all imports and resources will be under setting
Documentation  Opening of browsers    # Documentation is keyword for descriptions
Library  SeleniumLibrary
*** Variables ***
# scalar variable -- single value
${url}  https://www.cricbuzz.com/
## list variable
@{bikes}  ktm  kwasaki  honda  pulsar
## Dictionary Variable
&{cars}  nissan=gtr  honda=civic  bmw=m5

#defining all  varibles
*** Test Cases ***
#Opening Chrome Headless Browser
#    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
#    [Tags]  smoke
#    Open Browser  https://www.cricbuzz.com/  headlesschrome
#    Maximize Browser Window
#
#    Log    navigated to cricbuzz
#    Log To Console    navigated to cricbuzz
#    Sleep    3s
#
#    Close Browser
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke  regression
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.nissan}
    Sleep    3s

    Close Browser
#
#Opening Firefox Browser
#    [Documentation]  Firefox browser navigating to https://www.cricbuzz.com/
#    Open Browser  https://www.cricbuzz.com/  firefox
#    Maximize Browser Window
#
#    Log    navigated to cricbuzz
#    Log To Console    navigated to cricbuzz
#    Sleep    3s
#
#    Close Browser

#Opening Edge Browser
#    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
#    Open Browser  https://www.cricbuzz.com/  edge
#    Maximize Browser Window
#
#    Log    navigated to cricbuzz
#    Log To Console    navigated to cricbuzz
#    Sleep    3s
#
#    Close Browser

## all test scripts will be defined

Open cricbuzz in Edge
    Open Edge Browser


*** Keywords ***
## user-defined keyword will be written in keywords section
Open Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  edge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s

    Close Browser
*** Settings ***
Documentation  multiselect dropdown
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
${browser}  chrome

*** Test Cases ***
handling multiselect
    Open Browser  ${url}  ${browser}
    Maximize Browser Window
    Sleep  2s

    Scroll Element Into View    xpath=//label[text() = "Colors:"]
    Sleep  1s

    Page Should Contain List    id=colors

    Select From List By Label    id=colors  Blue

    Select From List By Value    id=colors  green

    Select From List By Index    id=colors  3

    @{select_options}  Get Selected List Values    id=colors
    Log To Console  ${select_options}

    Sleep  2s

    Close Browser


## cross browser verification --->  robot -d reports -v browser:"edge" task1.robot
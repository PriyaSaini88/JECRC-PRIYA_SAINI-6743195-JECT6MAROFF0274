*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Windows Practice
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Scroll Element Into View    id = PopUp
    Sleep    2s
    Click Element    id=PopUp
    Sleep    2s
    @{windows}  Get Window Handles
    @{titles}   Get Window Titles
    Log To Console    ${titles}

    Switch Window  NEW
    Sleep    3s
    ${title}  Get Title
    Log To Console    ${title}


#    Log To Console    ${titles}[-1]

    Switch Window  ${windows}[0]
    Sleep    2s

    Page Should Contain   Automation Testing Practice
    Sleep    2s

    Close Browser


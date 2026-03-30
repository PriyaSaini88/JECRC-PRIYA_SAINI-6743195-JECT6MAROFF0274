*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s
    
    Scroll Element Into View    id=alertBtn
    Sleep    2s

    Click Button    id=alertBtn
    Sleep    2s

    Handle Alert
    Sleep    2s

    Close Browser

Confirmation Alert Accept
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Scroll Element Into View    id=confirmBtn
    Sleep    2s
    
    Click Button    id=confirmBtn
    Sleep    2s

    Handle Alert
    
    Page Should Contain    You pressed OK!

    ${msg}  Get Text    id=demo
    Log To Console    ${msg}
    Sleep    2s

    Close Browser


Confirmation Alert Dismiss
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Scroll Element Into View    id=confirmBtn
    Sleep    2s

    Click Button    id=confirmBtn
    Sleep    2s

    Handle Alert   action=DISMISS

    ${msg}  Get Text    id=demo
    Log To Console    ${msg}
    Sleep    2s

    Page Should Contain    ${msg}
    Sleep    2s


    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Scroll Element Into View    id=promptBtn
    Sleep    2s

    Click Button  id=promptBtn
    Sleep    2s

    ${text}  Set Variable  Priya
    Input Text Into Alert    ${text}
    Sleep    2s

    Page Should Contain    ${text}

    ${msg}  Get Text    id=demo
    Log To Console    ${msg}

    Sleep    2s

    Close Browser

Prompt Alert Dismiss
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Scroll Element Into View    id=promptBtn
    Sleep    2s

    Click Button  id=promptBtn
    Sleep    2s

    ${text}=  Set Variable  Priya
    Input Text Into Alert    ${text}  action=DISMISS
    Sleep    2s

    Page Should Contain    User cancelled the prompt.

    ${msg}  Get Text    id=demo
    Log To Console    ${msg}

    Sleep    2s

    Close Browser




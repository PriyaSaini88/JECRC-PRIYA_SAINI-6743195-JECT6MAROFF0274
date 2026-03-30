*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Click Button    xpath=//button[@onclick = "jsAlert()"]
    Sleep    2s

    Handle Alert
    Sleep    2s

    Close Browser

Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Click Button    xpath=//button[@onclick = "jsConfirm()"]
    Sleep    2s

#    Handle Alert  ## to accept the alert
## to dismiss
    Handle Alert  action=DISMISS

    Sleep    2s

    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s

    Click Button    xpath=//button[@onclick = "jsPrompt()"]
    Sleep    2s

    Input Text Into Alert    jsdlskd  action=DISMISS
    ## it will input the text and accept it by default
    Sleep    2s

    Close Browser
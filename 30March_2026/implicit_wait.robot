## Implicit wait --> for whole selenium and for browser
## Set Selenium Implicit Wait
## Set Browser Implicit Wait
## Get Selenium Implicit Wait --> to get wait value set for the selenium


*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#${url}  https://the-internet.herokuapp.com/
${url}   https://testautomationpractice.blogspot.com/


*** Test Cases ***
implicit wait
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Set Selenium Implicit Wait    5s

   ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}

    Input Text    id=name    dskdsldm



    Close Browser


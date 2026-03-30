*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
handling js
    Open Browser  ${url}   chrome
    Maximize Browser Window
    Sleep    3s

    Execute Javascript  window.scrollTo(0, document.body.scrollHeight)
    Sleep    3s

    Execute Javascript  window.scrollTo(0, 0)
    Sleep  3s

    Execute Javascript  window.scrollBy(0, 800)
    Sleep  3s

    Execute Javascript  window.scrollBy(0, -400)
    Sleep  3s

    Close Browser
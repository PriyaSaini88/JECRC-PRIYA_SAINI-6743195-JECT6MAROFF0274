*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Single Iframe Handling
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Select Frame    id=singleframe

    Input Text    xpath=//input[@type="text"]    aklks
    Sleep    2s

    Unselect Frame

    Close Browser

Handling Multiple Frames
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//a[@href = "#Multiple"]

    Select Frame    xpath=//iframe[@src="MultipleFrames.html"]
    Sleep    2s

    Select Frame    xpath=//div[@class="iframe-container"]/descendant::iframe
    Sleep    2s
    
    Input Text    xpath=//input[@type="text"]    jskalsjk
    Sleep    2s

    Unselect Frame

    Close Browser
*** Setting ***
Documentation  Handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com
${url2}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
#Handling Checkboxes
#    [Documentation]  herokuapp checkboxes
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#    Sleep    2s
#
#    Click Element    xpath=//a[text() = "Checkboxes"]
#
#    Page Should Contain Checkbox   xpath=(//input[@type = "checkbox"])[1]
#
#    Select Checkbox    xpath=(//input[@type = "checkbox"])[1]
#    Sleep    2s
#
#    Unselect Checkbox    xpath=(//input[@type = "checkbox"])[2]
#    Sleep    2s
#
#    Close Browser

Handling Checkboxes Practice
    [Documentation]  testautomation checkboxes
    Open Browser  ${url2}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Click Element    id=female
    Sleep    1s
    
    Page Should Contain Checkbox    id=sunday

    Select Checkbox    id=sunday
    Sleep    2s

    Unselect Checkbox    id=sunday
    Sleep    1s

    Close Browser

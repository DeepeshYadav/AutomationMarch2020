*** Settings ***
Library    SeleniumLibrary
Library    Search.py   Rahul   WITH NAME   sub


*** Variables ***
@{Number}   ${1}  ${3}  ${5}   ${7}


*** Test Cases ***
first test
    [Tags]  Sanity  BVT
    open browser   https://www.google.co.in  chrome
    ${result} =     sub.display name
    input text     name=q     ${result}
    log to console    ${result}
    sleep   5s
    Close Browser


Second Test with loop
    [Tags]  Sanity  BVT  FULL
    First loop   ${Number}

*** Keywords ***

First loop
    [Arguments]    ${Number}
    ${length}=    Get Length    ${Number}
    FOR  ${var}  IN RANGE   ${length}
        Run Keyword If   '${number}[${var}]' == 3  Exit For Loop
        log to console    ${number}[${var}]
    END

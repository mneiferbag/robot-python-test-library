#
# Copyright (c) 2023 Markus Neifer
# Licensed under the MIT License.
# See file LICENSE in project root directory.
#
*** Settings ***
Documentation    Test some keywords coming from a test library implemented in Python.
Library          MncPythonLibrary


*** Test Cases ***
Keyword Argument Conversion Test
    [Documentation]    Testing integer, string and list datatypes.
    @{MY_LIST} =    Create List    foo    bar

    ${x} =    Sum As String    ${5}    ${20}
    Should Be Equal    ${x}    25

#    ${y} =    Join Strings    @{MY_LIST}
#    Should Be Equal    ${y}    "foo,bar"

    Log To Console    ${MY_LIST}[0]

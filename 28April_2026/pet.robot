*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    Create Session    petapi    ${BASE_URL}  verify=True
    
    ${payload}=    Load JSON From File    ${CURDIR}/../Data/add_pet.json
    
    ${response}=   POST On Session   petapi   /pet  json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200
    
    Log To Console    ${response.json()}
    Set Suite Variable    ${PET_ID}    ${payload}[id]

Update Existing Pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=    Load JSON From File    ${CURDIR}/../Data/update_pet.json

    ${response}=   PUT On Session   petapi   /pet  json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal As Strings    ${response.json()}[status]    pending

    Log To Console    ${response.json()}
    
    
Find pet byID
    Create Session    petapi    ${BASE_URL}  verify=True

    ${response}=   GET On Session   petapi   /pet/${PET_ID}

    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal As Integers    ${response.json()}[id]    ${PET_ID}

    Log To Console    ${response.json()}
    
    
Find pet by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${qa_status}=    Create Dictionary    status=sold
    ${response}=   GET On Session   petapi   /pet/findByStatus  params=${qa_status}

    Should Be Equal As Integers    ${response.status_code}    200
    
    Log To Console    ${response.json()}

Upload an Image
    Create Session    petapi    ${BASE_URL}  verify=True
    
    ${form_data}=    Create Dictionary    additionalMetadata=Dog's image
    ${file_path}=    Set Variable    ${CURDIR}/../Data/dog_image.jpg
    ${file}=    Evaluate    {'file': open($file_path, 'rb')}

    ${response}=   POST On Session   petapi   /pet/${PET_ID}/uploadImage
    ...   data=${form_data}
    ...  files=${file}


    Should Be Equal As Integers    ${response.status_code}    200

Updates a pet using form data
    Create Session    petapi    ${BASE_URL}  verify=True

    ${form_data}=    Create Dictionary    name=Bbb   status=sold

    ${response}=   POST On Session   petapi   /pet/${PET_ID}
    ...   data=${form_data}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Delete pet by Id
    Create Session    petapi    ${BASE_URL}  verify=True

    ${response}=   Delete On Session   petapi   /pet/${PET_ID}

    Should Be Equal As Integers    ${response.status_code}    200


import nexmo

def phoneFriend():
    print("Calling registered contact")

    client = nexmo.Client(key='f9294c7a', secret='wckYppRk8sIqnG6K')

    responseData = client.send_message({
        'from': 'FAS',
        'to': '447925822040',
        'text': 'This is a test',
    })

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    return

def phoneEmergencyServices():
    print("Calling emergency services")

privKey = input("Please enter the private API key of the thingspeak device: ")

deviceKey = 'HzAVEyY5GzMvLx47NTYxOjM'

if deviceKey == privKey:
    print("success")
else:
    print("fail")
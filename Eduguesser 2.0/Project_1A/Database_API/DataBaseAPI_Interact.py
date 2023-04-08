import requests

api_endpoint = "http://127.0.0.1:8010/Locations"

Location1 = {'imagePath': 'static/images/11.png',
             'info1': 'The picture is a depiction of how the concept of Heroic Nudity of mythological figures is very popular here',
             'info2': 'The Odyssey and The Iliad are ancient epics from this land',
             'info3': 'The country contains 18 UNESCO World Heritage Sites and is a popular tourist destination',
             'info4': 'It is a coastal country with no piece of land more than 137 kms away from the ocean',
             'info5': 'The famous writer Rick Riordan seems to know a lot about its mythology',
             'CountryName': 'Greece'}
response = requests.post(api_endpoint, json=Location1)
print(response)

#response = requests.get(f'{api_endpoint}/ids')
#print(response.json())

#response = requests.delete(f'{api_endpoint}/6')

response = requests.get(api_endpoint)
#print(response.json())
for item in response.json():
    print(item)
#print(type(response.json()[0][9]))

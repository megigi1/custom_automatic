#Writing an app sending SMS to your phone when it's going to be a good weather, over 25 degrees
#For start we need to create webscrapping of forecast
#Secondly I need to create if/else statement
#Coneccting app to TWILIO
#Sending SMS when its HOT


import requests
from twilio.rest import Client
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "MY"
account_sid = "MY"
auth_token = "MY"

weather_params = {
    "lat": 50.0591,
    "lon": 22.4941,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_be_hot = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_be_hot = True

if will_be_hot:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Go To Beach.",
        from_='+1234567',
        to='+48123456'
    )
    print(message.status)



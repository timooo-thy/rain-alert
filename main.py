import requests
from twilio.rest import Client
# error 401: api is expired or wrong
account_sid = "ACbce78b7fd8250e0ac57a726dc4e1b611"
auth_token = "371198913c7afeed4c62695c12d94ba6"
parameters = {
    "lat": 1.381600,
    "lon": 103.740360,
    "appid": 'f9f72e65c72f14a680b52f073452dc86',
    "exclude": 'current,minutely,daily'
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"][:12]

id = [hour["weather"][0]["id"] for hour in hourly_data]

for code in id:
    if int(code) < 600:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It is going to rain today. Remember to bring an umbrella! ☔️",
            from_='+19034005624',
            to='+6598572155'
        )
        print(message.status)
        break


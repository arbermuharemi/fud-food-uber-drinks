import urllib2
import json
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from uber_rides.auth import AuthorizationCodeGrant

# flight_number = 1478
# flight_origin_date = "2016-09-24"
# apikey = "ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW"
# flight_info = urllib2.urlopen("https://demo30-test.apigee.net/v1/hack/status"
#                               "?flightNumber=%d&flightOriginDate=%s&apikey"
#                               "=ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW".format(
#     flight_number, flight_origin_date)).read()
flight_info = urllib2.urlopen("https://demo30-test.apigee.net/v1/hack/status"
                              "?flightNumber=1478&flightOriginDate=2016-09-30"
                              "&apikey=ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW").read()
print flight_info
flight_info_json = json.loads(flight_info)
arrvialLat = flight_info_json["flightStatusResponse"]["statusResponse"][
    "flightStatusTO"]["flightStatusLegTOList"]["arrivalTsoagLatitudeDecimal"]
arrivalLong = flight_info_json["flightStatusResponse"]["statusResponse"][
    "flightStatusTO"]["flightStatusLegTOList"]["arrivalTsoagLongitudeDecimal"]

print arrvialLat
print arrivalLong

server_token = "GSYPRMkSl_a7qQn8FH6d4imBjBnvrTWhh-6OzVPX"
session = Session(server_token)
client = UberRidesClient(session)
response = client.get_products(arrvialLat, arrivalLong)
products = response.json.get('products')
print products
auth_flow = AuthorizationCodeGrant(
    "gT2GLeVlXMQkrWWBO872bcjHK168Tr8W",
    None,
    "fQMuhWzwuvMiy2yl31qDu4xIRMP0DIVQQUtJy3hj",
    None,
)
auth_url = auth_flow.get_authorization_url()
session = auth_flow.get_session()
client = UberRidesClient(session, sandbox_mode=True)
credentials = session.oauth2credential
# response = api_client.get_user_profile()
# profile = response.json

# first_name = profile.get('first_name')
# first_name = profile.get('last_name')
# email = profile.get('email')


response = client.request_ride(
    start_latitude=arrvialLat,
    start_longitude=-arrivalLong,
)

ride_details = response.json
ride_id = ride_details.get('request_id')


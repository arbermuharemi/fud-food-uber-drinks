import urllib2
import json
# from uber_rides.session import Session
# from uber_rides.client import UberRidesClient
# from uber_rides.auth import AuthorizationCodeGrant

flight_number = 813
flight_origin_date = "2016-09-24"
apikey = "ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW"
# flight_info = urllib2.urlopen("https://demo30-test.apigee.net/v1/hack/status"
#                               "?flightNumber=%d&flightOriginDate=%s&apikey"
#                               "=ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW".format(
#     flight_number, flight_origin_date)).read()
flight_info = urllib2.urlopen("https://demo30-test.apigee.net/v1/hack/status"
                              "?flightNumber=813&flightOriginDate=2016-09-24&apikey"
                              "=ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW").read()
print flight_info
flight_info_json = json.loads(flight_info)
arrvialLat = flight_info_json["flightStatusResponse"]["statusResponse"][
    "flightStatusTO"]["flightStatusLegTOList"]["arrivalTsoagLatitudeDecimal"]
arrivalLong = flight_info_json["flightStatusResponse"]["statusResponse"][
    "flightStatusTO"]["flightStatusLegTOList"]["arrivalTsoagLongitudeDecimal"]

print arrvialLat
print arrivalLong

# print arrvialLat
# print arrivalLong
# server_token = "GSYPRMkSl_a7qQn8FH6d4imBjBnvrTWhh-6OzVPX"
# session = Session(server_token)
# client = UberRidesClient(session)
# response = client.get_products(37.77, -122.41)
# products = response.json.get('products')
# print products
# auth_flow = AuthorizationCodeGrant(
#     gT2GLeVlXMQkrWWBO872bcjHK168Tr8W,
#     YOUR_PERMISSION_SCOPES,
#     YOUR_CLIENT_SECRET,
#     YOUR_REDIRECT_URL,
# )
# auth_url = auth_flow.get_authorization_url()



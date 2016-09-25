from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from uber_rides.auth import AuthorizationCodeGrant

server_token = "GSYPRMkSl_a7qQn8FH6d4imBjBnvrTWhh-6OzVPX"
session = Session(server_token)
client = UberRidesClient(session)
response = client.get_products(37.77, -122.41)
products = response.json.get('products')
print products
# auth_flow = AuthorizationCodeGrant(
#     gT2GLeVlXMQkrWWBO872bcjHK168Tr8W,
#     YOUR_PERMISSION_SCOPES,
#     YOUR_CLIENT_SECRET,
#     YOUR_REDIRECT_URL,
# )
# auth_url = auth_flow.get_authorization_url()



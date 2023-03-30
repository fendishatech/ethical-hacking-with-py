import ipinfo
import sys

try:
    ip_address = sys.argv[1]
except IndexError:
    # if it s none it uses the ip of the pc it is running on (useful for remote access)
    ip_address = None


# access token from ipinfo.io account
access_token = '0dc73c3c0843ab'
handler = ipinfo.getHandler(access_token)
# create a client object with the access token
handler = ipinfo.getHandler(access_token)
# get the ip info
details = handler.getDetails(ip_address)
# print the ip info
for key, value in details.all.items():
    print(f"{key}: {value}")

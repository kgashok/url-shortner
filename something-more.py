from pyshorteners import Shortener

# get the token from https://bitly.is/accesstoken
access_token = "1ef1315a2efebd7557de137f776602276d833cb9"
link = input("Enter the short link to get more info:")
client = Shortener(api_key=access_token)
print(f"Original Link: {client.bitly.expand(link)}\n"  # get more info here--> https://bit.ly/shorteners-info
      f"Short Link: {link}\n"
      f"Total number of clicks = {client.bitly.total_clicks(link)}")

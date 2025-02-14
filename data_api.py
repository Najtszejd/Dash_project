import requests
import pandas as pd

auctions_data = "/auctions_data/"
auctions_info = "/auctions_info"
distilleries_info = "/distilleries_info/"


url_1 = f"https://whiskyhunter.net/api{auctions_data}"
response = requests.get(url_1)
print(response)
data_1 = response.json()
auctions_data_df = pd.DataFrame(data_1)


auction_slug = [a_slug for a_slug in auctions_data_df["auction_slug"]]
url_1_1 = f"https://whiskyhunter.net/api/auction_data/{auction_slug}/"
response = requests.get(url_1_1)
print(response)
data_1_1 = response.json()

data_auction_slug = pd.DataFrame()

for i in auctions_data_df["auction_slug"]:
    url_1_1 = f"https://whiskyhunter.net/api/auction_data/{i}/"
    response = requests.get(url_1_1)
    data_1_1 = response.json()
    
    




url_2 = f"https://whiskyhunter.net/api{auctions_info}"
url_3 = f"https://whiskyhunter.net/api{distilleries_info}"
url_4 = f"https://whiskyhunter.net/api/distillery_data/{disillery_slug}/"



response = requests.get(url_2)
print(response)
data_2 = response.json()
auctions_info_df = pd.DataFrame(data_2)

response = requests.get(url_3)
print(response)
data_3 = response.json()
distilleries_info_df = pd.DataFrame(data_3)


response = requests.get(url_4)
print(response)
data_4 = response.json()
distilleries_info_df_slug = pd.DataFrame(data_4)

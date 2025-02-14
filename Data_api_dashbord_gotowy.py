import requests
import pandas as pd

auctions_data = "/auctions_data/"
auctions_data_slug = "/auction_data/{slug}/"
auctions_info = "/auctions_info"
distilleries_info = "/distilleries_info/"
distilleries_info_slug = "/distillery_data/{slug}/"


url_2 = f"https://whiskyhunter.net/api{auctions_info}"
response = requests.get(url_2)
print(response)
data_2 = response.json()

df_2 = pd.DataFrame(data_2)


url = f"https://whiskyhunter.net/api{auctions_data}"
response = requests.get(url)
print(response)
data = response.json()

df_1 = pd.DataFrame(data)

df_1_basic_data = df_1[['auction_name','all_auctions_lots_count','auction_trading_volume',
       'auction_slug']]

df_1_basic_data["URL"] = df_2["url"]
df_1_transl = {
            "auction_trading_volume":"Łączna suma transakcji",
            "all_auctions_lots_count":"Łączna liczba butelek na aukcjach",
            "auction_name":"Nazwa Aukcji","auction_slug":"Skrót aukcji" 
}

df_1_basic_data.rename(columns=df_1_transl, inplace=True)
import requests
import pandas as pd
import datetime

auctions_data = "/auctions_data/"
auctions_info = "/auctions_info"
distilleries_info = "/distilleries_info/"


url_1 = f"https://whiskyhunter.net/api{auctions_data}"
response = requests.get(url_1)
print(response)
if response.status_code == 200:
    data_1 = response.json()
else:
    print(f"Błąd pobierania danych: {response.status_code}")
    data_1 = []

url_2 = f"https://whiskyhunter.net/api{auctions_info}"
response = requests.get(url_2)
print(response)
if response.status_code == 200:
    data_2 = response.json()
else:
    print(f"Błąd pobierania danych: {response.status_code}")
    data_2 = []
auctions_info_df = pd.DataFrame(data_2)



auctions_data_df = pd.DataFrame(data_1)
auctions_data_df = auctions_data_df[auctions_data_df["dt"] > '2023-01-01']

auctions_info_df = auctions_info_df[["slug","url","base_currency"]]


auction_data_df_dict = {
'dt' : "Data",
'auction_trading_volume' : "Wolumen obrotu",
'auction_lots_count' : "Liczba pozycji",
'auction_name' : "Nazwa aukcji",
'auction_slug' : "Skrót nazwy aukcji"
}

auctions_data_df.rename(columns = auction_data_df_dict, inplace = True)

auctions_data_df["Data"] = pd.to_datetime(auctions_data_df["Data"])
auctions_data_df["Średnia wartość lota"] = (auctions_data_df["Wolumen obrotu"] / auctions_data_df["Liczba pozycji"]).astype(int)

auction_info_df_dict = {
    "slug" : "Skrót nazwy aukcji",
    "base_currency" : "Waluta"
}

auctions_info_df.rename(columns= auction_info_df_dict, inplace = True)
 
auction_table_data = pd.merge(auctions_data_df, auctions_info_df, on = "Skrót nazwy aukcji", how = "left")
auction_table_data["Wolumen obrotu"] = pd.to_numeric(auction_table_data["Wolumen obrotu"], errors='coerce').astype(int)


auction_table_data = auction_table_data.groupby("Nazwa aukcji").agg({
    "Liczba pozycji": "sum",
    "Wolumen obrotu": "sum",
    "Średnia wartość lota" : "first",
    "url" : "first",
    "Waluta" : "first" 
}).reset_index()






url_3 = f"https://whiskyhunter.net/api{distilleries_info}"
response = requests.get(url_3)
print(response)
if response.status_code == 200:
    data_3 = response.json()
else:
    print(f"Błąd pobierania danych: {response.status_code}")
    data_3 = []
distilleries_info_df = pd.DataFrame(data_3)

# url_4 = f"https://whiskyhunter.net/api/distillery_data/{disillery_slug}/"
# response = requests.get(url_4)
# print(response)
# data_4 = response.json()
# distilleries_info_df_slug = pd.DataFrame(data_4)

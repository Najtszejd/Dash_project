import requests
import pandas as pd

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

auctions_data_df = pd.DataFrame(data_1)
auctions_data_df = auctions_data_df[auctions_data_df["dt"] > '2023-01-01']

auction_data_df_dict = {
'dt' : "Data",
'auction_trading_volume' : "Wolumen obrotu",
'auction_lots_count' : "Liczba pozycji",
'auction_name' : "Nazwa aukcji",
'auction_slug' : "Skrot nazwy aukcji"
}

auctions_data_df.rename(columns = auction_data_df_dict, inplace = True)
auctions_data_df["Data"] = pd.to_datetime(auctions_data_df["Data"])

auction_data_df_filter_table = (
    auctions_data_df.groupby("Nazwa aukcji")[["Liczba pozycji","Wolumen obrotu"]]
    .sum()
    .reset_index()
    )
auction_data_df_filter_table["Wolumen obrotu"] = pd.to_numeric(auction_data_df_filter_table["Wolumen obrotu"], errors='coerce').round().astype(int)
# auction_data_df_filter_table["Wolumen obrotu"] = auction_data_df_filter_table["Wolumen obrotu"].round().astype(int)

url_2 = f"https://whiskyhunter.net/api{auctions_info}"
response = requests.get(url_2)
print(response)
if response.status_code == 200:
    data_2 = response.json()
else:
    print(f"Błąd pobierania danych: {response.status_code}")
    data_2 = []
auctions_info_df = pd.DataFrame(data_2)


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

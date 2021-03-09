import dload

bscan_url = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=" 
addy_url = "&address="
lp_contract = "0xf5ad2466541d5d970521e3d7e3e9e62549ee8c36"
token_contract = "0xf79037f6f6be66832de4e7516be52826bc3cbcc4"
drugsv2_contract = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
bnb_price_url = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
bnbusd = float(dload.json(bnb_price_url)["price"])
marketcap_url = "https://api.bscscan.com/api?module=stats&action=tokenCsupply&contractaddress="






marketcap = float(dload.json(marketcap_url + token_contract)["result"])/10**6
print(type(marketcap), type(bnbusd))

marketcap_usd = marketcap * bnbusd

token_bal =  float(dload.json(bscan_url+ token_contract + addy_url + lp_contract )["result"])/10**6

print("{:.18f}".format(token_bal))
print(" circulation supply: ", "{:.18f}".format(marketcap))
print("usd marketcap: ", "{:.18f}".format(marketcap_usd))
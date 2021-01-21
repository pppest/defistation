import dload

bscan_url = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=" 
addy_url = "&address="
lp_contract = "0xf5ad2466541d5d970521e3d7e3e9e62549ee8c36"
token_contract = "0xf79037f6f6be66832de4e7516be52826bc3cbcc4"

token_bal =  float(dload.json(bscan_url+ token_contract + addy_url + lp_contract )["result"])
print(token_bal)



#!/usr/bin/env python3

import dload
import json
import time
import os

###
### this is the UPDATED version
###
###
# vatious settings
bnb_contract = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
narwal_lp = "0x40ff83ac2890dd5469f5eca2c17dcaf10ee09957"
pancake_lp = "0x40257481f09db2211a3274b34554bbb00b0a7fb1"
bnb_price_url = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
cred_contract = "0x571D0B55fe30eb1F6E68e8799F181c46De6B0059"
thugs_contract = "0xe10e9822a5de22f8761919310dda35cd997d63c0"
btri_cred_lp_contract = "0xF271F9Cc3E3626394978A9C0C9582931fa3caDD1"
btri_contract = "0x30c18c9cb3de61f2bd1974749a6f5725150208f3"

# LP contract: token contract - I left out wbnb as it is the same in all pairs.
lp_list = {
    "0xce7b1bc3ff9115b64bf4d6b1549f8339d02762f4": "0x8ff795a6f4d97e7887c79bea79aba5cc76444adf", # bch
    "0xdfb193940e1317f38e91568fdb05efe18ee4a3c7": "0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c", # btcb
    "0xf08865069864a5a62eb4dd4b9dcb66834822a198": "0x47bead2563dcbf3bf2c9407fea4dc236faba485a", # sxp
    "0x44e89861096371246ea8e3e86d97781ea24fbb29": "0x56b6fb708fc5732dec1afc8d8556423a2edccbd6", # eos
    "0x421df185ff87bc5f19bd5a90102a51452b70c4a4": "0x339550404ca4d831d12b1b2e4768869997390010", # drugsv2
    "0x9cbe4f200b474a1c33bffe7c6e531e1d47ecab46": "0x571d0b55fe30eb1f6e68e8799f181c46de6b0059", # cred
    "0x8ea481fe8e35c74355daf9b5f6b3b69f3c864afc": "0x4338665cbb7b2485a8855a139b75d5e34ab0db94", # ltc
    "0x2c92d0390f95477c70cb7b4b92050b0db5d04a1e": "0xf8a0bf9cf54bb92f17374d9e9a321e6a111a51bd", # link
    "0xf2e4e3f9b58b3edac88ad11d689a23f3119a782d": "0xe9e7cea3dedca5984780bafc599bd69add087d56", # busd
    "0xf7f21a56b19546a77eababf23d8dca726caf7577": "0x4b0f1812e5df2a09796481ff14017e6005508003", # twt
    "0x75115c644f9661a761a333ba0a38e42b1649f143": "0x2170ed0880ac9a755fd29b2688956bd959f933f8", # eth
    "0x0ff2d8b1a11195526f42905892bcb29e7b9f338d": "0x728c5bac3c3e370e372fc4671f9ef6916b814d8b", # unfi
    "0x1389003bcb228586648721a4f6187004dae01c51": "0xa1303e6199b319a891b79685f0537d289af1fc83", # nar
    "0x9354cab0f1083135439b23aa6c364329e578f39a": "0xe10e9822a5de22f8761919310dda35cd997d63c0", # thugs
    "0x8d27dccb0fb3d6621fa4f4155d719f4af159286e": "0xa1faa113cbe53436df28ff0aee54275c13b40975", # alpha
    "0xa5e5eeb6b51fa0fdc59915c81d75c83470bfa4f0": "0x179983892ec36287f1f342443b671ba549762241", # guns
    "0xed8ecb790be568461d85cf82c386e51124e46a52": "0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3", # dai
    "0x45ac15fb9650a790a0cd0f2b10c5ec4a6bbfcc2c": "0xa2b726b1145a4773f68593cf171187d8ebe4d495", # inj
    "0x0dc44e742941d4c935d6113a3b643656c5092d93": "0xa6381c6fd8f40a44721ef4f61edc1a8ccca7bf3d", # bhc
    "0x388ea96b8e384588ea17ec16d7d89cf591cb8b46": "0x63870a18b6e42b01ef1ad8a2302ef50b7132054f", # blink
    "0x0d29724d1834fc65869812bae5d63dce8acb7921": "0x55d398326f99059ff775485246999027b3197955", # busd-t
    "0x52a7fbe0995607b74e77a367036e76bce11a3b44": "0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63", # xvs
    "0x223b53b64aa5f87d2de194a15701fc0bc7474a31": "0xCa3F508B8e4Dd382eE878A314789373D80A5190A", # bifi
    "0xf5ad2466541d5d970521e3d7e3e9e62549ee8c36": "0xf79037f6f6be66832de4e7516be52826bc3cbcc4", # hard
    "0xe835ed82c7d9d018f8f5173eecfbb56f29f38570": "0xc97fac34ceb0bb1b2bdaf3b59ada378b99111a22", # bliq
    "0x40257481f09db2211a3274b34554bbb00b0a7fb1": "0x0000000000000000000000000000000000000000", #thugs pcake
    "0x40ff83ac2890dd5469f5eca2c17dcaf10ee09957": "0x0000000000000000000000000000000000000000", #thugs nar
    "0xd46E7f33f8788f87D6017074dC4e4d781D3df91E": "0x6fd7c98458a943f469e1cf4ea85b173f5cd342f4", ## bhc? v2?
    "0xc7C4726D0A45E4e7392901A90dCB52Ec4d2Bd1a3": "0xc13b7a43223bb9bf4b69bd68ab20ca1b79d81c75", ## jgn
    "0x982eE1343c73688314990483dea924808231dE4D": "0x30c18c9cb3de61f2bd1974749a6f5725150208f3",  ## tri bnb
    "0x99CE2eC80940d03a30898421654A038E75ab54A8": "0x233d91a0713155003fc4dce0afa871b508b3b715",  ## ditto bnb
    "0x153e580760097Df78A749bc349Dc1Ed09baFDBd4": "0x3aabCf53A1930A42E18D938C019E83Ebee50a849",  ## sponge bnb
    "0x3701cFE08a3f0b629dBcaEcebA773A8B4f0044E3": "0x03d6bd3d48f956d783456695698c407a46ecd54d" } ## hypr bnb 
#  use return.totalLiquidityUSD from json
streetswap_url = "https://api.streetswap.vip/totalliquidity"

# use result from og json. remember its *10^18
og_contract = "0x03edb31BeCc296d45670790c947150DAfEC2E238"
drugsv2_contract = "0x339550404ca4d831d12b1b2e4768869997390010"
og_drugs_url =  "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=" + drugsv2_contract + "&address=" + og_contract

# for drugs USD val and pair entries
streetswap_ticker_url = "https://api.streetswap.vip/tickers"
drugs_usd_pair = "0x339550404Ca4d831D12B1b2e4768869997390010_0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"

# creds and btri usd vales for btri/cred lp
cred_usd_pair = "0x571D0B55fe30eb1F6E68e8799F181c46De6B0059_0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
btri_wbnb_pair = "0x30C18C9cb3de61f2BD1974749A6f5725150208F3_0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"

# east / west tokens staked in club house
east_side_contract ="0x3b209c3e4b13e2fa5521b1cc0ccd15deeee2716d"
west_side_contract ="0xbd5b204250fe7f6d75594f00039625c243569e0d"
club_house_contract = "0xdcC718bd3D5f85AF244A40F3FEE46CF4f4F83Ed4"
club_house_east_bal_url = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=" + east_side_contract +"&address=" + club_house_contract
club_house_west_bal_url = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=" + west_side_contract +"&address=" + club_house_contract
guns_usd_pair ="0x179983892eC36287f1F342443B671Ba549762241_0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"

# defistation info
id_id = "Thugs"
api_key = "527768e0-8391-4d12-8501-93f3d83fda9e"
defistation_user = "VGh1Z3M6NTI3NzY4ZTAtODM5MS00ZDEyLTg1MDEtOTNmM2Q4M2ZkYTll"
defistation_api_url = '"https://api.defistation.io/dataProvider/tvl"'
curl_cmd =   "curl -f -X POST " + defistation_api_url + " -u " + id_id + ":" + api_key + " -H 'Content-Type: application/json' -d "

# calculate TVL
sw_total_liq = float(dload.json(streetswap_url)["return"]["totalLiquidityUSD"])
og_drugs_bal =  float(dload.json(og_drugs_url)["result"])/10**18
streetswap_ticker = dload.json(streetswap_ticker_url)
drugs_usd_val = float(streetswap_ticker[drugs_usd_pair]["last_price"])
og_drugs_usd_bal = og_drugs_bal * float(drugs_usd_val)

# get east west tokens staked and calculate their usd value vs. guns price
guns_usd_val = float(streetswap_ticker[guns_usd_pair]["last_price"])
club_house_east_bal = float(dload.json(club_house_east_bal_url)["result"])/10**18
club_house_west_bal = float(dload.json(club_house_west_bal_url)["result"])/10**18
east_west_usd_val = (club_house_west_bal + club_house_west_bal) * guns_usd_val
print("guns usd: ", guns_usd_val)
print("east bal: ", club_house_east_bal)
print("west bal: ", club_house_west_bal)
print("east west usd val: ", east_west_usd_val)

# set tvl
tvl = og_drugs_usd_bal + sw_total_liq + east_west_usd_val
false = "false"

# construct pair entries
pair_entities = [ { "id": pair, 
                    "token0": { "symbol": streetswap_ticker[pair]["base_symbol"] }, 
                    "token1": { "symbol":  streetswap_ticker[pair]["quote_symbol"]},
                } for  pair in streetswap_ticker ]

# calculate total bnb in contract
total_bnb = 0
total_token_bnb = 0
total_token_usd = 0

counter = 0
bscan_url = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=" 
addy_url = "&address="
thugs_usd_val = 0

bnbusd = float(dload.json(bnb_price_url)["price"])
print("bnbusd: ", bnbusd)

for lp_contract in lp_list:
        token_contract = lp_list[lp_contract]
        # get wbnb in LP, add 0.2 sec sleep caus of max 5/s limit
        wbnb_bal =  float(dload.json(bscan_url + bnb_contract+ addy_url + lp_contract)["result"])/10**18
        total_bnb += wbnb_bal
        time.sleep(0.2)
       
        token_bal =  float(dload.json(bscan_url+ token_contract + addy_url + lp_contract)["result"])/10**18

        if  lp_contract == "0xf5ad2466541d5d970521e3d7e3e9e62549ee8c36":
            token_bal = token_bal * 10**12
            print("hard ", "{:.18f}".format(token_bal), "{:.18f}".format(wbnb_bal))

        if  lp_contract == "0x982eE1343c73688314990483dea924808231dE4D":
            token_bal = token_bal * 10**9
            print("btri ", "{:.18f}".format(token_bal), "{:.18f}".format(wbnb_bal))
   
        if  lp_contract == "0x153e580760097Df78A749bc349Dc1Ed09baFDBd4":
            token_bal = token_bal * 10**9
            print("sponge ", "{:.18f}".format(token_bal), "{:.18f}".format(wbnb_bal))

        if token_bal != 0 :
            token_bnb_val = wbnb_bal / token_bal
        else:
            token_bnb_val = 0

        token_usd_val = token_bnb_val * bnbusd
        total_token_usd += token_usd_val
        if token_contract == thugs_contract :
            
           thugs_usd_val = token_usd_val
           print("thugs usd val: ", thugs_usd_val)
       

        time.sleep(0.2)
        counter += 1
        total_token_bnb += token_bnb_val

        print("lp contract: ",lp_contract, "wbnb bal: ", wbnb_bal)
        print("token contract: ", token_contract, "token bal: ", "{:.18f}".format(token_bal),"token bnb val: ", "{:.18f}".format(token_bnb_val), "token usd val: ", "{:.18f}".format(token_usd_val) )
        print()

# cred btri lp 
cred_usd_val  = float(streetswap_ticker[cred_usd_pair]["last_price"])
btri_wbnb_val = float(streetswap_ticker[btri_wbnb_pair]["last_price"])
btri_usd_val = btri_wbnb_val * bnbusd
print("btri usd val", btri_usd_val)
print("cred usd val", cred_usd_val)
cred_token_bal =  float(dload.json(bscan_url+ cred_contract + addy_url + btri_cred_lp_contract)["result"])/10**18
time.sleep(0.2)
btri_token_bal =  float(dload.json(bscan_url+ btri_contract + addy_url + btri_cred_lp_contract)["result"])/10**9
time.sleep(0.2)

btri_token_bal_usd = btri_token_bal * btri_usd_val
cred_token_bal_usd = cred_token_bal * cred_usd_val

tvl += btri_token_bal_usd
tvl += cred_token_bal_usd

print("btri tokens in lp ", btri_token_bal)
print("cred tokens in lp ", cred_token_bal)
print("btri in lp usd val ", btri_token_bal_usd)
print("cred in lp usd val ", cred_token_bal_usd)
print()

# get thugs in cred contract and add usd value to tvl
thugs_bal =  float(dload.json(bscan_url + thugs_contract + addy_url + cred_contract)["result"])/10**18
thugs_in_creds_usd_val = thugs_bal * thugs_usd_val
tvl += thugs_in_creds_usd_val

# conctruct data json
data = {
    "tvl": tvl,
    "bnb": total_bnb,
    "data": {
        "pairEntities":  pair_entities
        }, 
    "test": false}

result = json.dumps(data) 

# write defistation curl info
f = open("defistationcurl.sh", "w")
#f.write(result)
f.write(curl_cmd + "'" + result + "'" + " && : || curl -s -X POST https://api.telegram.org/bot716244131:AAEeUjyMK3P9U7DRjNGLTYkYVBvx5i8mDjg/sendMessage -d text='defistation error' -d chat_id=-259573637")
f.close()

# test info
print("number of LP pools ", counter)   
print("total token BNB value: ", total_token_bnb)
print("total token USD value: ", total_token_usd)
print("thugs in creds" , thugs_bal)
print("thugs usd val ", thugs_usd_val)
print("thugs in creds usd val ",thugs_in_creds_usd_val)
print()
print("Streetswap total liquidity USD: ", sw_total_liq)
print("OG Drugs balance: ", og_drugs_bal)
print("drugs usd  val: ", drugs_usd_val)
print("OG drugs bal USD val: ",og_drugs_usd_bal )
print("TVL: ", tvl)
print("Total BNB in contract: ",total_bnb)
print()
print()


# execute curl
#os.system(curl_cmd  + "'" + result + "'") #  > ./curloutput.log  && date > ./last_update.log ") #|| sh send_msg.sh 'defistation error'")


import dload

lp_list = [
    "0xce7b1bc3ff9115b64bf4d6b1549f8339d02762f4", # bch
    "0xdfb193940e1317f38e91568fdb05efe18ee4a3c7", #btc
    "0xf08865069864a5a62eb4dd4b9dcb66834822a198", #sxp
    "0x44e89861096371246ea8e3e86d97781ea24fbb29", #eos
    "0x421df185ff87bc5f19bd5a90102a51452b70c4a4", #drugsv2
    "0x9cbe4f200b474a1c33bffe7c6e531e1d47ecab46", #cred
    "0x8ea481fe8e35c74355daf9b5f6b3b69f3c864afc", #ltc
    "0x2c92d0390f95477c70cb7b4b92050b0db5d04a1e", #link
    "0xf2e4e3f9b58b3edac88ad11d689a23f3119a782d", #busd
    "0xf7f21a56b19546a77eababf23d8dca726caf7577", #twt
    "0x75115c644f9661a761a333ba0a38e42b1649f143", #eth
    "0x0ff2d8b1a11195526f42905892bcb29e7b9f338d", #unfi
    "0x1389003bcb228586648721a4f6187004dae01c51", #nar
    "0x8d27dccb0fb3d6621fa4f4155d719f4af159286e", #alpha
    "0xa5e5eeb6b51fa0fdc59915c81d75c83470bfa4f0", #guns
    "0xed8ecb790be568461d85cf82c386e51124e46a52", #dai
    "0x45ac15fb9650a790a0cd0f2b10c5ec4a6bbfcc2c", #inj
    "0x0dc44e742941d4c935d6113a3b643656c5092d93", #bhc
    "0x388ea96b8e384588ea17ec16d7d89cf591cb8b46", #blink
    "0x0d29724d1834fc65869812bae5d63dce8acb7921", #busd-t
    "0x52a7fbe0995607b74e77a367036e76bce11a3b44", #xvs
    "0x223b53b64aa5f87d2de194a15701fc0bc7474a31", #bifi
    "0xf5ad2466541d5d970521e3d7e3e9e62549ee8c36", #hard
    "0xe835ed82c7d9d018f8f5173eecfbb56f29f38570", #bliq
    "0x40257481f09db2211a3274b34554bbb00b0a7fb1", #thugs pcake
    "0x40ff83ac2890dd5469f5eca2c17dcaf10ee09957", #thugs nar
]


bscan_url = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c&address=0xce7b1bc3ff9115b64bf4d6b1549f8339d02762f4"
wbnb_bal =  float(dload.json(bscan_url)["result"])/10**18
print(wbnb_bal)
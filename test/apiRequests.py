from cryptocompare_client import CryptocompareClient

subs = ['0~Abucoins~BTC~USD', '0~BTCAlpha~BTC~USD', '0~BTCChina~BTC~USD', '0~BTCE~BTC~USD', '0~BitBay~BTC~USD',
        '0~BitFlip~BTC~USD', '0~BitSquare~BTC~USD', '0~BitTrex~BTC~USD', '0~BitexBook~BTC~USD', '0~Bitfinex~BTC~USD',
        '0~Bitlish~BTC~USD', '0~Bitpoint~BTC~USD', '0~Bitsane~BTC~USD', '0~Bitso~BTC~USD', '0~Bitstamp~BTC~USD',
        '0~CCEDK~BTC~USD', '0~CCEX~BTC~USD', '0~Cexio~BTC~USD', '0~CoinDeal~BTC~USD', '0~CoinHub~BTC~USD',
        '0~Coinbase~BTC~USD', '0~Coincap~BTC~USD', '0~Coinfloor~BTC~USD', '0~Coinroom~BTC~USD', '0~CoinsBank~BTC~USD',
        '0~Coinsbit~BTC~USD', '0~Coinsetter~BTC~USD', '0~Cryptsy~BTC~USD', '0~DSX~BTC~USD', '0~EXRATES~BTC~USD',
        '0~Exenium~BTC~USD', '0~Exmo~BTC~USD', '0~ExtStock~BTC~USD', '0~Gatecoin~BTC~USD', '0~Gateio~BTC~USD',
        '0~Gemini~BTC~USD', '0~Graviex~BTC~USD', '0~Huobi~BTC~USD', '0~Incorex~BTC~USD', '0~IndependentReserve~BTC~USD',
        '0~Kraken~BTC~USD', '0~Kuna~BTC~USD', '0~LakeBTC~BTC~USD', '0~Liqnet~BTC~USD', '0~Liquid~BTC~USD',
        '0~LiveCoin~BTC~USD', '0~LocalBitcoins~BTC~USD', '0~Lykke~BTC~USD', '0~MonetaGo~BTC~USD', '0~NDAX~BTC~USD',
        '0~Neraex~BTC~USD', '0~Nexchange~BTC~USD', '0~OKCoin~BTC~USD', '0~Ore~BTC~USD', '0~P2PB2B~BTC~USD',
        '0~Poloniex~BTC~USD', '0~QuadrigaCX~BTC~USD', '0~Quoine~BTC~USD', '0~Remitano~BTC~USD', '0~RightBTC~BTC~USD',
        '0~Simex~BTC~USD', '0~SingularityX~BTC~USD', '0~StocksExchange~BTC~USD', '0~StocksExchangeio~BTC~USD',
        '0~TheRockTrading~BTC~USD', '0~Threexbit~BTC~USD', '0~TrustDEX~BTC~USD', '0~WEX~BTC~USD', '0~WavesDEX~BTC~USD',
        '0~Yobit~BTC~USD', '0~bequant~BTC~USD', '0~betconix~BTC~USD', '0~binanceusa~BTC~USD', '0~bingcoins~BTC~USD',
        '0~bitFlyer~BTC~USD', '0~bitasset~BTC~USD', '0~bitflyerus~BTC~USD', '0~blockchaincom~BTC~USD',
        '0~btcmex~BTC~USD', '0~btse~BTC~USD', '0~bullish~BTC~USD', '0~bybit~BTC~USD', '0~cobinhood~BTC~USD',
        '0~coinfield~BTC~USD', '0~coinsuper~BTC~USD', '0~coss~BTC~USD', '0~crex24~BTC~USD', '0~crosstower~BTC~USD',
        '0~cryptonex~BTC~USD', '0~currency~BTC~USD', '0~darbfinance~BTC~USD', '0~erisx~BTC~USD', '0~etoro~BTC~USD',
        '0~ftx~BTC~USD', '0~ftxus~BTC~USD', '0~hbus~BTC~USD', '0~idevex~BTC~USD', '0~itBit~BTC~USD', '0~lmax~BTC~USD',
        '0~primexbt~BTC~USD', '0~seedcx~BTC~USD', '0~sigenp2p~BTC~USD', '0~sistemkoin~BTC~USD', '0~tchapp~BTC~USD',
        '0~thore~BTC~USD', '0~utorg~BTC~USD', '0~wbb~BTC~USD', '0~xcoex~BTC~USD']


def generate_streaming_data():
    client = CryptocompareClient()
    client.subscribe(sub_strings=subs)
    return client.listen(seconds=120)

generate_streaming_data()

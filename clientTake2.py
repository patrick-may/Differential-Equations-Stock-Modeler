import polygon
import pandas as pd

api_key = open("config.txt", "r").read()

# only able to get 2 years of historical data :_(
def rangeQuery(ticker):
    # fancy long query
    client = polygon.StocksClient(api_key)
    
    resp = client.get_aggregate_bars(symbol = ticker, from_date="2020-01-03", 
                    to_date = "2022-12-04", timespan = "day", full_range = True)
    
    #resp = client.get_bulk_ticker_details(ticker, from_date="2015-01-03",  to_date = "2022-12-01")
    
    # make pandas data frame
    df = pd.DataFrame(resp)
    df["date"] = pd.to_datetime(df["t"], unit="ms")
    df.drop(columns=["t"], inplace=True)
    
    print(df)
    df.to_json("data.json")
    historical_data = df[["date", "c"]]
    historical_data["day"] = df["date"].apply(lambda x: str(x)[:10])
    hd = historical_data.drop(columns=["date"])
    
    print(hd)
    hd.to_csv(f"{ticker}HistoricalData.csv")
    


if __name__ == "__main__":
    rangeQuery("VIXY")

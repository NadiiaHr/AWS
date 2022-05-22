import json
import boto3
import yfinance as yf

tickers = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
kinesis = boto3.client('kinesis', "us-east-2")

def lambda_handler(a, b):
  
  for ticker in tickers:
    data = yf.download(ticker, start="2022-05-02", end="2022-05-03", interval = "5m")
  
    for datetime, row in data.iterrows():
      result = {'name' : ticker}
      result['high'] = round(row['High'], 2)
      result['low'] = round(row['Low'], 2)
      result['ts'] = str(datetime)
      to_json = json.dumps(result)+"\n"
      print(to_json)
      kinesis.put_record(
                StreamName="kinesis-deliverystream-project3",
                Data=to_json,
                PartitionKey="partitionkey"
                )
  return {
    'statusCode': 200,
    'body': json.dumps("Run Complete!")
  }
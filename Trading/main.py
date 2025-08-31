import os
import requests
from twilio.rest import Client

STOCK_API_KEY = os.getenv("TRADING_API_KEY")
TRADING_NEWS_API_KEY = os.getenv("TRADING_NEWS_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "VOO",
    "apikey": STOCK_API_KEY
}
response = requests.get(stock_endpoint, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

diff = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = diff / float(yesterday_closing_price) * 100
print(diff_percent)

if diff_percent > 0:
    news_params =  {
        "apiKey": TRADING_NEWS_API_KEY,
        "qInTitle": "VOO"
    }
    response = requests.get(news_endpoint, params=news_params)
    articles = response.json()["articles"]
    three_articles = articles[:3]
    
    
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    
    for article in formatted_articles:
        client = Client(ACCOUNT_SID, TWILIO_TOKEN)
        message = client.messages.create(
            body=article,
            from_="+14632087513",
            to="+40774621904"
        )
import os
import requests
import urllib.parse
from flask import redirect, render_template, session
from functools import wraps
import finnhub
import yfinance as yf 
import json
from nsepython import * 

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    
    # finnhub_client = finnhub.Client(api_key="cfop1dpr01qm7nlt1vngcfop1dpr01qm7nlt1vo0")
    # result = finnhub_client.symbol_lookup(symbol)
    # price = finnhub_client.quote(symbol)["c"] * 75
    # if price == 0:
    
    try:
         
        price = nse_eq(symbol)["priceInfo"]["close"]
        stock = nse_eq(symbol)
        return {
            "name":nse_eq(symbol)["info"]["companyName"],
            "symbol":nse_eq(symbol)["info"]["symbol"],
            "price":nse_eq(symbol)["priceInfo"]["close"]
            
        }
    except  (KeyError, TypeError, ValueError):
        return None  
    
    # apikey = "PDI8EFNKBI2MKU4D"
    
    # """Look up quote for symbol."""
    # try:

    #     urlForStockInfo = "https://yh-finance.p.rapidapi.com/auto-complete"

    #     querystring = {"q":{symbol}}

    #     yhheaders = {
    #         "X-RapidAPI-Key": "6353e02cf9mshc4eba3ae77bbcb4p149f87jsnd1b972f8b27b",
    #         "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
    #     }

    #     stockInfoResponse = requests.request("GET", urlForStockInfo, headers=yhheaders, params=querystring)

   
            
    #     urlForStockPrice = "https://yfinance-stock-market-data.p.rapidapi.com/price"

    #     payload = f"symbol={symbol}&period=1d"
    #     headers = {
    #         "content-type": "application/x-www-form-urlencoded",
    #         "X-RapidAPI-Key": "6353e02cf9mshc4eba3ae77bbcb4p149f87jsnd1b972f8b27b",
    #         "X-RapidAPI-Host": "yfinance-stock-market-data.p.rapidapi.com"
    #     }

    #     stockPriceResponse = requests.request("POST", urlForStockPrice, data=payload, headers=headers)
        
        
    #     stockInfoResponse.raise_for_status()
    #     stockPriceResponse.raise_for_status()
    # except requests.RequestException:
    #     return None
    
    # try:
    #     data = stockInfoResponse.json()
    #     price = stockPriceResponse.json()
    #     return {
    #     "name":data["quotes"][0]["shortname"],
    #     "symbol":data["quotes"][0]["symbol"],
    #     "price": (float(price["data"][0]["Close"]) * 75)
    # }
    # except  (KeyError, TypeError, ValueError):
    #     return None    
    

    

def inr(value):
    """Format value as inr."""
    return f"₹{(value):,.2f}"

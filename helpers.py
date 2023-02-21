import os
import requests
from flask import redirect, render_template, session
from functools import wraps
import yfinance as yf 
import json
from nsetools import Nse

nse = Nse()

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
    
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):    
    try:
        company = nse.get_quote(symbol)
        return {
            "name":company['companyName'],
            "symbol":company['symbol'],
            "price": company['basePrice']
            
        }
    except  (KeyError, TypeError, ValueError):
        return None  


def inr(value):
    """Format value as inr."""
    return f"₹{(value):,.2f}"

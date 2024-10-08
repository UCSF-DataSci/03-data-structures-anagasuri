#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    # Create a list of quotes here
              "The greatest glory in living lies not in never falling, but in rising every time we fall.", 
              "The way to get started is to quit talking and begin doing.",
              "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
              "The future belongs to those who believe in the beauty of their dreams.",
              "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."
]

def get_quote_of_the_day(quotes):
    todays_quote = None

    # Your code here
    todays_quote = random.choice(quotes) 
    
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt 

# 0 8 * * * /usr/bin/python3 /workspaces/03-data-structures-anagasuri/01-daily_quote.py >> /workspaces/03-data-structures-anagasuri/daily_quote.txt 
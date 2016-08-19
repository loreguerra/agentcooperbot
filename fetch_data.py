from ca_markov.cc_markov import MarkovChain
import csv
import re

#reading scrapy item CSV file and writing into strings

def get_quote_list():
    quote_list = ""
    with open('dalecooper_scrapy/items.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            row = str(row)
            quote = re.sub(r'[\[\]\"\']', '', row)
            if quote == "quote":
                del quote
            else:
                quote_list += quote + "\n"
        return quote_list

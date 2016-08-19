from ca_markov.cc_markov import MarkovChain
import csv
import re

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
    print quote_list

#with open('quotes.txt', 'w') as output_file:
#        output_file.write(row)

#mc = MarkovChain()

#quotes = mc.add_file('quotes.txt')

#mc.generate_text()

from ca_markov.cc_markov import MarkovChain
import csv
import re

quote_list = ""

with open('dalecooper_scrapy/items.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        row = str(row)
        quote = re.sub(r'[\[\]\"\']', '', row)
        quote_list += quote + "\n"
    print quote_list

#with open('quotes.txt', 'w') as output_file:
#        output_file.write(row)



#with open('quotes.txt', 'w') as outfile:
#    json.dump(json_file, outfile)

#mc = MarkovChain()

#quotes = mc.add_file('quotes.txt')

#mc.generate_text()

from ca_markov.cc_markov import MarkovChain
import json

with open('dalecooper_scrapy/quotes.json') as data_file:
    json_file = json.load(data_file)

with open('quotes.txt', 'w') as outfile:
    json.dump(json_file, outfile)

#mc = MarkovChain()

#quotes = mc.add_file('quotes.txt')

#mc.generate_text()

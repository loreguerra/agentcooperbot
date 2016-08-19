from ca_markov.cc_markov import MarkovChain

mc = MarkovChain()

mc.add_file('dalecooper_scrapy/quotes.json')

mc.generate_text()

# convert json to text file, use function to load and generate text

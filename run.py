from ca_markov.cc_markov import MarkovChain
import fetch_data

#use function from fetch_data to grab CSV file and turn into strings

quote_list = fetch_data.get_quote_list()

print quote_list

from ca_markov.cc_markov import MarkovChain
import fetch_data

#instance of MarkovChain
mc = MarkovChain()

#use function from fetch_data to grab CSV file and turn into strings
quote_list = fetch_data.get_quote_list()

#Adding string to use to instance and generating text from instance
MarkovChain.add_string(mc, quote_list)
MarkovChain.generate_text(mc)

#create function to call generate_text in reply
#join list of words into string
#display string as "Special Agent Dale Cooper: {string}"

from ca_markov.cc_markov import MarkovChain
import fetch_data

#instance of MarkovChain
mc = MarkovChain()

#use function from fetch_data to grab CSV file and turn into strings
quote_list = fetch_data.get_quote_list()

#Adding string to instance and generate markoved text from instance
MarkovChain.add_string(mc, quote_list)

markov_text = MarkovChain.generate_text(mc)
#if markov_text[len(markov_text)-1] in naughty_words_list
first_letter = markov_text[0][0].upper()
first_word_lower = markov_text[0]
partial_word = first_word_lower[1:]
first_word_upper = first_letter + partial_word
markov_text.pop(0)
sentence = '%s %s' % (first_word_upper, ' '.join(markov_text))
print sentence

#create function to call generate_text in reply
#capitalize first word letter
# if sentence contains "why, what, who, where" add '?' to end
#if last word is 'if, at, the, of, and, that, he, she, are' delete and finish sentence - loop?
#join list of words into string
#display string as "Special Agent Dale Cooper: {string}"

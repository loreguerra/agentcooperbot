from ca_markov.cc_markov import MarkovChain
import fetch_data
import filter_words

#instance of MarkovChain
mc = MarkovChain()

#use function from fetch_data to grab CSV file and turn into strings
quote_list = fetch_data.get_quote_list()

#Adding string to instance and generate markoved text from instance
MarkovChain.add_string(mc, quote_list)

# Filter out weird sentence endings, capitalize first word and names
def create_reply():
    markov_text = MarkovChain.generate_text(mc)
    markov_filtered = []
    for word in markov_text:
        if word == markov_text[0]:
            markov_filtered.append(word.title())
        elif word in filter_words.names:
            markov_filtered.append(word.title())
        #change to lambda filter?
        elif markov_text[len(markov_text)-1] in filter_words.naughty_sentence_enders:
            del markov_text[len(markov_text)-1]
        else:
            markov_filtered.append(word)
    sentence = 'Special Agent Dale Cooper: %s.' % (' '.join(markov_filtered))
    print sentence

create_reply()


#get rid of duplicate words in a row
#generate random sentence ending punctuation? either . or ?
#create function to call generate_text in reply

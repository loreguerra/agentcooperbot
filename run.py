from ca_markov.cc_markov import MarkovChain
import fetch_data

#instance of MarkovChain
mc = MarkovChain()

#use function from fetch_data to grab CSV file and turn into strings
quote_list = fetch_data.get_quote_list()

naughty_sentence_enders = ['if', 'at', 'the', 'of', 'and', 'that', 'he', 'she', 'are', 'a', 'whos', 'let', 'ive', 'to', 'theyre', 'shes', 'i' ,'in', 'it', 'with']
names = ['laura', 'palmer', 'leo', 'johnson', 'sheriff', 'agent', 'dale', 'cooper', 'mayor', 'lana', 'albert', 'james', 'hurley', 'annie', 'caroline', 'i', 'carl', 'audrey', 'gordon', 'bob', 'harry', 'twin peaks', 'lucy', 'andy', 'diane' 'maddy', 'ferguson', 'mr', 'packard', 'leland', 'great northern hotel']
#import names^^ from external list - json?

#Adding string to instance and generate markoved text from instance
MarkovChain.add_string(mc, quote_list)

# Filter out weird sentence endings, capitalize first word and names
def create_reply():
    markov_text = MarkovChain.generate_text(mc)
    markov_filtered = []
    for word in markov_text: #change to lambda filter?
        if markov_text[len(markov_text)-1] in naughty_sentence_enders:
            del markov_text[len(markov_text)-1]
        elif word == markov_text[0]:
            markov_filtered.append(word.title())
        elif word in names:
            markov_filtered.append(word.title())
        else:
            markov_filtered.append(word)
    sentence = ' '.join(markov_filtered)
    print sentence

create_reply()

#create function to call generate_text in reply
#display string as "Special Agent Dale Cooper: {string}"

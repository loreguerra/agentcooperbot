from ca_markov.cc_markov import MarkovChain
import fetch_data

#instance of MarkovChain
mc = MarkovChain()

#use function from fetch_data to grab CSV file and turn into strings
quote_list = fetch_data.get_quote_list()

naughty_sentence_enders = ['if', 'at', 'the', 'of', 'and', 'that', 'he', 'she', 'are', 'a', 'whos', 'let', 'ive', 'to', 'theyre', 'shes', 'i' ,'in', 'it']
names = ['laura', 'palmer', 'leo', 'johnson', 'sheriff', 'agent', 'dale', 'cooper', 'mayor', 'lana', 'albert', 'james', 'hurley', 'annie', 'caroline', 'i', 'carl', 'audrey', 'gordon', 'bob', 'harry', 'twin peaks', 'lucy', 'andy', 'diane' 'maddy', 'ferguson', 'mr', 'packard', 'leland', 'great northern hotel']
#import names^^ from external list - json?

#Adding string to instance and generate markoved text from instance
MarkovChain.add_string(mc, quote_list)

def create_reply():
    markov_text = MarkovChain.generate_text(mc)
    markov_filtered = []
    for word in markov_text: #change to lambda filter?
        if markov_text[len(markov_text)-1] in naughty_sentence_enders:
            del markov_text[len(markov_text)-1]
        elif word in names:
            markov_filtered.append(word.title())
        else:
            markov_filtered.append(word)

    #creating capitalized first word. would like to refactor later
    first_letter = markov_filtered[0][0].upper()
    first_word_lower = markov_filtered[0]
    first_word_upper = first_letter + first_word_lower[1:]
    markov_filtered.pop(0)
    sentence = '%s %s' % (first_word_upper, ' '.join(markov_filtered))
    print sentence

create_reply()

#create function to call generate_text in reply
#if last word is 'if, at, the, of, and, that, he, she, are' delete and finish sentence - loop?
#display string as "Special Agent Dale Cooper: {string}"

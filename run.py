from ca_markov.cc_markov import MarkovChain
import fetch_data
import filter_words
from time import sleep

#instance of MarkovChain
mc = MarkovChain()

#use function from fetch_data to grab CSV file and turn into strings
quote_list = fetch_data.get_quote_list()

#Adding string to instance and generate markoved text from instance
MarkovChain.add_string(mc, quote_list)

# display loading... connecting... display status, type exit to exit, display hello from cooper
# listen for input, generate response
USER_NICK = ''
DC_NICK = 'spagent_dc2'

print 'Connecting...'
sleep(2)
print 'Loading...'
sleep(2)
print 'Connected. You are now online with spagent_dc2. Type "exit" to exit anytime. Specify your nickname with /nick.\n\n'
print '%s: Special Agent Dale Cooper here.\n' % DC_NICK
USER_NICK = raw_input('/nick:')

# format user input
def user_input():
    user_reply = raw_input('%s: ' % USER_NICK)
    if user_reply == 'exit':
        quit()

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
    sentence = '%s: %s.' % (DC_NICK, ' '.join(markov_filtered))
    print sentence

#create function to call generate_text in reply
while True:
    user_input()
    sleep(3)
    create_reply()

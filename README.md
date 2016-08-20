# Special Agent Dale Cooper bot

Building a chat bot with the Markov Chain module from Codecademy, using Scrapy to collect the best quotes from Dale Cooper via IMDb.

Right now, the quotes are extracted according to actor URL, cleaned up, and dumped into a CSV file using a feed export.

In the future, I'd like to set up a pipeline and use a CSV item exporter to export the data to a CSV file, so everything is automated.

I currently have the spider cleaning up the extracted data before writing to the item and then fetch_data.py reading the CSV, cleaning it up again, and adding to a list of strings. I'd like to have either the spider or fetch_data.py do one process to clean up the text, but not both files with two separate processes.

##Ideas for future versions

1. Scrape more sites for more quotes
2. Create GUI for chatting
3. Add emojis
4. Modify the Markov module
5. Figure out how to get natural-sounding sentences
6. Spell check quotes
7. Check for duplicate words in a row

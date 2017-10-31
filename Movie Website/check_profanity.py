import os
import urllib

def read_text():
    quotes = open(os.path.expanduser("~/Desktop/Intro to Programming Nanodegree/Movie Website/movie_quotes.txt"))
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print ("Whoa, profanity was found!")
    elif "false" in output:
        print ("This document has no profanity.")
    else:
        print ("Could not scan this document properly.")

read_text()

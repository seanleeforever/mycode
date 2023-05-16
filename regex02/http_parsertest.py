import requests
import re


def main():

    print("Welcome to the simple HTTP response parser. Where should we search (ex: https://alta3.com)?\n type quit to quit")
    url = input()
    
    while url != "quit":
        print(f"Great! So we will try to open this url {url} to search for the phrase:")
        searchfor = input()
        searchMe = requests.get(url).text
        #print (searchMe)
        if re.search(searchfor, searchMe):
            print(f"Found a match!")
            match=re.findall(searchfor,searchMe)
            print(match)
            print("Found ",match.count(searchfor),f"occurance of {searchfor} phrase")
        else:
            print("no match")
        print("Welcome to the simple HTTP response parser. Where should we search (ex: https://alta3.com)?\n type quit to quit")
        url = input()

if __name__ == "__main__":
    main()

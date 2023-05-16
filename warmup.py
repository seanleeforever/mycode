import requests
API="http://api.open-notify.org/astros.json"
def main():
    gotresp = requests.get(API)

    get_dj = gotresp.json()

    ## print the response
    print(get_dj)
    print ("type of get_dj is", type(get_dj))

    dictionaryof=get_dj["people"]
    print("type of dictionaryof is ",type(dictionaryof))
    print(dictionaryof)
    
    ## display only the keys within
    ## the dictionary by using dict.keys()
    print ("people in space:", get_dj["number"])
    for people in dictionaryof:
        print(people["name"], "is on the", people["craft"] )
    

if __name__=="__main__":
    main()
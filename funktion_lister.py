import random

def __main__():
    #1.1
    items = ["apple","orange","banana","pear"]
    items.append("strawberry")
    print(items)

    #1.2
    print(items[0])
    
    #1.3
    items[3] = "pineapple"
    print(items)

    #1.4
    sameitems = ["a","b","c","d","d","d"]

    #1.5
    jokes = ["Jeg overvejer at gifte mig med en tysker er det over grænsen?","Alle børnene kom sikkert hjem fra fabrikken undtagen Ib og Arne de blev til chili konkarne"]
    print(jokes[random.randrange(len(jokes))])


if __name__ == "__main__":
    __main__()
     
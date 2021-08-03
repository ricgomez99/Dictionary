import json

def search():
    search_term = input("Enter search Term: ")
    with open('glossary.json') as data:
        term_data = json.load(data)
    print("{} - {}".format(search_term, term_data[search_term]))

def write():
    term = input("Enter term: ")
    define_term = input("Enter the definition for term: ")

    #open
    with open('glossary.json') as data:
        term_data = json.load(data)
    term_data[term] = define_term
    #write
    with open('glossary.json', "w") as data:
        json.dump(term_data, data)


response = input("Search terms or add term\n Enter search or write: ")

if response.casefold() == "search":
    search()
elif response.casefold() == "write":
    write()
else:
    print("Program Failed.")
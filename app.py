import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def all():
    for i in (data):
        print(i["title"])

def beforeAndAfterYear():
    yearAfter = int(input("Movies after what year do you want to view? "))
    yearBefore = int(input("Movies before what year do you want to view? "))
    alreadyPrint = []
    for i in (data):
        if i["year"] > yearAfter:
            print(i["title"])
            alreadyPrint.append(i["title"])

        if i["year"] > yearBefore and not i["title"] in alreadyPrint:
            print(i["title"])

def year():
    year = int(input("From what year do you want to see moveis from? "))
    for i in (data):
        if i["year"] == year:
            print(i["title"])

def beforeYear():
    year = int(input("Movies before what year do you want to view? "))
    for i in (data):
        if i["year"] < year:
            print(i["title"])

def afterYear():
    year = int(input("Movies after what year do you want to view? "))
    for i in (data):
        if i["year"] > year:
            print(i["title"])
def genre():
    genre = input("What genre do you want to search for? ")
    for i in (data):
        if genre in i["genres"]:
            print(i["title"])

def all():
    sortType = input("Do you want to search for movies on a specific year (say 'year'), before a year (say 'before'), after a year (say 'after'), or a specific genre (say genre') ")
    if sortType == "year":
        year()
    elif sortType == "before":
        beforeYear()
    elif sortType == "after":
        afterYear()
    elif sortType == "genre":
        genre()
    else:
        print("invalid input stupid")
all()
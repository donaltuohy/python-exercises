##################################
#
#  Exercise 22: Reading form a file
#  https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
#
##################################

import requests

nameCount = {}

with open("./data/names.txt", "r+") as names_file:
    names = names_file.read().split("\n")
    
    for name in names:
        if name in nameCount:
            nameCount[name] += 1
        else:   
            nameCount[name] = 1 

    print(nameCount)




catCount = {}

with open("./data/categories.txt", "r+") as cats_file:
    lines = cats_file.read().split("\n")

    for line in lines:
        cat = line.split("/")[2]
        if cat in catCount:
            catCount[cat] +=1
        else:
            catCount[cat] = 1


    print(catCount)




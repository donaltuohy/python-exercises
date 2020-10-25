##################################
#
#  Exercise 23: File overlap
#  https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
#
##################################

def readFileOfNumbersIntoList(filename):
    list = []

    with open(filename) as file:
        line = file.readline()

        while line:
            list.append(int(line))
            line = file.readline()
    
    return list

if __name__ == "__main__":
    primes = readFileOfNumbersIntoList("./data/primes.txt")
    happies = readFileOfNumbersIntoList("./data/happy.txt")

    overlap = [prime for prime in primes if prime in happies]

    print(overlap)

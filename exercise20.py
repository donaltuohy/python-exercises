##################################
#
#  Exercise 20: Element Search
#  https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
#
##################################

import random as rand

def elementSearch(list, element, x):
    x += 1
    list.sort()
    listLen = len(list)
    half = listLen // 2
    
    if listLen <= 2:
        return element in list
    elif list[half] == element:
        return True
    elif list[half] > element:
        return elementSearch(list[:half], element, x)
    elif list[half] < element:
        return elementSearch(list[half:], element, x)



def main():
    list = [rand.randint(0, 100) for _ in range(LIST_SIZE)]
    x = 0
    a = [1,2,3,4,5,6,7,8, 9]

    print("firstSearch: " + str(elementSearch(a, 6, x)))
    print("firstSearch: " + str(elementSearch(a, 20, x)))
    print("firstSearch: " + str(elementSearch(a, 1, x)))
    print("firstSearch: " + str(elementSearch(a, 8, x)))
    print("firstSearch: " + str(elementSearch(a, 10, x)))


if __name__ == "__main__":
    LIST_SIZE = 10
    main()    
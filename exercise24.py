##################################
#
#  Exercise 24: Game Board
#  https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
#
##################################

rowString = " ---"

colString = "|   "

def drawRow(width):
    print(rowString * width)
        
def drawColumn(width):
    print(colString * (width + 1))

def drawGrid(width, height):
    drawRow(width)
    for _ in range(height):
        drawColumn(width)
        drawRow(width)


def main():
    width = int(input("What width: "))
    height = int(input("What height: "))

    drawGrid(width, height)

if __name__ == "__main__":
    main()

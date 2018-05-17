import turtle

#main function that gets the input colors and box width from the user and passes these to createChessBoard function
def main():
    #Get inputs
    colorsInput = input("Enter two colors separated by comma to fill your chess board= ")
    boxWidth = int(input("Enter the box width= "))

    #colrsInput is a single string, so we use split method to create a list of values from that string
    colorsList = colorsInput.split(",")
    color1 = colorsList[0] #first color will be in index 0 in the list
    color2 = colorsList[1] #second color will be in index 1

    print(colorsList) #Show the colors list
    print("Box Width= ", boxWidth)

    #pass the two colors and boxWidth to this function
    createChessBoard(color1, color2, boxWidth)


#Uses nested loop to create the board using createBox function to create boxes by column first and then rows
def createChessBoard(firstColor, secondColor, boxWidth):
    #Starting point
    x = -800
    y = 0

    #Nested loop
    for row in range(8): #start with each row and finish all columns
        for column in range(8):
            if((row + column) % 2 == 0): #a simple mathematical formula that helps to replace lots of if conditionals to
                                            #create alternating colors in each row
                color = firstColor
            else:
                color = secondColor

            createBox(x,y,color, boxWidth) #call the createBox to create a box at the starting points and use the passed color
            x = x + boxWidth #after creating a box, move its x-coordinate by adding boxWidth to move left.
                    # Eg; if boxwidth = 50, and x starts at 0, then series will be 0,50,100,150,200,250,300,350

        #after finishing all columns,
        x = -800 #start x at same point again
        y = y + boxWidth #increase y by boxWidth so that it moves up now.

#creates a box at passed starting point with the color and boxWidth
def createBox(startX, startY, color, boxWidth):
    turtle.hideturtle()
    turtle.speed(0)

    #goto the passed starting point
    turtle.penup()
    turtle.goto(startX,startY)
    turtle.pendown()

    turtle.fillcolor(color) #use the passed color to fill
    turtle.begin_fill()
    for i in range(4): #loop 4 times as 4 lines create a box
        turtle.forward(boxWidth)
        turtle.left(90) #take left turn by 90 degrees
    turtle.end_fill()

#start with main function
main()

#These 2 lines are for pycharm IDE to hold the turtle window. If you use Python's default IDLE, you can remove this.
import time
time.sleep(5)

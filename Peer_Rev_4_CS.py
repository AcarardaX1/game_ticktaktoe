

def displayTable(table):

    print("*" * 50) #Value is arranged by "50" to the interpreter

    for anything in range(len(table)):
        for blablab in range(len(table[anything])):
            print(f"_", end=" ")

        print(" ")


def rowControl(table):
    counterval1 = 0
    counterval2 = 0

    for hehehe in range(len(table)):
        for bruh in range(len(table[hehehe])):

            if table[hehehe][bruh] == "X":
                counterval1 += 1

            if table[hehehe][bruh] == "O":
                counterval2 += 1

        if counterval1 == 3:
            return (True, "user1")
        if counterval2 == 3:
            return (True, "user2")

        counterval1 = 0 #Hell Yeah, checking and debugging1
        counterval2 = 0 #Hell Yeah, checking and debugging2
    return False, "Nothing"

def columnControl(table):
    count1 = 0
    count2 = 0

    for i in range(len(table)):
        for j in range(len(table[i])):

            if table[j][i] == "X":
                count1 += 1

            if table[j][i] == "O":
                count2 += 1


        if count1 == 3:
            return (True, "user1")
        if count2 == 3:
            return (True, "user2")

        count1 = 0 #No more hell yeah, but checking and debugging1
        count2 = 0 #No more hell yaeh, but chekcing and debugging2
    return False, "Nothing"

def diaganolControl(table): 

    u1 = 0
    u2 = 0

    for x in range(len(table)):

        if table[x][x] == "X":
            u1 += 1

        if table[x][x] == "O":
            u2 += 1


        if u1 == 3:
            return (True, "user1")
        if u2 == 3:
            return (True, "user2")

        u1 = 0 #Feel Free1
        u2 = 0 #Feel Free2

    for i in (range(len(table))):
        for k in reversed(range(len(table[i]))): 

            if table[i][k] == "X":
                u1 += 1

            if table[i][k] == "O":
                u2 += 1

        if u1 == 3:
            return (True, "user1")
        if u2 == 3:
            return (True, "user2")

            u1 = 0
            u2 = 0
    return False, "Nothing"

def Tie_def(table):
    gg = False
    emptyspaces = 9


    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != "_":
                emptyspaces -= 1

    if emptyspaces==0:
       gg = True
       print("Result: Draw, The game is over! ")

    return gg


def updateTable(table, user):


    row = int(input("Please, Specify the row:"))
    column = int(input("Please, Specify the column:"))


    while row not in [1,2,3] and column not in [1,2,3] and table[row][column] != "_":
         row = int(input("Please, Specify the row:"))
         column=int(print("Please, Specify the column:"))


    table[row-1][column-1] = "X" if user == "USER1" else "O" 

    return table


def whoWin(table):

    (row1, row2) = rowControl(table)
    (column1, column2) = columnControl(table)
    (diagonal1, diagonal2) = diaganolControl(table)

    finishGame = False

    if(row1):

        print("*" * 20, row2, " Congrats!", "*" * 20)
        finishGame = True
        return finishGame

    elif(column1):


        print("*" * 20, column2, " Congrats!", "*" * 20)
        finishGame = True
        return finishGame

    elif(diagonal1):


        print("*" * 20, diagonal2, " Congrats!", "*" * 20)
        finishGame = True
        return finishGame

    return finishGame

def startGame():

    print("X is for User1")
    print("O is for User2")

    table = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]

    userDetermine = 0

    while(True):



        if(userDetermine % 2 == 0):
            displayTable(updateTable(table, "USER1"))
            userDetermine += 1
        elif(userDetermine % 2 == 1):
            displayTable(updateTable(table, "USER2"))
            userDetermine += 1

        if(Tie_def(table)):
            break
        if(whoWin(table)):
            break






startGame()







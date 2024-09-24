# Record structure
class characterInfo:
    def __init__(self, characterID, name, HP, DF, status, creationDate, creationTime):
        self.characterID = str(characterID)
        self.name = str(name)
        self.HP = int(HP)
        self.DF = int(DF)
        self.status = str(status)
        self.creationDate = creationDate
        self.creationTime = creationTime


def createArrayOfRecords():
    characters = [] # Array to store records

    userInput = int(input("Enter how many characters you want to create(between 5 and 10): ")) # The user inputs how many characters they want to create
    while userInput > 10 or userInput < 5:
        print("Error, you can only create 5 to 10 characters.")
        userInput = int(input("Try again: "))

    for counter in range(userInput): # A new record is created, populated with data and stored in an array for each character to be created
        insertInfo(counter, characters)

    print("Unsorted array of records:")
    displayArrayOfRecords(characters) # The unsorted array of records is displayed to the user
    return characters


def insertInfo(counter, characters):
    randomLetter = chr(random.randrange(65,90)) # Program generates a random capital letter
    randomNumber = random.randrange(1,9) # Program generates a random number between 1 and 9
    ID = randomLetter + str(randomNumber) + str(counter) # Program concatenates the random capital letter, the random number
                                                         # and the number of what character is currently being created which makes this value unique

    charaName = str(input("Enter a character name for character " + str(counter+1) + ": "))
    while len(charaName) > 30:
        print("Error, character name can only have a length 30 or lower.")
        charaName = str(input("Try again: "))

    healthPoints = int(input("Enter character " + str(counter+1) + "'s health points (between 1 and 128): "))
    while healthPoints > 128 or healthPoints < 1:
        print("Error, a character's health points must be between 1 and 128.")
        healthPoints = int(input("Try again: "))
    
    defencePoints = int(input("Enter character " + str(counter+1) + "'s defence points (between 25 and 75): "))
    while defencePoints > 75 or defencePoints < 25:
        print("Error, a character's defence points must be between 25 and 75.")
        defencePoints = int(input("Try again: "))

    charaStatus = str(input("Enter whether character " + str(counter+1) + " is either Neutral(n), Friendly(f) or Hostile(h): "))
    while charaStatus != "n" and charaStatus != "f" and charaStatus != "h":
        print("Error, you can only enter n, f or h.")
        charaStatus = str(input("Try again: "))
    if charaStatus == "n":
        charaStatus = "Neutral"
    elif charaStatus == "f":
        charaStatus = "Friendly"
    else:
        charaStatus = "Hostile"

    dt = datetime.datetime.now()
    date = dt.strftime("%Y-%m-%d")
    time = dt.strftime("%X")

    characters.append(characterInfo(ID, charaName, healthPoints, defencePoints, charaStatus, date, time))
    print("\n")


def displayArrayOfRecords(characters):
    for index in range(len(characters)):
        print(characters[index].characterID, characters[index].name, characters[index].HP, characters[index].DF, characters[index].status,
              characters[index].creationDate, characters[index].creationTime)
    print("\n")


def userChooseHPorDF():
    userChoice = str(input("Enter for either health points(HP) or defence points(DF) to be used: "))                                                                                           
    while userChoice != "HP" and userChoice != "DF":
        print("Error, you can only enter either HP or DF.")
        userChoice = str(input("Try again: "))
    print("\n")
    return userChoice


def swap(item1, item2):
    return item2, item1


def insertionSort(characters, userChoice):
    for outer in range(1, len(characters)):
        inner = outer
        if userChoice == "HP":
            while inner > 0 and characters[inner-1].HP > characters[inner].HP:
                characters[inner-1].characterID, characters[inner].characterID = swap(characters[inner-1].characterID, characters[inner].characterID)
                characters[inner-1].name, characters[inner].name = swap(characters[inner-1].name, characters[inner].name)
                characters[inner-1].HP, characters[inner].HP = swap(characters[inner-1].HP, characters[inner].HP)
                characters[inner-1].DF, characters[inner].DF = swap(characters[inner-1].DF, characters[inner].DF)
                characters[inner-1].status, characters[inner].status = swap(characters[inner-1].status, characters[inner].status)
                characters[inner-1].creationDate, characters[inner].creationDate = swap(characters[inner-1].creationDate, characters[inner].creationDate)
                characters[inner-1].creationTime, characters[inner].creationTime = swap(characters[inner-1].creationTime, characters[inner].creationTime)
                inner -= 1
                
        else:
            while inner > 0 and characters[inner-1].DF > characters[inner].DF:
                characters[inner-1].characterID, characters[inner].characterID = swap(characters[inner-1].characterID, characters[inner].characterID)
                characters[inner-1].name, characters[inner].name = swap(characters[inner-1].name, characters[inner].name)
                characters[inner-1].HP, characters[inner].HP = swap(characters[inner-1].HP, characters[inner].HP)
                characters[inner-1].DF, characters[inner].DF = swap(characters[inner-1].DF, characters[inner].DF)
                characters[inner-1].status, characters[inner].status = swap(characters[inner-1].status, characters[inner].status)
                characters[inner-1].creationDate, characters[inner].creationDate = swap(characters[inner-1].creationDate, characters[inner].creationDate)
                characters[inner-1].creationTime, characters[inner].creationTime = swap(characters[inner-1].creationTime, characters[inner].creationTime)
                inner -= 1
            
    print("Sorted array of records using an insertion sort:")
    displayArrayOfRecords(characters)


def selectInformation(characters, userChoice):
    selectedInfo = []
    if userChoice == "HP":
        for counter in range(len(characters)):
            selectedInfo.append(characters[counter].HP)
    else:
        for counter in range(len(characters)):
            selectedInfo.append(characters[counter].DF)
            
    print("Selected information:")
    print(selectedInfo)
    return selectedInfo


def binarySearch(selectedInfo):
    userValue = int(input("Using the information above, enter what value you want to search for: "))
    start = 0
    end = len(selectedInfo) - 1
    mid = 0
    comparisons = 0
    position = -1
    while end >= start:
        mid = int((end + start)/2)
        comparisons += 1
        if selectedInfo[mid] == userValue:
            position = mid
            break
        elif selectedInfo[mid] < userValue:
            start = mid + 1
        else:
            end = mid - 1            
    return position, comparisons

             
def saveResults(position, selectedInfo, comparisons):
    if position == -1:
        print("Value was not found in the sorted array of records.")
    else:
        print("Value was found in the sorted array of records.")

    textFile = open("SearchResults.txt", "w")
    if position == -1:
        textFile.write(str(selectedInfo[position]) + " was not found at any position in the sorted array." + "\n")
        textFile.write("The binary search took " + str(comparisons) + " comparisons and did not find the value.")
    else:
        textFile.write(str(selectedInfo[position]) + " was found at position " + str(position) + " in the sorted array." + "\n")
        textFile.write("The binary search took " + str(comparisons) + " comparisons to find " + str(selectedInfo[position]) + " in the sorted array.")
    textFile.close()
    
    print("View information based on search in an external text file.")
    print("\n")


def createDatabase():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "stuartG",
    password = "340HAj5m?"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE CharacterData;")
    print("\n")
    print("MySQL connection has been made and a database has been created.")


def createTable():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "stuartG",
    password = "340HAj5m?",
    database = "CharacterData"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE Characters(CharacterID VARCHAR(3) UNIQUE NOT NULL, Name VARCHAR(30) NOT NULL, HealthPoints INT NOT NULL CHECK(HealthPoints BETWEEN 1 AND 128), DefencePoints INT NOT NULL CHECK(DefencePoints BETWEEN 25 AND 75), Status VARCHAR(8) NOT NULL, CreationDate DATE NOT NULL, CreationTime TIME NOT NULL, PRIMARY KEY(CharacterID));") 
    print("\n")
    print("A table has been created.")


def insertAllIntoTable(characters):
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "stuartG",
    password = "340HAj5m?",
    database = "CharacterData"
    )
    mycursor = mydb.cursor()
    for index in range(len(characters)):
        sql = "INSERT INTO Characters (CharacterID, Name, HealthPoints, DefencePoints, Status, CreationDate, CreationTime) VALUES(%s, %s, %s, %s, %s, %s, %s);"
        val = characters[index].characterID, characters[index].name, characters[index].HP, characters[index].DF, characters[index].status, characters[index].creationDate, characters[index].creationTime
        mycursor.execute(sql, val)
        mydb.commit()
    print("\n")
    print("All character information has been inserted into a database.")


def menu(characters, userChoice):
    print("\n")
    print("Menu:")
    print("1) Display the table.")
    print("2) Update a record from the table.")
    print("3) Delete a record from the table.")
    print("4) End the program.")
    userMenu = int(input("Using the menu above, enter what you want the program to do: "))
    while userMenu < 1 or userMenu > 4:
        print("Error, the menu only has 4 options (enter from 1 to 4 only).")
        userMenu = int(input("Try again: "))
    print("\n")
    # Option to display the table
    if userMenu == 1:
        displayTable(userChoice)
        menu(characters, userChoice) # Menu is repeated
    
    # Option to update a record from the table, EXCLUDES updating Character ID   
    elif userMenu == 2:
        characters = updateFromTable(characters)
        menu(characters, userChoice) # Menu is repeated

    # Option to delete a record from the table
    elif userMenu == 3:
        characters = deleteFromTable(characters)
        menu(characters, userChoice) # Menu is repeated

    # Option to end the entire program and asks user again before the program proceeds
    else:
        endChoice = str(input("Are you sure you want to end the program, Yes(y) or No(n)? "))
        while endChoice != "y" and endChoice != "n":
            print("Error, Yes(y) and No(n) are the only options available.")
            endChoice = str(input("Try again: "))
            
        if endChoice == "y":
            print("Program ended.")
        else:
            menu(characters, userChoice) # Menu is repeated


def displayTable(userChoice):
    print("Displaying the table selected.")
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "stuartG",
    password = "340HAj5m?",
    database = "CharacterData"
    )
    mycursor = mydb.cursor()
    
    if userChoice == "HP":
        mycursor.execute("SELECT * FROM Characters ORDER BY HealthPoints ASC")
    else:
        mycursor.execute("SELECT * FROM Characters ORDER BY DefencePoints ASC")
    data = mycursor.fetchall()
    for index in data:
        print(index)
    print("Entire table has been displayed.")

  
def selectID(mycursor, characters):
    mycursor.execute("SELECT CharacterID FROM Characters")
    data = mycursor.fetchall()
    print("All Character ID's:")
    for index in data:
        print(index)
        
    userInputID = str(input("Using the information displayed above, select the record from the table: "))
    found = False
    position = -1
    for index in range(len(characters)):
        if characters[index].characterID == userInputID:
            found = True
            position = index
            break      
    return found, position, userInputID


def updateFromTable(characters):
    print("Record updating selected.")   
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "stuartG",
    password = "340HAj5m?",
    database = "CharacterData"
    )
    mycursor = mydb.cursor()
    
    found, position, userInputID = selectID(mycursor, characters)
        
    if found == True:
        print("Menu:")
        print("1) Update name.")
        print("2) Update health points.")
        print("3) Update defence points.")
        print("4) Update status.")
        print("5) Don't want to update anything anymore.")
        userMenu = int(input("Using the menu above, select what value you want to update: "))
        while userMenu < 1 or userMenu > 5:
            print("Error, the menu only has 5 options (enter from 1 to 5 only).")
            userMenu = int(input("Try again: "))
            
        if userMenu == 1:
            charaName = str(input("Enter a new character name: "))
            while len(charaName) > 30:
                print("Error, character name can only have a length 30 or lower.")
                charaName = str(input("Try again: "))
            sql = "UPDATE Characters SET Name = %s WHERE CharacterID = %s"
            val = charaName, userInputID
            mycursor.execute(sql, val)
            mydb.commit()
            print("Record updated successfully.")
            characters[position].name = charaName

        elif userMenu == 2:
            healthPoints = int(input("Enter new character health points (between 1 and 128): "))
            while healthPoints > 128 or healthPoints < 1:
                print("Error, a character's health points must be between 1 and 128.")
                healthPoints = int(input("Try again: "))
            sql = "UPDATE Characters SET healthPoints = %s WHERE CharacterID = %s"
            val = healthPoints, userInputID
            mycursor.execute(sql, val)
            mydb.commit()
            print("Record updated successfully.")
            characters[position].HP = healthPoints 

        elif userMenu == 3:
            defencePoints = int(input("Enter new character defence points (between 25 and 75): "))
            while defencePoints > 75 or defencePoints < 25:
                print("Error, a character's defence points must be between 25 and 75.")
                defencePoints = int(input("Try again: "))
            sql = "UPDATE Characters SET defencePoints = %s WHERE CharacterID = %s"
            val = defencePoints, userInputID
            mycursor.execute(sql, val)
            mydb.commit()
            print("Record updated successfully.")
            characters[position].DF = defencePoints

        elif userMenu == 4:
            charaStatus = str(input("Enter a new character status, either Neutral(n), Friendly(f) or Hostile(h): "))
            while charaStatus != "n" and charaStatus != "f" and charaStatus != "h":
                print("Error, you can only enter n, f or h.")
                charaStatus = str(input("Try again: "))
            if charaStatus == "n":
                charaStatus = "Neutral"
            elif charaStatus == "f":
                charaStatus = "Friendly"
            else:
                charaStatus = "Hostile"
            sql = "UPDATE Characters SET Status = %s WHERE CharacterID = %s"
            val = charaStatus, userInputID
            mycursor.execute(sql, val)
            mydb.commit()
            print("Record updated successfully.")
            characters[position].status = charaStatus
            
        else:
            print("Record updating was stopped.")
        
    else:
        print("The Character ID entered does not exist.")      
    return characters


def deleteFromTable(characters):
    if len(characters) > 1:
        print("Record deletion selected.")
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "stuartG",
        password = "340HAj5m?",
        database = "CharacterData"
        )
        mycursor = mydb.cursor()
    
        found, position, userInputID = selectID(mycursor, characters)
        print (found, userInputID)
        if found == True:
            characters.pop(position)
            sql = "DELETE FROM Characters WHERE CharacterID = %s"
            val = (userInputID,)
            mycursor.execute(sql, val) 
            mydb.commit()
            print("Record deleted successfully.")
        else:
            print("The Character ID entered does not exist.")     
    else:
        print("Record deletion denied as there is only 1 record left in the database.")
    return characters


# Main Program

import random

import datetime
    
import mysql.connector


characters = createArrayOfRecords() # Creates and populates the array of records and inserts all information into it


userChoice = userChooseHPorDF() # User enters whether they want to use the HP or DF data for the insertion sort and binary search


insertionSort(characters, userChoice) # The array of records is sorted, using the user's earlier choice, (of either HP or DF)
                                    # into ascending order using an insertion sort and then displays the sorted array to the user
                                    
selectedInfo = selectInformation(characters, userChoice) # The program inserts all of the data of the user's earlier choice (of either HP or DF)
                                                        # into an array and then displays the array to the user 

position, comparisons = binarySearch(selectedInfo) # The user selects what value (from the displayed array) that the binary search is to search for


saveResults(position, selectedInfo, comparisons) # The results of the binary search (this includes whether value was or wasn't found,
                            # position value was found in the sorted array of records and the number of comparisons) are written to an external text file

createDatabase() # Connection to mysql server is initialised and a database is created


createTable() # A table is created within the new database using the MySQL connection


insertAllIntoTable(characters) # All information within the array of records is inserted and stored within the table using the MySQL connection


menu(characters, userChoice) # The user is given 4 options and can select to either display the entire table,
                # add a new record to the table, delete a record from the table or end the program, unless the user chooses to end the program the menu
                # procedure is repeated again using recursion

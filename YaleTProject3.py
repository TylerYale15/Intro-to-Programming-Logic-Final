#This program takes information about grades and study hours from two files and displays it while also allowing it to be validated
#By Tyler Yale
#Last modified 12/3/2019

#Define main function
def Main():
    #Set run again to true
    RunAgain = bool(True)
    #Start while loop
    while RunAgain == bool(True):
        #Run menu function and set to choice
        Choice = Menu()
        #Check if choice is a
        if Choice == "a" or Choice == "A":
            print("")
            #Call GetStudyHours
            GetStudyHours()
        #Check if choice is b
        elif Choice == "b" or Choice == "B":
            print("")
            #Call GetGrade
            GetGrade()
        #Check if choice is c
        elif Choice == "c" or Choice == "C":
            #Call GetAverages
            RunAgain = GetAverages()

#Define GetStudyHours function
def GetStudyHours():
    #Init variables
    DataList = []
    CREDITSFORONECLASS = 3
    #Open file
    StudyHoursFile = open("StudyHours.txt", "r")
    
    #Read first line and set to NameLine
    NameLine = StudyHoursFile.readline()
    #Strip the new line from NameLine
    NameLine = NameLine.rstrip()

    #Start while loop for file
    while NameLine != '':
        Name = ProperCase(NameLine)
        #Read next line and set to CreditNum
        CreditNum = StudyHoursFile.readline()
        #Validate Credit num is a digit
        try:
            CreditNum = int(CreditNum)
        except:
            CreditNum = int(input("Invalid data! Please enter a valid number for " + Name + ": "))
            print("")
            
        #Validate CreditNum
        while CreditNum % 3 != 0 or CreditNum < 3 or CreditNum > 18:
            CreditNum = int(input("Please enter a number of credits that is divisible by 3 and in between 3 and 18 for " + Name + ": "))
            print("")
            
        #Read next line and assign to DesiredGrade
        DesiredGrade = StudyHoursFile.readline()
        DesiredGrade = DesiredGrade.rstrip()
        DesiredGrade = DesiredGrade.upper()
        #Validate DesiredGrade
        while DesiredGrade != "A" and DesiredGrade != "a" and DesiredGrade != "B" and DesiredGrade != "b" and DesiredGrade != "C" and DesiredGrade != "c" and DesiredGrade != "D" and DesiredGrade != "d" and DesiredGrade != "F" and DesiredGrade != "f":
            DesiredGrade = input("Please enter a valid grade for " + Name + ": ").upper()
            print("")
        #Call DetermineStudyHours and set to StudyHoursPerWeek
        StudyHoursPerWeek = DetermineStudyHours(DesiredGrade)

        #Calculate StudyHours
        StudyHours = CreditNum / CREDITSFORONECLASS * StudyHoursPerWeek
        
        DataList.append([Name, CreditNum, StudyHours, DesiredGrade])

        print("Student Name:", Name)
        print("Credits:", CreditNum)
        print("Desired Grade:", DesiredGrade)
        print("Study Hours Required:", StudyHours)
        print("")
        
        #Read next line 
        NameLine = StudyHoursFile.readline()
        NameLine = NameLine.rstrip()

    #Close file

    StoreData(DataList)
    
    StudyHoursFile.close()

#Define Store Data
def StoreData(Data):

    #Sort the elements in data list 
    Data.sort()

    #Open the HowManyHours file
    HowManyHoursFile = open("HowManyHours.txt", "a")

    #Create for loop that will iterate through data list 
    for index in Data:

        #Set line to each index of the nested list
        line = '{}\n{}\n{}\n{}\n'.format(index[0], index[1], index[2], index[3])
        #Write to the file
        HowManyHoursFile.write(line)
    line.strip('\n') 

    #Close the file
    HowManyHoursFile.close()

#Define ProperCase
def ProperCase(Name):
    #Init lists and variables
    ProperCaseName = []
    FullName = ''

    #Split Name into a list seperating by a space
    NameList = Name.split(' ')

    #Create for loop that will iterate through list 
    for word in NameList:
    #Sets the first index of each element to a capital
        word = word[0].upper() + word[1:].lower()
        #Appends word to the ProperCaseName list
        ProperCaseName.append(word)

    #Create for loop that iterates through ProperCaseName
    for element in ProperCaseName:
        #Convert each element of list to a string
        FullName += str(element) + ' '

    #Return name
    return FullName

#Define GetGrade
def GetGrade():
    DataList = []
    #Init variables
    CREDITSFORONECLASS = 3
    #Open file
    GradesFile = open("Grades.txt", "r")
    #Read first line and set to NameLine
    NameLine = GradesFile.readline()
    NameLine = NameLine.rstrip()

    #Start while loop for file
    while NameLine != '':
        Name = ProperCase(NameLine)
        #Read next line and set to CreditNum
        CreditNum = GradesFile.readline()

        CreditNum = int(CreditNum)
        #Validate CreditNum
        while CreditNum % 3 != 0 or CreditNum < 3 or CreditNum > 18:
            CreditNum = int(input("Please enter a number of credits that is divisible by 3 and in between 3 and 18 for " + Name + ": "))
            print("")
        #Read next line and set to StudyHours
        StudyHours = GradesFile.readline()
        #Validate that study hours is a number
        try:
            StudyHours = int(StudyHours)
        except:
            StudyHours = int(input("Invalid data! Please enter a valid number for " + Name + ": "))
            print("")
        #Validate StudyHours
        while StudyHours > 90 or StudyHours < 0:
            StudyHours = int(input("Please enter a valid number of study hours between 0 and 90 for " + Name + ": "))
            print("")
        #Calculate StudyHoursPerWeek
        StudyHoursPerWeek = StudyHours * CREDITSFORONECLASS / CreditNum
        #Call DetermineGrade function and set to Grade
        Grade = DetermineGrade(StudyHoursPerWeek)

        DataList.append([Name, CreditNum, StudyHours, Grade])
        
        #Display information
        print("Student Name:", Name)
        print("Credits:", CreditNum)
        print("Total Study Hours:", StudyHours)
        print("Desired Grade:", Grade)
        print("")
        #Read next line
        NameLine = GradesFile.readline()
        NameLine = NameLine.rstrip()

    #Close file

    StoreData(DataList)
    
    GradesFile.close()

#Define GetAverages
def GetAverages():
    #Init variables
    CREDITSFORONECLASS = 3
    TotalStudents = 0
    TotalCredits = 0
    TotalStudyHours = 0
    #Open file
    HowManyHoursFile = open("HowManyHours.txt", "r")
    #Read first line and set to NameLine
    NameLine = HowManyHoursFile.readline()
    #Start while loop for file
    while NameLine != '':
        #Read next line and set to CreditNum
        CreditNum = HowManyHoursFile.readline()
        CreditNum = int(CreditNum)

        StudyHours = HowManyHoursFile.readline()
        StudyHours = StudyHours.rstrip()
        StudyHours = float(StudyHours)
        #Read next line and set to DesiredGrade
        Grade = HowManyHoursFile.readline()
        Grade = Grade.rstrip()
        #Accumulate
        TotalStudents += 1
        TotalCredits += CreditNum
        TotalStudyHours += StudyHours
        #Read next line
        NameLine = HowManyHoursFile.readline()
    #Close first file
    HowManyHoursFile.close()

    #Calculate Averages and display information
    try:
        AverageCredits = TotalCredits / TotalStudents
        AverageStudyHours = TotalStudyHours / TotalStudents
        RunAgain = bool(False)
        print("")
        print("Total Students:", TotalStudents)
        print("Average Credits:", format(AverageCredits, ".2f"))
        print("Average Study Hours:", format(AverageStudyHours, ".2f"))
        print("")
        #Thank the user
        print("Thank you for using this program")
        print("")
    except:
        ZeroDivisionError()
        RunAgain = bool(True)
        print("")
        print("There are no entries in the file, please use option A or B first!")
        print("")
    return RunAgain

#Define DetermineStudyHours        
def DetermineStudyHours(Grade):
    #Init variables
    StudyHours = 0

    #Determine what grade is equal to and set StudyHours equal to either 15, 12, 9, 6, or 0
    if Grade == "A":
        StudyHours = 15
    elif Grade == "B":
        StudyHours = 12
    elif Grade == "C":
        StudyHours = 9
    elif Grade == "D":
        StudyHours = 6
    elif Grade == "F":
        StudyHours = 0

    #Return StudyHours
    return StudyHours

#Define DetermineGrade
def DetermineGrade(StudyHours):
    #Init variables
    Grade = ""

    #Determine StudyHours and then determine Grade
    if StudyHours >= 15:
        Grade = "A"
    elif StudyHours >= 12:
        Grade = "B"
    elif StudyHours >= 9:
        Grade = "C"
    elif StudyHours >= 6:
        Grade = "D"
    elif StudyHours >= 0:
        Grade = "F"

    #Return Grade
    return Grade

#Define Menu
def Menu():
    #Display Welcome
    print("Welcome to the grade determining software")
    print("Choose option 'A' to determine hours to study")
    print("Choose option 'B' to determine grade")
    print("Choose option 'C' to quit the program")
    print("")

    #Get user input
    Choice = input("Please enter a choice: ")

    #Validate input
    while Choice != "a" and Choice != "A" and Choice != "b" and Choice != "B" and Choice != "c" and Choice != "C":
        Choice = input("Please enter a valid choice: ")

    #Return Choice
    return Choice

#Call Main function
Main()

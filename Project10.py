#---------------------
# Summer Davis
# COSC 1336
# Project 10
#---------------------
# Objective: compute a patient's bill for a hospital stay.
#
# Program Components:
# - PatientAccount class to keep track of patient charges & days spent in the hospital
# --> roomBill, surgeryBill, medBill, daysSpent
# - A surgery method will have the charges for at least five types of surgery and
#   will update the surgeryBill member variable.
# - A data file will contain at least five types of surgery and its cost. Both type and
#   cost will be separated by commas.
# - A pharmacy method will have the charges for at least five types of medication and
#   will update the medBill member variable.
# - A data file will contain at least five types of medication and its cost. Both type
#   and cost will be separated by commas.
# - The dayCharge method will update the daysSpent member variable.
# - The setName method will assign the name of the patient
# - Each day in the hopsital costs $1,000
# - A menu that allows the user to enter type of surgery, medication, number of days
#   in the hospital, and check the patient out of the hospital.
#
# Program will:
# - Display header
# - Ask user if they are ready to enter patient information
# - Ask user to enter name of patient
# - display menu (L - length of stay, S - surgery, P - pharmacy, X - exit)
# - once user is finished making selections and chooses 'X',
# - generate invoice using displayResult()
# - display footer
#---------------------

# Classes
class PatientAccount:

    def __init__(self):
        print('\n')
        print('-' * 70)
        print('Hospital Patient Check-out')
        print('_' * 80)
        print('\n')
        self.name = ''
        self.roomBill = 0
        self.daysSpent = 0
        self.surgeryBill = 0
        self.medBill = 0
        self.totalDue = self.getTotalDue()

    def setName(self, value):
        self.name = value

    def setRoomBill(self, value):
        self.roomBill = value

    def setSurgeryBill(self, value):
        self.surgeryBill = value

    def setMedBill(self, value):
        self.medBill = value

    def setTotalDue(self, value):
        self.totalDue = value

    def getName(self):
        return self.name

    def getRoomBill(self):
        return self.roomBill

    def getSurgeryBill(self):
        return self.surgeryBill

    def getMedBill(self):
        return self.medBill

    def getTotalDue(self):
        return self.roomBill + self.surgeryBill + self.medBill

    def dayCharge(self, days):
        self.daysSpent += days

    def addRoomBill(self, days):
        print(f'Adding {days} days (at $1,000/day to patient bill)')
        charge = 1000 * days
        self.roomBill += charge
        self.dayCharge(days)
        print(f'Total amount for Hospital Stay: ${self.roomBill}')

    def addSurgeryBill(self, choice):
        print(f'Adding {choice} to patient bill.')
        charge = int(choice[1])
        self.surgeryBill += charge
        print(f'Surgery Bill: ${charge}')

    def addMedBill(self, choice):
        print(f'Adding {choice} to patient bill.')
        charge = int(choice[1])
        self.medBill += charge
        print(f'Medicine Bill: ${charge}')
        
    
    
# Collect and organize all of the program tasks
def main():
    
    # Display header
    header()

    # Prepare data files
    surgeryFile = 'surgery.txt'
    pharmaFile = 'pharmacy.txt'

    # Prepare data dictionaries
    surgeryList = readMedData(surgeryFile)
    pharmaList = readMedData(pharmaFile)


    # Check if user would like to enter patient information
    enterInfo = getStringData('Are you ready to enter Patient Information? (Y/N) ', ['Y', 'N'])
    
    # While enterInfo is Y, 
    while (enterInfo == 'Y'):
            
            # Log patient information
            patientAccount = PatientAccount()
            patientAccount.setName(getStringName('Name of Patient: '))

            # While menu choices are being made
            while (True):

                # Generate Check-out menu
                checkoutChoice = checkoutMenu()

                # Length of Stay
                if (checkoutChoice == 'L'):
                    days = getIntegerData('Enter the length of stay: ')
                    patientAccount.addRoomBill(days)

                # Surgery Menu
                elif (checkoutChoice == 'S'):
                    surgeryChoice = surgeryMenu(surgeryList)
                    patientAccount.addSurgeryBill(surgeryChoice)

                # Pharmacy Menu
                elif (checkoutChoice == 'P'):
                    pharmaChoice = pharmaMenu(pharmaList)
                    patientAccount.addMedBill(pharmaChoice)

                # Exit program
                else:
                    displayResult(patientAccount)
                    break


            # Ask if user would like to enter info for another patient
            enterInfo = getStringData('Do you like to process another Patient? (Y/N) ', ['Y', 'N'])
    
    # Once user selects 'N', display footer
    footer()


# Generate invoice
def displayResult(patientAccount):
    name = patientAccount.getName()
    total = patientAccount.getTotalDue()

    print('\n')
    print('-' * 50)
    print('Summary: Patient Bill')
    print('-' * 50)
    print(f'Name: {name}')
    print(f'Total Bill: owes: ${total:,.02f}')
    print('-' * 50)
    print('\n')
    

# Generate Pharmacy Menu
def pharmaMenu(pharmaList):
    print('-' * 50)
    print('Pharmacy Menu')
    print('-' * 50)
    
    count = 1
    for item in pharmaList:
        print(f'{count}\t{item}')
        count += 1
    
    print('-' * 70)
    print('\n')

    choice = validateSelection('Enter a medicine: ', count)
    return pharmaList[choice-1]


# Generate Surgery Menu
def surgeryMenu(surgeryList):
    print('-' * 50)
    print('Surgery Menu')
    print('-' * 50)
    
    count = 1
    for item in surgeryList:
        print(f'{count}\t{item}')
        count += 1
    
    print('-' * 70)
    print('\n')

    choice = validateSelection('Enter a surgery: ', count)
    return surgeryList[choice-1]


# Generate Check-Out Menu
def checkoutMenu():
    menu = {'L':'enter length of stay', 'S':'enter surgery menu',
            'P':'enter pharmacy menu', 'X':'exit program and view bill summary'}
    print('\n')
    print('-' * 70)
    print('Hospital Patient Check-out')
    print('-' * 70)

    for item in menu:
        print(f'{item} ..... {menu[item]}')

    print('-' * 70)
    print('\n')

    choice = getStringData('Enter your selection: ', ['L', 'S', 'P', 'X'])
    return choice
    

# Reads a file based on delimiter
# and returns a dictionary
def readMedData(fileName):
    medList = []
    
    try:
        dataFile = open(fileName, 'r')

        for line in dataFile:
            newLine = line.strip('\n')

            if (len(newLine) > 0):
                
                try:
                    tempList = newLine.split(',')
                    medList.append(tempList)
                    
                except ValueError:
                    continue

        dataFile.close()
        return medList

    except FileNotFoundError:
        print(f'\n\tError: File not found.\n')

# Get users entry of non-empty string
def getStringName(prompt):
    while (True):
        value = input(prompt)
        if (len(value) > 0):
            return value
        else:
            print(f'\n\tError: nothing entered.')

# Get users entry of string data commands
def getStringData(prompt, cmdList):
    while (True):
        value = input(prompt)
        value = value.upper()

        if (value in cmdList):
            return value
        else:
            print(f'\n\tError: Invalid selection. {cmdList} only.\n')

        
# Get users entry of ONLY positive float data
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))

            if (value >= 0):
                return value
            else:
                print(f'\n\tError: Negative entry.')

        except ValueError: 
            print(f'\n\tError: Non Numbers entered.\n')

# Get users entry of ONLY positive integer data
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))

            if (value >= 0):
                return value
            else:
                print(f'\n\tError: Negative entry.')

        except ValueError:
            print(f'\n\tError: Non Integers entered.\n')


# Get users entry of ONLY integer data within the menu range
def validateSelection(prompt, count):
    while (True):
        try:
            value = int(input(prompt))

            if (value in range(1, count)):
                return value
            else:
                print(f'\n\tError: Select 1-{count-1}.\n')
        

        except ValueError: 
            print(f'\n\tError: Non Integers entered.\n')

# Display the start of the project
def header ():
    print('\n')
    print('Project 10: Patient Fees')
    print('Written by: Summer Davis')
    print('\n')
    print('This program computes the total charges for a hospital stay. Users can select' + \
          f'\nmedicines and surgeries and days spent in the hospital.')
    print('-' * 70)
    print('Welcome to AllyBaba Patient Management System')
    print('-' * 70)
    print('\n')
    
# Display the end of the project
def footer():
    print('\n')
    print('-' * 60)
    print('End of Project 10')

# Call the main function  
main()

import pandas;
import matplotlib.pyplot as plt;
import csv;
import tkinter as tk
import numpy

Customer_Data = pandas.read_csv("OSHack_BankCustomers.csv")

def showAge():
    ageLoanCount = {"Young":0, "Adults": 0, "Old Adults": 0}
    Age_Loan = Customer_Data.loc[:,"age"]

    for i in Age_Loan:
        if i <= 30:
            ageLoanCount["Young"] += 1
        elif i > 30 and i < 60:
            ageLoanCount["Adults"] += 1
        else:
            ageLoanCount["Old Adults"] += 1

    pie = numpy.array(list(ageLoanCount.values()))
    AgeLabels = ["Young(15-30)", "Adults(30-60)", "Old Adults(60-90)"]
    plt.pie(pie, labels = AgeLabels)
    plt.legend(title = "Age Groups:")
    plt.show()
    
def showJob():
    jobCount = {}
    jobs = Customer_Data.loc[:,"job"]
    for i in jobs:
        if i in jobCount:
            jobCount[i] += 1
        else:
            jobCount[i] = 1

    jobList = list(jobCount.keys())
    CountList = list(jobCount.values())
    plt.bar(jobList, CountList, color ='maroon', width = 0.4)
    plt.show()

def showMartialStatus():
    martialStatus = {"Married":0, "Unmarried":0}
    marital = Customer_Data.loc[:,"marital"]

    for i in marital:
        if i == "married":
            martialStatus["Married"] += 1
        else:
            martialStatus["Unmarried"] += 1

    pie = numpy.array(list(martialStatus.values()))
    martialLabels = ["Married", "Unmarried"]
    plt.pie(pie, labels = martialLabels)
    plt.legend(title = "Martial Status:")
    plt.show()

def showEducation():
    educationCount = {}
    education = Customer_Data.loc[:,"education"]
    for i in education:
        if i in educationCount:
            educationCount[i] += 1
        else:
            educationCount[i] = 1

    pie = numpy.array(list(educationCount.values()))
    EducationLabels = list(educationCount.keys())
    plt.pie(pie, labels = EducationLabels)
    plt.legend(title = "Education Level:")
    plt.show()

def showdefault():
    defaultCount = {}
    default = Customer_Data.loc[:,"default"]
    for i in default:
        if i in defaultCount:
            defaultCount[i] += 1
        else:
            defaultCount[i] = 1

    defaultLabels = list(defaultCount.keys())
    pie = numpy.array(list(defaultCount.values()))
    plt.pie(pie, labels = defaultLabels)
    plt.legend(title = "Default:")
    plt.show()

def showBalance():
    balanceCount = {"Debt":0, "Not in Debt": 0}
    balance = Customer_Data.loc[:,"balance"]
    for i in balance:
        if i < 0:
            balanceCount["Debt"] += 1
        else:
            balanceCount["Not in Debt"] += 1
    
    balanceLabels = list(balanceCount.keys())
    pie = numpy.array(list(balanceCount.values()))
    plt.pie(pie, labels = balanceLabels)
    plt.legend(title = "Balance:")
    plt.show()

def showHousing():
    housingCount = {"Yes":0, "No": 0}
    housing = Customer_Data.loc[:,"housing"]
    for i in housing:
        if i == "yes":
            housingCount["Yes"] += 1
        else:
            housingCount["No"] += 1
    
    housingLabels = list(housingCount.keys())
    pie = numpy.array(list(housingCount.values()))
    plt.pie(pie, labels = housingLabels)
    plt.legend(title = "Housing:")
    plt.show()

def showLoan():
    loanCount = {"Yes":0, "No":0}
    loan = Customer_Data.loc[:,"loan"]
    for i in loan:
        if i == "yes":
            loanCount["Yes"] += 1
        else:
            loanCount["No"] += 1

    pie = numpy.array(list(loanCount.values()))
    loanLabels = list(loanCount.keys())
    plt.pie(pie, labels = loanLabels)
    plt.legend(title = "Loan Level:")
    plt.show()

def showContact():
    contactCount = {}
    contact = Customer_Data.loc[:,"contact"]
    for i in contact:
        if i in contactCount:
            contactCount[i] += 1
        else:
            contactCount[i] = 1

    contactLabels = list(contactCount.keys())
    pie = numpy.array(list(contactCount.values()))
    plt.pie(pie, labels = contactLabels)
    plt.legend(title = "Contact:")
    plt.show()

def showDay():
    dayCount = {}
    day = Customer_Data.loc[:,"day"]
    for i in day:
        if i in dayCount:
            dayCount[i] += 1
        else:
            dayCount[i] = 1

    x = numpy.array(sorted(list(dayCount.keys()))) 
    y = numpy.array(list(dayCount.values()))
    
    plt.plot(x, y) 
    plt.xlabel("Days") 
    plt.ylabel("Count")
    plt.show()

def showMonth():
    monthCount = {}
    month = Customer_Data.loc[:,"month"]
    for i in month:
        if i in monthCount:
            monthCount[i] += 1
        else:
            monthCount[i] = 1

    x = numpy.array(list(monthCount.keys()))
    y = numpy.array(list(monthCount.values()))
    
    plt.plot(x, y) 
    plt.xlabel("Months") 
    plt.ylabel("Count")
    plt.show()

def showOperatingSystem():
    OperatingSystemCount = {}
    OperatingSystem = Customer_Data.loc[:,"OperatingSystems"]
    for i in OperatingSystem:
        if i in OperatingSystemCount:
            OperatingSystemCount[i] += 1
        else:
            OperatingSystemCount[i] = 1

    pie = numpy.array(list(OperatingSystemCount.values()))
    OperatingSystemLabels = list(OperatingSystemCount.keys())
    plt.pie(pie, labels = OperatingSystemLabels)
    plt.legend(title = "OperatingSystem Status:")
    plt.show()

while(True):
    print("*********Welcome to Customer Data Analysis Sysytem*********")
    choice = input(('''1. Show Age
2. Show Job
3. Show Marital Status
4. Show education
5. Show Default
6. Show Balance
7. Show Housing
8. Show Loan
9. Show Contact
10. Show Day
11. Show Month
12. Show Operating System
13. Exit
Please enter your choice: '''))
    
    if choice == "1" or choice.lower == "age":
        showAge()
    elif choice == "2" or choice.lower == "job":
        showJob()
    elif choice == "3" or choice.lower == "marital status":
        showMartialStatus()
    elif choice == "4" or choice.lower == "education":
        showEducation()
    elif choice == "5" or choice.lower == "default":
        showdefault()
    elif choice == "6" or choice.lower == "balance":
        showBalance()
    elif choice == "7" or choice.lower == "housing":
        showHousing()
    elif choice == "8"or choice.lower == "loan":
        showLoan()
    elif choice == "9"or choice.lower == "Contact":
        showContact()
    elif choice == "10"or choice.lower == "day":
        showDay()
    elif choice == "11"or choice.lower == "month":
        showMonth()
    elif choice == "12"or choice.lower == "weekend":
        showOperatingSystem()
    elif choice == "13" or choice.lower == "exit":
        break
    else:
        print("Invalid Choice.")

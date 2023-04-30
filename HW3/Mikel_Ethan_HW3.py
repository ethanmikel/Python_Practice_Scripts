#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:43:13 2023

@author: ethanmikel
"""

#Author: Ethan Mikel
#Homework Number & Name: 3 Retirement Account
#Due Date: Feb. 14 by 12pm
#Program Description: This program prompts users to input their annual savings, the year they want to start saving, the year they want to stop saving (must be greater than start year), the year they want to retire (must be greater than the year they stop saving), and the interest rate. For  the years the user inputs they must be inbetween 2020-2100 and the interest rate must be between 1 to 15%; if the user fails to do this it will contuine to ask the user till they enter a correct value. Once the program gets all of the correct inputted data it will then print the, the amount the user wants to save for that year, the amount of interest they earned for that year, and the total amount of their savings until they retire.  
    
#Sets the variables: interest_earned, total_savings, addtional_savings to 0, so they can be used in the program later on.
interest_earned=0
total_savings=0
additional_savings=0

#Asks the user the amount of savings they want to save for every year. Will contuine to ask the user until they give a postive savings amount. 
annual_savings=float(input("\nWhat is your annual savings amount? $"))
while annual_savings < 0: 
    print("\nPlease enter a postive number.")
    annual_savings=float(input("What is your annual savings amount? $"))
    
#Asks the user the year they want to start saving. Will contuine to ask the user for their start year until they enter a year that is inbetween 2020-2100.
start_year=int(input("\nWhat year do you want to start saving? "))
while start_year < 2020 or start_year > 2100:
    print("\nPlease enter a valid start saving year between 2020 - 2100. ")
    start_year=int(input("What year do you want to start saving? "))
    
#Asks the user the year they want to stop saving. Will contuine to ask the user for their end year until they enter a year that is inbetween 2020-2100 and is greater than or equal to their start year.
end_year=int(input("\nWhat year do you want to end saving? "))
while end_year < 2020 or end_year > 2100 or end_year < start_year:
    print("\nPlease enter a valid end savings year between 2020 - 2100 and is larger than the start year.")
    end_year=int(input("What year do you want to stop saving? "))

#Asks the user the year they want to retire saving. Will contuine to ask the user for their retirement year until they enter a year that is inbetween 2020-2100 and is greater than or equal to their end year.
retire_year=int(input("\nWhat year do you want to retire? "))
while retire_year < 2020 or retire_year > 2100 or retire_year < end_year:
    print("\nPlease enter a retirement year between 2020 - 2100 and is larger than the end year.")
    retire_year=int(input("What year do you want to retire? "))

#Asks the user for the interest rate. Will contuine to ask the user for the interest rate until they give a value that is from 1-15%. 
interest_rate=float(input("\nWhat is the interest rate? "))
while interest_rate < 1 or interest_rate > 15:
    print("\nPlease enter a valid interest rate (1 - 15%). ")
    interest_rate=float(input("What is the interest rate? "))

#Prints the header for the users projected data per year 
print("\nYear \t\tSavings \t\t Interest\t\t\t Total")
print("--------------------------------------------------------------")

#This loop calculates the amount the user wants to save every year by seeing if the current year is less than or equal to year they want to stop saving. This loop also calculates the interest earned per year and the total savings per year. This loop then prints out the forcasted (current) year, the savings for that year, the interest earned for that year, and the current total for that year.
for current_year in range(start_year, retire_year+1, 1):
    if current_year <= end_year:
        additional_savings=annual_savings
    elif current_year > end_year:
        additional_savings=0
    interest_earned=(total_savings+additional_savings)*interest_rate/100
    total_savings=total_savings+additional_savings+interest_earned
    print(str(current_year) + " \t" + format(additional_savings,'12,.0f') + "\t " + format(interest_earned, '12,.0f') + "\t\t " + format(total_savings, '12,.0f'))
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:05:37 2023

@author: ethanmikel
"""
#Author: Ethan Mikel
#Homework Number & Name: 5 Gradebook
#Due Date: March 6 by 7PM
#Program Description: This program is designed to allow the user to input a student and their grade, then once the user has inputed all of the grades write both the names and grades in .txt file

#Imports the path to allow us to be able to write the names and grades in the .txt file 
import os
os.chdir(path)

#Main calls both the user_name and average_value function to then be able to allow the user to enter the a student's name and their grade to be written in a .txt file. It also prompts the user if they are wanting multiple student entrires and tell them how many students they have entered in data for.
def main():
    repeat='Y'
    count=0
    while repeat=='Y' or repeat=='y':
        name = user_name()
        numeric_average=average_value()
        repeat=input("Would you like to enter another student (Y for Yes and N for No)? ")
        student_data = open('gradebook.txt', 'a') 
        student_data.write(name+"\n"+str(numeric_average)+"\n")
        count+=1
    print("Total Number of Students Inputed:", count)
    
#This function imports the functions python script to validate that the user has inputed enough characters as a name, then returns the student's name. 
def user_name():
    import Mikel_Ethan_HW5_Functions 
    while True:
        name = input("What is the name of the student? ")
        if Mikel_Ethan_HW5_Functions.user_name_validation(name):
            break
        else: 
            continue
    return name

#This function validates the users input for the student's numeric grade. It does this by calling a function python script to ensure that the user input is between 0 and 100, it also makes sure the user did not input nothing or str. 
def average_value():
    import Mikel_Ethan_HW5_Functions 
    while True:
        try: 
            numeric_average = float(input("What is the numeric average? "))
            if not Mikel_Ethan_HW5_Functions.numeric_average_validation(numeric_average):
                break
            else: 
                continue
        except ValueError:
             print ("Numeric Average cannot be left blank, be a special character, or be a letter.")    
    return numeric_average

#Calls main function
main()


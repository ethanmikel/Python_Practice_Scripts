#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:26:36 2023

@author: ethanmikel
"""

#Author: Ethan Mikel
#Homework Number & Name: 5 Gradebook
#Due Date: March 6 by 7PM
#Program Description: Program is designed for a user to input in a student's name to then be able to update their grade that is associated with their name. It then makes a temporary file to then be able to rewrite the gradebook.txt file to correspond to then the new grade.
    

#Imports the path to allow us to be able to write the names and grades in the .txt file 
import os
os.chdir(path)

#Main method calls the functions student_search, new_average, and grade_update to then be able to update gradebook.txt with the updated numeric average. It does this by changing the name of a temp file to gradebook.txt and deleting the previous gradebook.txt file. Also if no student was found, this method returns that the student was not found.
def main():  
    line_number=student_search()
    if line_number != 0: 
        numeric_average=new_average()
        grade_update(numeric_average, line_number)
        os.remove('gradebook.txt')
        os.rename('temp.txt', 'gradebook.txt')
    else :
        print("The student was not found.")

#This function asks the user to input a student name it also validates that the user inputed enough characters by calling the function script, once it has the students name. It then goes through the entire gradebook.txt file to then find the line number to be able add one additional line to then find the line number that is assocated with the inputed student's grade.
def student_search():
    line_count=0
    line_number=0
    import Mikel_Ethan_HW5_Functions 
    student_data = open('gradebook.txt', 'r') 
    while True:
        student_name=input("What is the name of the student? ")
        if Mikel_Ethan_HW5_Functions.user_name_validation(student_name):
            break
        else: 
            continue
    student = student_data.readline().rstrip("\n")
    while student != '':
        if student == student_name:
            line_number=line_count+1
        else: 
            line_count+=1
        student = student_data.readline().rstrip("\n")
    student_data.close()
    return line_number

#This function validates the users input for the student's numeric grade. It does this by calling a function python script to ensure that the user input is between 0 and 100, it also makes sure the user did not input nothing or str. 
def new_average():
    import Mikel_Ethan_HW5_Functions 
    while True:
        try: 
            numeric_average = float(input("What is new the numeric average? "))
            if not Mikel_Ethan_HW5_Functions.numeric_average_validation(numeric_average):
                break
            else: 
                continue
        except ValueError:
             print ("Numeric Average cannot be left blank, be a special character, or be a letter.")    
    return numeric_average

#Function takes the line_number and new numeric_average retruned in the other functions to then update the students grade to the new desired value. It does this by writing all of the other lines in gradebook.txt in a temp file then when it reaches the desired line number changes the grade to the new grade. 
def grade_update(numeric_average, line_number):
    count=0
    student_data = open('gradebook.txt', 'r') 
    temp_data = open('temp.txt', 'w')
    student = student_data.readline().rstrip("\n")
    while student != "":
        if  count==line_number:
            temp_data.write(str(numeric_average)+"\n")
            student = student_data.readline().rstrip("\n")
        temp_data.write(str(student)+"\n")
        student = student_data.readline().rstrip("\n")
        count+=1
    temp_data.close()
    student_data.close()
    
#Calls main function
main()

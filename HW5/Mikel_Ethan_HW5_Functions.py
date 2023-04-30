#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:53:46 2023

@author: ethanmikel
"""
#Author: Ethan Mikel
#Homework Number & Name: 5 Gradebook
#Due Date: March 6 by 7PM
#Program Description: Validates that the user enter the correct amount of characters for the student name and that their numeric average is between 0 and 100.

#Function returns True if the students name the user inputed is greater than or equal to a length of 2, if it isn't prints out a warning and retruns False. 
def user_name_validation(name):
    if len(name)>=2:
        return True
    else:
        print("Name must be at least two characters.")
        return False
    
#Function retruns true if the user inputs a value that is lower than 0 or greater than 100, if the user does input a value between 0 and 100 then it returns False. 
def numeric_average_validation(numeric_average):
    if numeric_average < 0 or numeric_average > 100:
        print("Numeric Average must be a value between 0 and 100.")
        return True
    else: 
        return False
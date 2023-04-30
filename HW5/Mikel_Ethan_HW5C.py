#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:26:47 2023

@author: ethanmikel
"""
#Author: Ethan Mikel
#Homework Number & Name: 5 Gradebook
#Due Date: March 6 by 7PM
#Program Description: Designed to traverse the gradebook.txt file and print out every student name and grade, then find the max and min grade in the file to output them. 

#Imports the path to allow us to be able to write the names and grades in the .txt file 
import os
os.chdir(path)

#Main function outputs every students name and their assocaiated grade all on one single line for every student. This function also uses an if loop to be able to see if the current min and max value need to be changed, so that at the end of the program they can be printed. 
def main():
    max_grade=0
    min_grade=101
    gradebook_data = open('gradebook.txt', 'r')    
    gradebook = gradebook_data.readline().rstrip('\n')
    while gradebook != '':  
        print(gradebook+"'s grade is ", end="")
        gradebook = gradebook_data.readline().rstrip('\n')
        gradebook=float(gradebook)
        if gradebook > max_grade:
            max_grade = gradebook
        elif gradebook < min_grade:
            min_grade = gradebook
        print(gradebook)
        gradebook = gradebook_data.readline().rstrip('\n')
    print("The max grade is:",max_grade)
    print("The min grade is:",min_grade)
    
#Calls main function
main()
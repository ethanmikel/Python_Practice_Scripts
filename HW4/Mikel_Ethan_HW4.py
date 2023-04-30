#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 14:07:55 2023

@author: ethanmikel
"""

#Author: Ethan Mikel
#Homework Number & Name: 3 Retirement Account
#Due Date: Feb. 27 by 7pm
#Program Description: Program is designed to allow the user to input a studnets grades then output the student's final numeric and letter grade by using functions. 
    
#Configures the global variables to allow for the precentage of each catergory to be easily changed.
exam1_weight=0.2
exam2_weight=0.2
exam3_weight=0.2
homework_weight=0.2
language_quick_reference_weight=0.1
final_project_weight=0.1

#Main method that calls the functions get_grade, calc_average, and calc_letter to then be able to output the final numeric and letter grade 
def main():
    grade_exam_1=get_grade("Exam 1")
    grade_exam_2=get_grade("Exam 2")
    grade_exam_3=get_grade("Exam 3")
    grade_homework_assignments=get_grade("Homework Assignments")
    grade_language_quick_reference=get_grade("Language Quick Reference")
    grade_final_project=get_grade("Final Project")
    numeric_grade=calc_average(grade_exam_1, grade_exam_2, grade_exam_3, grade_homework_assignments, grade_language_quick_reference, grade_final_project)
    letter_grade=calc_letter(numeric_grade)
    print("Final Numeric Grade:",str(format(numeric_grade, '.2f')))
    print("Final Letter Grade:",letter_grade)

#Prompts the user to enter the grade that coresponds with the assingment they are entering, value must be between 0 and 100 inclusively. 
def get_grade(assignment):
   grade=float(input("What is the grade for "+assignment+": "))
   while grade < 0 or grade > 100:
           print("Grade must be a number between 0 and 100")
           grade=float(input("What is the grade for "+assignment+": "))
   return grade

#Function claculates the students final numeric grade by having the six parameters set in the get_grade function and the global variables. 
def calc_average(grade_exam_1, grade_exam_2, grade_exam_3, grade_homework_assignments, grade_language_quick_reference, grade_final_project):
    final_numeric_grade=(grade_exam_1*exam1_weight)+(grade_exam_2*exam2_weight)+(grade_exam_3*exam3_weight)+(grade_homework_assignments*homework_weight)+(grade_language_quick_reference*language_quick_reference_weight)+(grade_final_project*final_project_weight)
    return final_numeric_grade

#Calculates the letter grade by using the final numeric grade to then assign it to its corresponding letter grade. 
def calc_letter(final_numeric_grade):
    letter_grade=' '
    if final_numeric_grade >= 89.50:
        letter_grade='A'
    elif final_numeric_grade >= 79.50:
        letter_grade='B'
    elif final_numeric_grade >= 69.50:
        letter_grade='C'
    elif final_numeric_grade >= 59.50:
        letter_grade='D'
    else: 
        letter_grade='F'
    return letter_grade

#Calls the main function
main()

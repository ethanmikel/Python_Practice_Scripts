#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:14:39 2023

@author: ethanmikel
"""

#Author: Ethan Mikel
#Homework Number & Name: 7 Return on Investemnt 
#Due Date: April 10 by 11:59 PM
#Program Description: Prompts the user for both the current and inital value to then be able to call the validation and calculation class and the adjacent program to ensure the user has entered a correct input, so that this program can then read out the value for ROI. 
    
import Mikel_Ethan_HW7_Classes

#Sets the address for both classes to then be used in the following methods
validation_class = Mikel_Ethan_HW7_Classes.ValidationClass()
calculation_class = Mikel_Ethan_HW7_Classes.CalculationClass()

#Main function calls get_initial_value, get_current_value, main_ROI to prompt and print out the right information
def main():
    intital_value=get_initial_value()
    current_value=get_current_value()
    main_ROI(intital_value, current_value)

#Prompts the user for a inital value, then validates it with the ValidationClass if intial_value is -1 then it will countine prompting the user until they have entered a correct input. If all validations are met then it returns the intial_value
def get_initial_value():
    inital_value = -1
    while inital_value == -1:
        str_value = input("What is the initial value? ")
        inital_value=validation_class.checkFloat(str_value)
    else: 
        return inital_value
    
#Prompts the user for a inital value, then validates it with the ValidationClass if intial_value is -1 then it will countine prompting the user until they have entered a correct input. If all validations are met then it returns the current_value
def get_current_value():
    current_value = -1
    print('')
    while current_value == -1:
        str_value = input("What is the current value? ")
        current_value=validation_class.checkFloat(str_value)
    else: 
        return current_value
    
#Gives the CalculationClass both the inital_value and current_value to then be able to call get_roi method within the class to print out the users ROI. 
def main_ROI(intital_value, current_value):
    calculation_class.roi_calculation(intital_value, current_value)
    roi_value=calculation_class.get_roi()
    roi_value = roi_value - 0.15
    print("The ROI for this investment is", roi_value)
    
#Calls main function 
main()

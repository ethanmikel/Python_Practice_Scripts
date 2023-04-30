#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:47:23 2023

@author: ethanmikel
"""

#Author: Ethan Mikel
#Homework Number & Name: 7 Return on Investemnt 
#Due Date: April 10 by 11:59 PM
#Program Description: The ValidationClass validates that both the intital and current value inputted by the user are correct meaning they are positive numbers. In the CalculationClass it calculates the return on investment (ROI) for the users spectifc input for initial and current amount.  
    
#ValidationClass ensure the user has inputed a correct value for inital and current input. 
class ValidationClass:
    default_value = -1

    #checkFloat method ensures that the users input for inital and current value is a float and not any type of string, left empty, or a negative value. If it encounters any of these, it returns -1 back to the main class to prompt the user for a new input, so the cycle can repeat. If it validates that it is a positive value it returns the float back to the main program. 
    def checkFloat(default_value, str_value): 
        try:
            default_value = float(str_value)
        except TypeError:
            print()
        except: 
            print("Invalid initial value, please try again!\n")
            default_value = -1
        else:
            if default_value < 0: 
                print("Invalid initial value, please try again!\n")
                default_value = -1
        return default_value
    
    #checkInteger method ensures that the users input for inital and current value is a int and not any type of string, left empty, or a negative value. If it encounters any of these, it returns -1 back to the main class to prompt the user for a new input, so the cycle can repeat. If it validates that it is a positive value it returns the float back to the main program. However, for this homework we do not call this instead it is for future and learning purposes.  
    def checkInteger(default_value, str_value): 
        try:
            default_value = int(str_value)
        except TypeError:
            print()
        except: 
            print("Invalid initial value, please try again!\n")
            default_value = -1
        else:
            if default_value < 0: 
                print("Invalid initial value, please try again!\n")
                default_value = -1
        return default_value
    
#CalculationClass takes both the inital and current values that have been validated and calculates the ROI the user has. 
class CalculationClass:
    
    #__init__ function intalizes all three variables and makes sure the ROI value is a private variable, meaning it can only be accessed by the main program.  
    def __init__(self):
        self.intial_value = -1
        self.current_value = -1
        self.__roi_value = 0
    
    #Sets the value of .__roi_value after calculating it with inital and current value then it formats it to be a precentage with two decimal places. 
    def roi_calculation(self, intial_value, current_value):
        self.__roi_value = format((current_value - intial_value) / intial_value, '.2%')
        
    #Enables the main program to access the .__roi_value, meaning that the main program can only read the calcualted ROI value. 
    def get_roi(self):
        return self.__roi_value
        
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:34:02 2023

@author: ethanmikel
"""
#Author: Ethan Mikel
#Homework Number & Name: 8 Employee Management
#Due Date: April 17 by 11:59 PM
#Program Description: Program has three different classes Employee, ProductionWorker, ShiftSupervisor. The employee class is the superclass for both  ProductionWorker and ShiftSupervisor classes within both sub classes it stores the needed variables and in the __str__ method it calls the superclass __str__ method and add in the rest of the statement 

import Mikel_Ethan_HW8_Validation

#Is the address for the validation class to validate the users inputs 
validation = Mikel_Ethan_HW8_Validation.ValidationClass()

#Employee class has __init__, __str__ and the corresponding get and set methods for employees name and id, which are crucial since both employee_name and employeeID are hidden variables. In the __str__ method is returns the employees name and id 
class Employee():
    def __init__(self):
        self.__employee_name = ''
        self.__employeeID = ''
        
    def set_employee_name(self, employee_name):
        self.__employee_name=employee_name
    def get_employee_name(self):
        return self.__employee_name
    def set_employeeID(self, employeeID):
        self.__employeeID=employeeID
    def get_employeeID(self):
        return self.__employeeID
    
    def __str__(self):
        return "\nEmployee Name: " + self.__employee_name + "\nEmployee ID: " +  self.__employeeID
  
#ProductionWorker class is a subclass to the Employee class and has hidden variables with their assoicating set/get methods that contain the worker shift, hourly wage, and number of hours. As well as, in the __init__ method it is also has super().__init__() which calls employee name and id from the employee class. In the __str__ method it calls the __str__ method in the super class and then returns the employee's wage, number of hours, and their total pay (not stored but is calcualted in the return statement) 
class ProductionWorker(Employee): 
    def __init__(self):
        super().__init__()
        self.__shift = -1
        self.__hourly = -1
        self.__hours = -1
        
    def set_shift(self, str_value):
        self.__shift=validation.checkInt(str_value)
    def get_shift(self):
        return self.__shift
    def set_hourly(self, str_value):
        self.__hourly=validation.checkFloat(str_value)
    def get_hourly(self):
        return self.__hourly
    def set_hours(self, str_value):
        self.__hours=validation.checkFloat(str_value)
    def get_hours(self):
        return self.__hours
    
    def __str__(self):
        return super().__str__()+"\nEmployee Rate: $" + str(format(self.__hourly, ',.2f')) + "\nHours Worked:" + str(format(self.__hours, ',.2f')) + "\nTotal Pay: $"+str(format(self.__hours * self.__hourly, ',.2f'))
    
#ShiftSupervisor class is a subclass to the Employee class and has hidden variables with their assoicating set/get methods that contain the supervisor salary, bonus, and the total amount of pay. As well as, in the __init__ method it is also has super().__init__() which calls employee name and id from the employee class. In the __str__ method it calls the __str__ method in the super class and then returns the supervisor salary, bonus, and the total amount of pay (is a stored object) 
class ShiftSupervisor(Employee):
    def __init__(self):
        super().__init__()
        self.__salary= -1
        self.__bonus = -1
        self.__total_pay = 0
    
    def set_salary(self, str_value):
        self.__salary=validation.checkFloat(str_value)
    def get_salary(self):
        return self.__salary
    def set_bonus(self, str_value):
        self.__bonus=validation.checkFloat(str_value)
    def get_bonus(self):
        return self.__bonus
    
    def set_annual_pay(self):
        self.__total_pay = self.__salary + self.__bonus
    def get_annual_pay(self):
        return self.__total_pay
    
    def __str__(self):
        return super().__str__() + "\nSalary: $" + str(format(self.__salary, ',.2f')) + "\nBonus: $" + str(format(self.__bonus, ',.2f')) + "\nTotal Pay: $" + str(format(self.__total_pay, ',.2f'))
    
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:36:10 2023

@author: ethanmikel
"""
#Author: Ethan Mikel
#Homework Number & Name: 8 Employee Management
#Due Date: April 17 by 11:59 PM
#Program Description:
    
import Mikel_Ethan_EmployeeFile

#Address for both the Employee and ShiftSupervisor class
employee = Mikel_Ethan_EmployeeFile.Employee()
supervisor = Mikel_Ethan_EmployeeFile.ShiftSupervisor()

#Main class calls the employee_info, salary_bonus methods, and then calls/prints the str method from ShiftSupervisor class in the EmployeeFile
def main():
    employee_info()
    salary_bonus()
    supervisor.set_annual_pay()
    print(supervisor)
    
#Prompts the user to input their name and id to then be set to both the Employee and ProductionWorker classes
def employee_info():
    employee_name=input("What is this employee's name? ")
    employee.set_employee_name(employee_name)
    supervisor.set_employee_name(employee_name)

    employee_id=input("\nWhat is this employee's ID? ")
    employee.set_employeeID(employee_id)
    supervisor.set_employeeID(employee_id)
    
def salary_bonus():
    
    #Pormpts the user to input the correct salary, then it calls the set_salary method in ShiftSupervisor to ensure it is a desired input (a positive number). If the return value from the get method is -1 then it will prompt the user again
    salary = -1
    while salary == -1:
        str_value = input("\nWhat is the employee's salary? ")
        supervisor.set_salary(str_value)
        salary=supervisor.get_salary()
        if salary == -1:
            print("This pay rate is not valid. Try again.\n")
    
    #Pormpts the user to input the correct bonus, then it calls the set_bonus method in ShiftSupervisor to ensure it is a desired input (a positive number). If the return value from the get method is -1 then it will prompt the user again
    bonus = -1
    while bonus == -1:
        str_value = input("\nhat is the employee's bonus ")
        supervisor.set_bonus(str_value)
        bonus=supervisor.get_bonus()
        if bonus == -1:
            print("This hours worked is not valid. Try again.\n")

#Calls main
main()
            

    

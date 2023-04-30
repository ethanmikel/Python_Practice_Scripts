#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:35:51 2023

@author: ethanmikel
"""
#Author: Ethan Mikel
#Homework Number & Name: 8 Employee Management
#Due Date: April 17 by 11:59 PM
#Program Description:

import Mikel_Ethan_EmployeeFile

#Address for both the Employee and ProductionWorker class
employee = Mikel_Ethan_EmployeeFile.Employee()
production_worker = Mikel_Ethan_EmployeeFile.ProductionWorker()

#Main class calls the employee_info, employee_schedule_pay methods, and then calls/prints the str method from ProductionWorker class in the EmployeeFile
def main():
    employee_info()
    employee_schedule_pay()
    #print(employee)
    print(production_worker)

#Prompts the user to input their name and id to then be set to both the Employee and ProductionWorker classes
def employee_info():
    employee_name=input("What is this employee's name? ")
    employee.set_employee_name(employee_name)
    production_worker.set_employee_name(employee_name)

    employee_id=input("\nWhat is this employee's ID? ")
    employee.set_employeeID(employee_id)
    production_worker.set_employeeID(employee_id)
    
def employee_schedule_pay():
    
    #Prompts the user to input the shift (day or night, must be either a 1 or 2). It then calls the EmployeeFile to ensure the users input is correct and is a 1 or 2, will contuine to prompt user until desired value. If the return value from the get method is -1 then it will prompt the user again
    shift = -1
    while shift == -1:
        str_value = input("\nWhat shift does this employee work (1=day and 2=night)? ")
        production_worker.set_shift(str_value)
        shift=production_worker.get_shift()
        if shift == -1:
            print("Please enter a valid shift (1 or 2)")
      
    #Pormpts the user to input the correct hourly wage, then it calls the set_hourly method in ProductionWorkers to ensure it is a desired input (a positive number). If the return value from the get method is -1 then it will prompt the user again
    hourly_pay = -1
    while hourly_pay == -1:
        str_value = input("What is the employee's pay rate? ")
        production_worker.set_hourly(str_value)
        hourly_pay=production_worker.get_hourly()
        if hourly_pay == -1:
            print("This pay rate is not valid. Try again.\n")
    
    #Pormpts the user to input the correct number of hours, then it calls the set_hours method in ProductionWorkers to ensure it is a desired input (a positive number). If the return value from the get method is -1 then it will prompt the user again
    hours = -1
    while hours == -1:
        str_value = input("\nHow many hours did this employee work? ")
        production_worker.set_hours(str_value)
        hours=production_worker.get_hours()
        if hours == -1:
            print("This hours worked is not valid. Try again.\n")
  
#Calls main
main()
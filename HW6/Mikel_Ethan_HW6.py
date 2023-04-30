#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:51:38 2023

@author: ethanmikel
"""

#Author: Ethan Mikel
#Homework Number & Name: 6 Stock Prices
#Due Date: Mar 20 by 12pm
#Program Description: The program is desinged to read the weekly closing prices then put the inputs into a 2D list to then allow a user to input the desired start and end week to then return the average change and the highest/week change in a week.
    
#Calls the apple_list, start_week_input, end_week_input, and traverse_list_calc to then be able to get the desired inputs from the user and then output the desired values of change of the weekly end stock prices. 
def main():
    apple_stock_list=apple_list()
    #print(apple_stock_list)
    start_week=start_week_input()
    #print(start_week)
    end_week=end_week_input(start_week)
    #print(end_week)
    traverse_list_calc(apple_stock_list, start_week, end_week)
   
#Reads the ApplePrices.txt file to then be able to put the weekly end stock prices in to a list, along with the week the end prices are associated with, and the change in stock price from one week to another. Once the list has been filled with all of the end prices for every week, it returns the list
def apple_list():
    apple_list=[]
    week=1
    temp_stock_price=0.0
    dif_stock_price=0.0
    week=1
    apple_stock_price=open('ApplePrices.txt', 'r')
    stock_price = apple_stock_price.readline().rstrip("\n")
    try:
        while stock_price != '':
            apple_list+=[[week,float(stock_price),dif_stock_price]]
            week+=1
            temp_stock_price=float(stock_price)
            stock_price = apple_stock_price.readline().rstrip("\n")
            dif_stock_price=round(float(stock_price)-temp_stock_price, 2)
    except ValueError:
        return apple_list
    
#Allows the user to input a desired week from 1 to 52 inclusively; however, if a user inputs a non-numerical value it automatically sets the start week to 1. This method also calls input_validation to validate the start week to be incluslive to 1 and 52, the returns the start week
def start_week_input():
    flag = True
    while flag == True:
        start_week = input("Please enter the start week: ")
        if start_week == '':
            start_week = 1
            flag = False
        else:
            try:
                start_week = int(start_week)
            except ValueError:
                if not start_week:
                    start_week = 1
                else:
                    print("Week must be a valid numeric value.")
            else:
                if start_week < 1 or start_week > 52:
                    print("You must enter a valid numeric value between 1 and 52.")
                else:
                    flag = False
    return int(start_week)

#Allows the user to input a desired week from 1 to 52 inclusively; however, if a user inputs a non-numerical value it automatically sets the end week to 52. This method also calls input_validation to validate the start week to be incluslive to 1 and 52, then returns the end week 
def end_week_input(start_week):
    flag = True
    while flag == True:
        end_week = input("Please enter the end week: ")
        if end_week == '':
            end_week = 52
            flag = False
        else:
            try:
                end_week = int(end_week)
            except ValueError:
                if not end_week:
                    end_week = 52
                else:
                    print("Week must be a valid numeric value")
            else:
                if end_week < 1 or end_week > 52:
                    print("You must enter a valid numeric value between 1 and 52.")
                elif end_week < start_week:
                    print("End week cannot be before start week.")
                else:
                    flag = False
    return int(end_week) 

#Uses the apple_stock_list, start_week, end_week previosuly found in the other methods. With the apple_stock_list we find the desired weeks we need by setting the start-1/end week to the range of a for loop, then we are able to caluclate the total amount of change within the desired weeks. We also check every week to see if there is a new highest and lowest minimum change in a week. Once it has travesered the desired week in the list it then prints out the start week, end week, average change (calculated), and the min/max week of change
def traverse_list_calc(apple_stock_list, start_week, end_week):
    change_total=0
    max_change=0
    min_change=0
    for i in range(start_week-1,end_week):
        change_total = change_total + apple_stock_list[i][2]
        if apple_stock_list[i][2] > max_change:
            max_change = apple_stock_list[i][2]
            max_week = i+1
        elif apple_stock_list[i][2] < min_change:
            min_change = apple_stock_list[i][2]
            min_week = i+1
    average_change = round(change_total/(end_week-start_week+1),2)
    
    print("\nStart Week:", start_week)
    print("End Week:", end_week)
    print('The average change is:', average_change)
    print('The week with the highest change is week',max_week,'with a change of',max_change)
    print('The week with the lowest change is week',min_week,'with a change of',min_change)
    
#Calls main function
main()
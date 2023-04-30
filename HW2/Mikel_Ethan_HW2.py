#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:12:42 2023

@author: ethanmikel
"""

#Author: Ethan Mikel
#Homework Number & Name: 2 Audiobooks
#Due Date: Feb. 1 by 12pm
#Program Description: This program This program is designed for a user to input their name, the amount of books they want to purchase, the type of member they are, and if they are a regular member prompt them by asking if they would like to upgrade their membership to premimum. Based on a users inputs the program will then figure out the price the user will pay for their books, the amount of free books they will receive, and the total amount they will pay. It will then print out a product summary to give the user a recipt of their transaction.  

#Instantiate both the tax and membership_fee variables that will be used in the program later to ensure there is not any errors when using them and allows us to quickly change both of them without having to search for them in our code. 
tax=.0825
membership_fee=4.95

#Asks the user for their name, the number of books they would like to purchase, and what the current type of their membership is 
customer_name=input("What is your name? ")
quantity_book=int(input("How many books would you like to buy? "))
membership_type=input("What type of member are you? (Press R for Regular or P for Premium): ")

#Takes the input of the user from the variable membership_type and if the user inputs an R/r then  the program asks the user if they would like to upgrade their membership to Premimum. 
if membership_type == "R" or membership_type == "r": #Opening if statement that is true when a user inputs either R/r and if the user inputs Y/y then it will upgrade the users membership
    upgrade_membership=input("Would you like to upgrade to a premium membership for a fee of $4.95? (Y for Yes or N for No): ") #Prompts the user by asking if they would like to upgrade their membership to premium by entering 'Y/y' or 'N/n'
else: #Assumes the user is already a premium user or declines to upgrade their membership 
    upgrade_membership="N" #Ensures that if the previous user upgraded their membership that if the customer does not want to be upgraded that they will not be upgraded by changining the upgrade_membership to N

#This if loop is that is true for either memebers who have inputed that they were a Premuimum member or if they upgraded their membership to a premimum mebership, when the program understands the users membership then it will set the book_price to the correct amount and change the membership_type to the 'Premium' word to be outputted later
if membership_type == "P" or membership_type == "p" or upgrade_membership == "y" or upgrade_membership == "Y":
    book_price=8.49 #Sets the premuim member book price to $8.49
    membership_type="Premium" #Sets the premium member membership_type to 'Premium' 
else: #Assumes that if the user dud not meet the test case for the if loop then they are a regular member and sets their book price to the regular member fee and sets the membership_type to "Regular" to be outputed later
    book_price=9.95 #Sets the regular member book price to $9.95
    membership_type="Regular" #Sets the regular member membership_type to 'Regular' 
    
subtotal=book_price*quantity_book #Calcalutes the subtotal by multiplying the book_price, which was found in the previous if-loop by the users membership status by the number of books they are purchasing 
tax=tax*subtotal #Calcalutes the tax by multiplying the tax variable we instanited as 0.0825 in the beginning of our program by the subtotal we calculated in the previous line
total=tax+subtotal #Calculares the total the user will pay by adding the tax and the subtotal the program previously calculated in the previous lines
    
#This if-loop that is calculating the number of free books the user will receive based off their membership status and the number of books they have purchased. 
if membership_type == "Premium" : #Checks to see if the user is a premium member because the number of free books a user receives is different by the number of books they purchase (e.g. a regular user gets 2 free books if they purchase more than 12 book, but a premium user gets 2 free books if they buy more than 9 books)
    if quantity_book > 9: #If the premium user bought more than 9 books than this if-loop will add two books to the total number of books the user purchased 
        quantity_book=quantity_book+2 #Adds two books to the total quantity of books
    elif quantity_book >= 6 and quantity_book <= 9: #If the premium user bought more than 6, but less than 9 books than this if-loop will add one book to the total number of books the user purchased 
        quantity_book=quantity_book+1 #Adds one books to the total quantity of books
else: #THis else assumes that the user is a regular member since the if statement was returned false. 
    if quantity_book > 12: #If the regular user bought more than 12 books than this if-loop will add two books to the total number of books the user purchased 
        quantity_book=quantity_book+2 #Adds two books to the total quantity of books
    elif quantity_book >= 8 and quantity_book <= 12: #If the regular user bought more than 8, but less than 12 books than this if-loop will add one book to the total number of books the user purchased 
        quantity_book=quantity_book+1 #Adds one books to the total quantity of books

#First returns a line, then this block prints out the product summary by prinitng out the users name, membership type, number of books, and the subtotal we caluclated
print("\n------Product Summary------")
print("Customer Name:",customer_name)
print("Customer Type:",membership_type)
print("Total Books:", quantity_book)
print("Subtotal: $"+str(format(subtotal, '.2f')))

#This if-loop is looking to see if the user updated their membership type to then give them a thank you message, the membership fee, and then add the membership fee to their total (since you don't have to tax the membership fee and it only apply to these types of customers)
if upgrade_membership == "Y" or upgrade_membership == "y": #This if-loop is true if the upgrade_membership variable that a regular user would be prompted if it is 'Y/y'
    print("Thank you for upgrading to premium membership!") #Prints a thank you message for upgrading their membership 
    print("Membership Fee: $"+str(format(membership_fee, ',.2f'))) #Prints out the cost of the membership fee by using the membership_fee we instantiated earlier in the program
    total=membership_fee+total #Adds the membership fee to the total amount the user will be charged 
    
#Finishes off printing the users amount they were taxed and their total they will have to pay to the audiobook company
print("Tax: $"+str(format(tax, ',.2f')))
print("Total: $"+str(format(total, ',.2f')))


# -*- coding: utf-8 -*-
# Amortization Table - Calculates an amortization table given loan details
    
# Introduction
print("Welcome to the Amortization Calculator!\nI will need the loan information to make the needed calculations...")
print("Please do not use commas or percent signs in your input")

# Get the needed information from the user: 
# Total amount given to seller
purchase_price = float(input("Purchase price in dollars: "))

# Amount of up-front money given
down_payment_percent = float(input("Down payment as a percentage: ")) 

# Annual interest rate as a percentage
interest_rate_percent = float(input("Interest Rate as a percentage: "))

# Amount of payments made in a year 
payment_type = input("Payment type (monthly, semi-monthly, bi-weekly, weekly): ").lower() 

# Amount paid for every payment made 
payment_amount = float(input("Payment amount " + str(payment_type) + ": "))

# If payment type is monthly 
if payment_type == "monthly":
    
    # They pay 12 times a year 
    payment_per_year = 12

# If payment type is semi-monthly 
elif payment_type == "semi-monthly": 
    
    # They pay 24 times a year 
    payment_per_year = 24 

# If payment type is bi-weekly
elif payment_type == "bi-weekly": 
    
    # They pay 26 times a year 
    payment_per_year = 26 

# If payment type is weekly
elif payment_type == "weekly": 
    
    # They pay 52 times a year 
    payment_per_year = 52 

# Only monthly, semi-monthly, bi-weekly, or weekly are accepted inputs
else: 
    print("The payment type can only be monthly, semi-monthly, bi-weekly, or weekly")  
    
    # Amount of payments made in a year 
    payment_type = input("Please input one of the payment type options (monthly, semi-monthly, bi-weekly, weekly): ").lower() 

# Initialize varible
total_interest = 0 
condition2 = 1
year = 1
closing = 0
interest_sum = 0 
principal_sum = 0 

# Convert down payment as a percent of the purchase price to in dollars 
down_payment = (purchase_price * down_payment_percent/100) 

# Convert interest rate as a percent to a decimal 
interest_rate = (interest_rate_percent/100) 

# How much they actually owe the bank
loan_amount = (purchase_price - down_payment) 

# FIRST ROW
# Starting amount user needs to pay off 
starting_amount = loan_amount 

# Calculate how much from their payment is going towards interest 
interest_portion = float(starting_amount * interest_rate/payment_per_year)

# Calculate how much from their payment is going towards principal 
principal_portion = float(payment_amount - interest_portion) 

# Get the ending balance 
ending_balance = (starting_amount - principal_portion)  

# The ending balance becomes the new outstanding principal 
outstanding_principal = ending_balance 

# Find total interest until mortgage is paid off 
total_interest += interest_portion

# Print amortization table 
print() 
print() 
print("------------------- Amortization Table: All numbers are displayed with 2 decimals -------------------")
print() 
    
# Print the headers
fixed_period = "{0: >7}".format("Period") 
fixed_out_principal = "{0: >25}".format("Outstanding Principal") 
fixed_payment = "{0: >11}".format("Payment")
fixed_interest = "{0: >15}".format("Interest")
fixed_principal = "{0: >15}".format("Principal")
fixed_ending = "{0: >21}".format("Ending Balance")

print(fixed_period , fixed_out_principal , fixed_payment , fixed_interest , fixed_principal , fixed_ending) 

# Print out first line
fixed_out_1 = "{0:>13.2f}".format(starting_amount)  
fixed_payment_1 = "{0:>19.2f}".format(payment_amount)
fixed_interest_1 = "{0:>13.2f}".format(interest_portion)
fixed_principal_1 = "{0:>15.2f}".format(principal_portion)
fixed_ending_1 = "{0:>20.2f}".format(ending_balance)

print(" " + (payment_type).capitalize().strip("ly") + " 001 " , fixed_out_1 , fixed_payment_1 , fixed_interest_1 , fixed_principal_1 , fixed_ending_1) 

# Every equals payment type # which starts at 1 
every = 1 

# Set a boolean to true to start the while loop 
condition = True 

# Repeat the following until mortgage is paid off 
while condition: 
    
    # Add 1 to the payment type number every line 
    every += 1 
    
    # Calculate how much from their payment is going towards interest 
    interest_portion = float(outstanding_principal * interest_rate/payment_per_year)
     
    # Calculate how much from their payment is going towards principal 
    principal_portion = float(payment_amount - interest_portion) 
    
    # Get the new ending balance
    ending_balance = (outstanding_principal - principal_portion)   
    
    # If the ending balance is not paid off yet 
    if ending_balance > 0: 
        
        # Print out the table 
        fixed_out_2 = "{0:>14.2f}".format(outstanding_principal)
        fixed_payment_2 = "{0:>19.2f}".format(payment_amount)
        fixed_interest_2 = "{0:>13.2f}".format(interest_portion)
        fixed_principal_2 = "{0:>15.2f}".format(principal_portion)
        fixed_ending_2 = "{0:>20.2f}".format(ending_balance)
            
        if every < 10: 
            print(" " + (payment_type).capitalize().strip("ly") + " 00" + str(every) , fixed_out_2 , fixed_payment_2 , fixed_interest_2 , fixed_principal_2 , fixed_ending_2) 
        
        elif every < 100: 
            print(" " + (payment_type).capitalize().strip("ly") + " 0" + str(every) , fixed_out_2 , fixed_payment_2 , fixed_interest_2 , fixed_principal_2 , fixed_ending_2) 
       
        elif every >= 100: 
            print(" " + (payment_type).capitalize().strip("ly") + " " + str(every) , fixed_out_2 , fixed_payment_2 , fixed_interest_2 , fixed_principal_2 , fixed_ending_2) 
    
        # Then the new outstancing principal is the ending balance
        outstanding_principal = ending_balance
        
        # Store ending balance in another variable for later 
        ending_balance_last = ending_balance 
        
        # Find total interest until mortgage is paid off 
        total_interest += interest_portion
        
    # If the ending balance is paid off 
    elif ending_balance <= 0: 
        
        # Calculate how much from their payment is going towards interest off the full payment amount  
        interest_portion = float(outstanding_principal * interest_rate/payment_per_year)

        # The amount of money left that is owed is the ending balance of the last line 
        outstanding_principal = ending_balance_last 

        # The payment amount is also the outstanding principal 
        payment_amount1 = outstanding_principal

        # Dont need to calculate how much is going to principal because all of it is going to principal 
        principal_portion = payment_amount1  

        # Get the ending balance which should be 0 because all paid off  
        ending_balance = (outstanding_principal - principal_portion)  
  
        # Print out the last row 
        fixed_out_3 = "{0:>14.2f}".format(outstanding_principal)
        fixed_payment_3 = "{0:>19.2f}".format(payment_amount1)
        fixed_interest_3 = "{0:>13.2f}".format(interest_portion)
        fixed_principal_3 = "{0:>15.2f}".format(principal_portion)
        fixed_ending_3 = "{0:>20.2f}".format(ending_balance)
        
        print(" " + (payment_type).capitalize().strip("ly") + " " + str(every) , fixed_out_3 , fixed_payment_3 , fixed_interest_3 , fixed_principal_3 , fixed_ending_3) 
        
        # Set the boolean to false so the loop terminates because the mortgage is over 
        condition = False 
           
# The number of lines in the table is how many payment type it took to pay off mortgage 
times = every 

# The number of years it took to pay off is the number of lines divided by how many times they pay in a year 
years = float((every)/payment_per_year)
        
# Find the total amount paid plus interest 
total_paid = (loan_amount + total_interest) 

# Extra Calculations 
print("------------------------------------------------------------------------------------------------------") 
print() 
print("Extra Information:")  
print("Intial loan amount: " + "$" + str(loan_amount)) 
print("Number of " + payment_type.strip("ly") + "s to pay off mortgage: " + str(every)) 
print("Number of years to pay off mortgage: " + str(years))  
print("Total interest paid over amortization period: " + "$" + str(total_interest)) 
print("Total principal paid/loan amount over amortization period: " + "$" + str(loan_amount)) 
print("Total amount paid (loan amount + total interest): " + "$" + str(total_paid))  
print() 

# Print the headers
print("----Total Interest and Principal Each Year----")

fixed_period_year = "{0: >5}".format("Period")
fixed_interest_yearly = "{0: >18}".format("Interest")
fixed_principal_yearly = "{0: >21}".format("Principal")
        
print(fixed_period_year, fixed_interest_yearly , fixed_principal_yearly)

# Set the starting amount to the original loan amount  
starting_amount = loan_amount 

# For the loan duration in years 
for index in range(int(years)):
    
    # If the year is 0 (the first year)
    if year == 0:
        
        # while the condition is less than or equal to 12, if it has not been 12 months yet 
        while condition2 <= int(payment_per_year):
            
            # Calculate how much from their payment is going towards interest 
            interest_portion = float(starting_amount * interest_rate / payment_per_year) 
            
            # Add the interest portion to the interest counter 
            interest_sum += interest_portion 
            
            # Calculate how much from their payment is going towards principal 
            principal_portion = float(payment_amount - interest_portion)
            
            # Add the principal portion to the principal counter 
            principal_sum += principal_portion
            
            # Closing balance is the starting amount minus the principal portion 
            closing = (starting_amount - principal_portion)
            
            # Make the condition go up by 1 
            condition2 += 1
        
        # Reset the counters back to 0 
        interest_sum = 0 
        principal_sum = 0 
        
        # Make the year counter go up by 1 
        year = year + 1
        
    # If it is anything else 
    else:
        
        # Make the condition go up by 1 
        condition2 = 1
        
        # while the condition is less than or equal to 12, if it has not been 12 months yet
        while condition2 <= int(payment_per_year):
            
            # Calculate how much from their payment is going towards interest 
            interest_portion = float(starting_amount * interest_rate / payment_per_year) 
            
            # Add the interest portion to the interest counter 
            interest_sum += interest_portion 
            
            # Calculate how much from their payment is going towards principal
            principal_portion = float(payment_amount - interest_portion)
            
            # Add the principal portion to the principal counter 
            principal_sum += principal_portion
            
            # Closing balance is the starting amount minus the principal portion 
            closing = (starting_amount - principal_portion) 
            
            # The starting amount is now the same as the closing 
            starting_amount = closing
            
            # Make the condition go up by 1 
            condition2 += 1
            
        # If the closing balance is not paid off 
        if closing > 0: 
            
            # Print the yearly updated balance
            # Add a 0 to make the alignment straight 
            if year < 10:
                print("Year " + "0" + str(year) + " " + "{0:>17.2f}".format(interest_sum) + " " + "{0:>21.2f}".format(principal_sum))
                
            
            elif year >= 10:
                print("Year " + str(year) + " " + "{0:>17.2f}".format(interest_sum) + " " + "{0:>21.2f}".format(principal_sum))
            
            # Reset the counters
            interest_sum = 0 
            principal_sum = 0 
            
        # If the closing balance is paid off 
        elif closing <= 0: 
            
            # Print the balance of the last year 
            # Add a 0 to make the alignment straight 
            if year < 10:
                print("Year " + "0" + str(year) + " " + "{0:>17.2f}".format(interest_sum) + " " + "{0:>21.2f}".format(principal_sum))
                
            
            elif year >= 10:
                print("Year " + str(year) + " " + "{0:>17.2f}".format(interest_sum) + " " + "{0:>21.2f}".format(principal_sum))
            
            # Reset the counters
            interest_sum = 0 
            principal_sum = 0 
        
        # Make the year counter go up by 1 
        year = year + 1
        
print("-----------------------------------------------")


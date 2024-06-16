#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome To The Tip Calculator")
total_bill = float(input("what Was The Total Bill?"))
tip_percentage = int(input("How Much Tip Do You Want To Leave? 10%, 12%, 15%"))
clients_amount = int(input("How Many People Are Going To Pay The Bill?"))
tip_amount = (total_bill * tip_percentage / 100)
whole_bill = (total_bill + tip_amount)

amount_per_person = whole_bill / clients_amount
amount_per_person_rounded_two = "{:.2f}".format(amount_per_person)
print(f"Each Person Should Pay: {amount_per_person_rounded_two}")
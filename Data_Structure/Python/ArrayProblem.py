monthly_expenses = [2200, 2350, 2600, 2310, 2190]

print("Monthly expenses in each month are:")
for month, expense in enumerate(monthly_expenses, start=1):
    print(f"{month}: {expense}$")

print("\n")
print("Here:\n1: Jan\t2: Feb\t3: Mar\t4: Apr\t5: May")
print("\n")

print("In February, how many dollars were spent extra compared to January?")
extra_in_feb = monthly_expenses[1] - monthly_expenses[0]
print(f"{extra_in_feb}$")
print("\n")

print("Find out your first 3 months' expenses:")
quarter_expenses = sum(monthly_expenses[:3])
print(f"{quarter_expenses}$")
print("\n")

print("Did you spend exactly 2000$ in any month?")
result = False
for month, expense in enumerate(monthly_expenses, start=1):
    if expense == 2000:
        print(f"Yes, in month {month}")
        result = True

if not result:
    print("No")
print("\n")

print("June month has finished and your expense is $1980. Adding it to the list.")
monthly_expenses.append(1980)
print("Updated expenses:", monthly_expenses)

print("You returned an item bought in April and got a refund of $200. Making corrections.")
monthly_expenses[3] -= 200
print("Updated expenses:", monthly_expenses)

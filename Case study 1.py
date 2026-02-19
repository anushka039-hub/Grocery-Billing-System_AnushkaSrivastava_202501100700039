# Grocery Billing System
print("WELCOME TO GROCERY MART")
item1 = int(input("Enter the price of item 1: "))
item2 = int(input("Enter the price of item 2: "))
item3 = int(input("Enter the price of item 3: "))

total_cost = item1+item2+item3

discount = 0
if total_cost >50:
  discount=0.10*total_cost

final_amount = total_cost-discount

print("GROCERY BILL :- ")
print("(Discount is applicable only if the total amount exceeds 50$)")
print('Orignal total cost: $',total_cost)
print("Discount: $", discount)
print("Final total amount after discount: $",final_amount)

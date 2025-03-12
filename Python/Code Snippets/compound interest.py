#program to find compound interest

#inputing the data
principle_amt = float(input("ENTER PRINCIPLE AMOUNT: "))
rate = float(input("ENTER INTEREST RATE: "))
time = int(input("ENTER TIME PERIOD: "))

#calculating interest
total_amt = principle_amt * (1 + (rate / 100)) ** time
interest = total_amt - principle_amt

#display interest and total amount
print(f"INTEREST TO BE PAID = {interest}")
print(f"TOTAL AMOUNT PAYABLE = {total_amt}")
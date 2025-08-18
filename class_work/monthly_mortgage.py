Principal_amount = int(input("Enter the Principal Amount: "))
Annual_Interest_Rate = float(input("Enter Annual Interest Rate: "))
Loan_Duration = int(input("Enter the loan duration in years: "))
 
Monthly_Payment = Annual_Interest_Rate / (12 * 100)
Loan_Duration1 = Loan_Duration * 12

Mortgage1 = Monthly_Payment * (( 1 + Monthly_Payment) ** Loan_Duration1)
Mortgage2 = (( 1 + Monthly_Payment) ** Loan_Duration1) - 1

Main_Mortgage = Principal_amount * (Mortgage1 / Mortgage2)
print("Your Monthly Payment Is: " , Main_Mortgage,"%")
 
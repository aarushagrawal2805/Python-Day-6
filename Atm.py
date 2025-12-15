class ATM:
    def __init__(self, acctype, no, bal):
        self.acctype = acctype
        self.no = no
        self.bal = bal

    def Create_account(self):
        print("----Enter Details To Create Account----")
        self.name=input("Enter Your Name :")
        self.no1=int(input("Enter Your Account Number :"))
        self.bal1=int(input("Deposit Amount :"))
        print("Your Account Created Succesfully !")
        print("Account Holder Name :",self.name)
        print("Account No. :",self.no1)
        print("Account Balance :",self.bal1)

    def change_pin(self):
        self.pin = int(input("Enter New PIN: "))
        print("New PIN Set Successfully!")


    def deposit(self):
        amount = int(input("Enter Amount To Deposit: "))
        self.bal += amount
        print(amount, "Deposited successfully!")
        print("Updated Balance:", self.bal)

    def withdrawal(self):
        amount = int(input("Enter Amount To Withdraw: "))

        if amount <= self.bal:
            self.bal -= amount
            print(amount, "Withdrawn Successfully!")
            print("Updated Balance:", self.bal)
        else:
            print("Insufficient Balance!")
            print("Available Balance:", self.bal)


# ---------------- OBJECT ----------------

ac1 = ATM("Saving Account", 22334455661, 5000)
ac1.pin = 123   # initial PIN

print("----------- ACCOUNT -----------")

chance = 0

while chance < 3:
    userpin = int(input("Enter PIN: "))

    if userpin == ac1.pin:
        print("Account Number  :", ac1.no)
        print("Account Type    :", ac1.acctype)
        print("Account Balance :", ac1.bal)

        print("\n1. Withdrawal")
        print("2. Deposit")
        print("3. Change PIN")
        print("4. Create Account")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ac1.withdrawal()
        elif choice == 2:
            ac1.deposit()
        elif choice == 3:
            ac1.change_pin()
        elif choice == 4:
            ac1.Create_account()
        elif choice == 5:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid Choice!")

    else:
        print("Wrong PIN! Try Again")

if chance == 3:
    s="\U0001F600"
    print("Card Blocked!")
    print("Contact To Your Bank",s)

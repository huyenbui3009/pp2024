#simulate a shared bank account . 2 threads= account holders
# both withdraw funds simul. account balance is synchronized properly to prevent race condition

# withdraw method with lock to sync access and prevent race condition ()

import threading 
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            current_balance=self.balance
            if amount<= current_balance:
                newbalance= current_balance-amount
                self.balance=newbalance #UPDATE CURRENT BALANCE AFTER WITHDRAWAL
                print(f"Successful withdrawal with new balance {newbalance}")
            else:
                print("Unsuccesull withdrawal")

def account_holder(account, amount):
    for i in range(3): #withdraw on this account for 3 times
        account.withdraw(amount) #each Object"account" with withdraw method

if __name__ == "__main__":
    aBankAccount=BankAccount(3000)
    thread_person1=threading.Thread(target=account_holder, args=(aBankAccount,200))
    thread_person2=threading.Thread(target=account_holder, args=(aBankAccount,400))

    thread_person1.start()
    thread_person2.start()

            



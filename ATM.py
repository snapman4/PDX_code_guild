def check_balance():
    return account_balance


def deposit(amount):
    balance = int(account_balance) + int(amount)
    return balance


def check_withdrawal(amount):
    if account_balance > amount:
        return True


def withdraw(amount):
    balance = int(account_balance - amount)
    return balance


def calc_interest():
    post_interest_balance = float(account_balance * 1.01)
    return post_interest_balance


transaction_type = input(
    "What would you like to do today?\n (c)heck balance \n (d)eposit \n (w)ithdrawal \n (i)nterest to be earned\n "
    "select (c), (d), (w) or (i): ")

account_balance = int(0)


def main():
    if transaction_type == "c":
        print("Your account balance is: ${}".format(check_balance()))
    elif transaction_type == "w":
        withdraw_amount = input("How much would you like to withdraw?: ")
        withdraw_amount = int(withdraw_amount)
        (check_withdrawal(withdraw_amount))
        if account_balance > withdraw_amount:
            (withdraw(withdraw_amount))
            new_balance = account_balance - withdraw_amount
            print("Your new balance is: ${}".format(new_balance))
        else:
            print("You don't have enough funds, your balance is: ${}".format(account_balance))
    elif transaction_type == "d":
        amount = input("How much would you like to deposit?: ")
        balance = deposit(amount)
        print("Thank you, your new balance is ${}".format(balance))
    elif transaction_type == "i":
        interest_balance = (calc_interest())
        print("Your new balance after added interest is: ${}".format(interest_balance))

main()

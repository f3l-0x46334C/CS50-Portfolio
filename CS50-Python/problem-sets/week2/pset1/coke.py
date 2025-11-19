def main():
    user_paid = 0
    amount_due = 50
    while user_paid < 50:
        coin_insert = input("Insert Coin: ")
        if not coin_insert.isdigit() or coin_insert not in ["5", "10", "25"]:
            print(f"Amount Due: {amount_due}")
        elif coin_insert.isdigit() and coin_insert in ["5", "10", "25"] and amount_due > 0:
            if user_paid + int(coin_insert) > 0:
                user_paid += int(coin_insert)
                amount_due = calc_amount_left(user_paid)
                print(amount_receivable(amount_due))

def calc_amount_left(coin_inserted) -> int:
    return 50 - coin_inserted

def amount_receivable(amount):
    if amount > 0: 
        return f"Amount Due: {amount}"
    else:
        change_owe = 0 - amount
        return f"Change Owed: {change_owe}"
        
main()
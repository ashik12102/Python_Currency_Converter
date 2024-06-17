def amount_validation():

    while True:
        try:
            Amount = float(input("Enter the amount to be converted: ").strip())
            
        except ValueError:
            print("the amount is invalid")
            continue
        if Amount<0:
            print("Amount needs to greater than 0")
            continue
        elif Amount == 0:
            print("Amount cannot be zero. Please enter an amount greater than 0")
        else:
            return Amount
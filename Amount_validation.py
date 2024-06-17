def amount_validation():

    while True:
        try:
            Amount = float(input("Enter the amount to be converted: "))
            
        except ValueError:
            print("the amount is invalid")
            continue
        if Amount<0:
            print("Amount needs to greater than 0")
        else:
            return Amount
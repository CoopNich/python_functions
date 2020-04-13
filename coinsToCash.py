def calc_dollars(**coins):
    
    dollarAmount = 0
    
    for key, value in coins.items():
        if key == "pennies":
            penny_change = value / 100
            dollarAmount += penny_change
        elif key == "nickels":
            nickel_change = value / 20
            dollarAmount += nickel_change
        elif key == "dimes":
            dimes_change = value / 10
            dollarAmount += dimes_change
        elif key == "quarters":
            quarter_change = value / 4
            dollarAmount += quarter_change

    print(dollarAmount)



calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)
one_to_100 = list(range(1, 101))

chicken = "Chicken"
monkey = "Monkey"
chicken_monkey = "ChickenMonkey"

for number in one_to_100:
    if number // 5 == number / 5 and number // 7 == number / 7:
        print(chicken_monkey) 
    elif number // 5 == number / 5:
        print(chicken)
    elif number // 7 == number / 7:
        print(monkey)
    else:
        print(number)
    
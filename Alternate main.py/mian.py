# shopping_list = ['apples','plums','pizza']
# print(shopping_list[2])

# shopping_list = ['apples','plums','pizza']
# print(shopping_list[2])


# import random
# shopping_list = ['apples','plums','pizza']
# print(shopping_list[random.randint(0,2)])

def get_number():
    while True:
        num = input("Give me a number.")
        try:
            num = int(num)
            return
        except:
            print("That's not a number")

num = get_number()

print(num)



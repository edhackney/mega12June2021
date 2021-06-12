# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options

for i, candy in enumerate(candy_list):
    print(f'[{candy_list.index(candy)}] {candy}')

print("which candy do you want? (enter a number)")
for x in range(allowance):
    selected = input("What number do you want: ")
    candy_cart.append(int(selected))

for candy in candy_cart:
    print(candy)



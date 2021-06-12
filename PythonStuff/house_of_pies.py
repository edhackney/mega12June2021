print("Welcome to the House of Pies! Here are our pies:")
pie_list = [" ", "Pecan", "Apple Crisp", "Bean", "Banoffee",  "Black Bun", "Blueberry", "Buko", "Burek",  "Tamale", "Steak"]
# choice = input("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak")


for i, pie in enumerate(pie_list):
    print(f'[{pie_list.index(pie)}] {pie}')

selection = input("which number pie would you like?")

print()
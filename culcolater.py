def two_numbers():
    while True:
        first_num = input("\nType the first number: ")
        while not first_num.isdigit():
            first_num = input("Please type a number: ")

        operation1 = input("Type the opretion: ")
        while operation1 not in operations:
            operation1 = input("Please type an opretion: ")

        second_num = input("Type the second number: ")
        while not second_num.isdigit():
            second_num = input("Please type a number: ")

        result = eval(f"{int(first_num)}{operation1}{int(second_num)}")
        print(f"{first_num} {operation1} {second_num} = {result} ")
        break

def three_numbers():
    while True:
        first_num = input("\nType the first number: ")
        while not first_num.isdigit():
            first_num = input("Please type a number: ")

        operation1 = input("Type the opretion: ")
        while operation1 not in operations:
            operation1 = input("Please type an opretion: ")

        second_num = input("Type the second number: ")
        while not second_num.isdigit():
            second_num = input("Please type a number: ")

        operation2 = input("Type the opretion: ")
        while operation2 not in operations:
            operation2 = input("Please type an opretion: ")

        third_num = input("Type the second number: ")
        while not third_num.isdigit():
            third_num = input("Please type a number: ")

        result = eval(f"{int(first_num)}{operation1}{int(second_num)}{operation2}{int(third_num)}")
        print(f"{first_num} {operation1} {second_num} {operation2} {third_num} = {result} ")

        break
    

operations = ['+','-','*','%','/','//']
print("\nWelcome to the calculator!\n")
system = input("Do you want to two numbers or three?\nlike (1 + 2) or (1 + 2 + 3)\ntype (2 or 3) or (two or three): ").lower()

while True:
    while system not in ('2' , '3' , 'two' , 'three'):
        system = input("Please type 2 or 3: ")
        
    if system in ('2', 'two'):
        two_numbers()

    elif system in ('3', 'three'):
        three_numbers()
    
    again = input("Do you want to calculate again?\nType yes if you want or enter any thing to exit: ").lower()
    if again != 'yes':
        break


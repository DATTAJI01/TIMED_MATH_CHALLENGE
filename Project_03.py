import random
import time

OPERATIONS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
Total_Problems = 15

def generate_problem():
    operand1 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operand2 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operation = random.choice(OPERATIONS)
    

    expression = str(operand1) + operation + str(operand2)

    answer = eval(expression)
    return expression, answer

wrong = 0
input("Press Enter to Begin!")
print("-------------------------------")

start_time = time.time()

for i in range(Total_Problems):
    expression, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ":" + expression + " = ")
        if guess == str(answer):
            print("Correct!")
            break
        wrong +=1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("-------------------------------")

print("Nice work! You finished in", total_time, "seconds.")




    









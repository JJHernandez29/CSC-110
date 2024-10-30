"""
Program: numberGenAndComp.py
Author: JJ Hernandez
Last date modified:4/18/2024
"""
import random

def numberGeneration(filename):
    with open(filename, 'w') as file:
        for _ in range(25):
            num = random.randint(1, 100)  # Generate random numbers between 1 and 100
            file.write(str(num) + '\n')

def isDescending(lst):
    if not lst:
        return True  # Empty list is considered descending
    return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

def main():
    filename = "q6numbers.txt"
    numberGeneration(filename)
    
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    if isDescending(numbers):
        print("The numbers in q6numbers.txt are in descending order.")
    else:
        print("The numbers in q6numbers.txt are not in descending order.")

if __name__ == "__main__":
    main()

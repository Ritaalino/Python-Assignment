# chaos.py (prints 20 values)
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):  # Changed from 10 to 20 iterations
        x = 3.9 * x * (1 - x)
        print(x)

main()

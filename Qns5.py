# chaos.py (user-determined number of values)
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))  # Get the number of values to print

    for i in range(n):  # Loop will now run 'n' times
        x = 3.9 * x * (1 - x)
        print(x)

main()

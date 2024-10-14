# chaos_table.py
def main():
    print("This program illustrates a chaotic function with two inputs")
    
    # Get two inputs from the user
    x1 = eval(input("Enter the first number between 0 and 1: "))
    x2 = eval(input("Enter the second number between 0 and 1: "))
    
    # Print the header for the table
    print("\n{:>10} {:>10}".format("Input 1", "Input 2"))
    print("-" * 22)
    
    # Loop to print 10 iterations of the chaotic function for both inputs
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{:>10.6f} {:>10.6f}".format(x1, x2))

main()

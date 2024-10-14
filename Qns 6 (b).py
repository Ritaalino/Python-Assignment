# chaos_b.py
def main():
    print("This program illustrates a chaotic function (b)")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * (x - x * x)
        print(x)

main()

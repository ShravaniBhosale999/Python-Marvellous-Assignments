#Program to check whether a number is even or odd using functions
def chknum(number):
    if number %2==0:
        print("Even")
    else:
        print("Odd")
    

if __name__ == "__main__":
    num=int(input("Enter a number: "))
    chknum(num)
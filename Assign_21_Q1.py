# Write a Python program to display prime and non-prime numbers in a list using multithreading.
import threading

def display_prime(lst):
    print("Prime numbers in the list are:")
    for num in lst:
        if num>1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=" ")
    print()

def dispay_nonprime(lst):
    print("Non prime numbers in the list are:")
    for num in lst:
        if num <=1:
            print(num,end="")
        else:
            for i in range(2,num):
                if (num % i) == 0:
                    print(num,end=" ")
                    break
    print()

def main():
    lst = list(map(int, input("Enter the list of numbers: ").split()))

    t1 = threading.Thread(target=display_prime, args=(lst,))
    t2 = threading.Thread(target=dispay_nonprime, args=(lst,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
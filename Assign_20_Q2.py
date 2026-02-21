import threading

def Evenfactor(n):
    print("Evenfactor thread started")

    sum = 0   # initialize once

    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            print(i)
            sum += i   # add factor value

    print("Sum of even factors:", sum)
    print("Evenfactor thread completed")

def Oddfactor(n):
    print("Oddfactor thread started")

    sum = 0   # initialize once

    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            print(i)
            sum += i   # add factor value

    print("Sum of odd factors:", sum)
    print("Oddfactor thread completed")


def main():
    n=int(input("Enter the number: "))
    t1 = threading.Thread(target=Evenfactor, args=(n,))
    t2 = threading.Thread(target=Oddfactor, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")



if __name__ == "__main__":
    main()

class Numbers:
    # Constructor
    def __init__(self, Value):
        self.Value = Value

    # Check Prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        
        return True

    # Sum of Factors
    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum

    # Check Perfect Number
    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    # Display Factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i)


# Example usage
obj1 = Numbers(6)

print("Prime:", obj1.ChkPrime())
print("Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of factors:", obj1.SumFactors())

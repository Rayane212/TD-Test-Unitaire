
class FizzBuzz:

    def __init__(self):
        pass
    
    def fizzbuzz(self, n):
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(i)
        return result
    
    def check_number(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return num

if __name__ == "__main__":
    n = int(input("Entrez un nombre: "))
    fizzbuzz = FizzBuzz()
    for i in fizzbuzz.fizzbuzz(n):
        print(i)
    num = int(input("Entrez un autre nombre pour vérifier: "))
    print(fizzbuzz.check_number(num))


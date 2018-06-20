'''According to Goldbach’s weak conjecture, every odd number greater than
5 can be expressed as the sum of three prime numbers.'''
primes = set()

def main():
    inputNumber = int(input("Enter number: "))
    getPrimes(inputNumber - 4)
    outputPrimeCombination(inputNumber)
    
def outputPrimeCombination(inputValue):
    outputted = set()
    for i in primes:
        for j in primes:
            for k in primes:
                if (i + j + k == inputValue):
                    if not(i in outputted and j in outputted and k in outputted):
                        if not( i > j or j > k):
                            print("{0} = {1} + {2} + {3}".format(inputValue,i,j,k))
                            outputted.add(i)
                            outputted.add(j)
                            outputted.add(k)
                    
'''This function gets all the primes up to highest input value and stores them
in the global primes set'''
def getPrimes(highestVal):
    for num in range(highestVal):
        if check_prime(num) == True:
            primes.add(num)
            
#primality check
def check_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
         return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

if __name__=="__main__":
    main()

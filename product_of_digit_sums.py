def sumofDigits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

class solution:
    def productOfDigitSums(self, A, B):
        sumA = sumofDigits(A)
        sumB = sumofDigits(B)
        return sumA * sumB
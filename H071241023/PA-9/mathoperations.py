class MathOperations:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)  # hitung bilangan faktorial

    def digit_sum(self, n):
        return sum(int(digit) for digit in str(n)) # menghitung berapa jumlah faktorialnya
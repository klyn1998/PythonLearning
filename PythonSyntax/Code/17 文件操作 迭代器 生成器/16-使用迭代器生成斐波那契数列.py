class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            self.count += 1
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


f = Fibonacci(12)  # 占时间，不占空间
for i in f:
    print(i)

# 占空间，不占时间
nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

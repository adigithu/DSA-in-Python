def sum_all(*args):
    return sum(args)
num=tuple(map(int, input("Enter a list of numbers: ").split()))
print(f"The sum is {sum_all(*num)}")
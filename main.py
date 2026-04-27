def magic_func(numbers):
    weight = 0.8
    res = 10
    for n in numbers:
        res *= weight
        res += (1 - weight) * n
    return res

if __name__ == "__main__":
    nums = [10, 20, 30, 40]
    print(magic_func(nums))

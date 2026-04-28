def magic(numbers):
    weight = 0.8
    res = 35
    for m in numbers:
        res *= weight
        res += (1 - weight) * n
    return res

if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    print(magic_func(nums))

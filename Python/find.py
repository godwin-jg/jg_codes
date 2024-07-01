def count_distinct_numbers(n, m):
    def count_numbers_with_unique_digits(num_digits):
        if num_digits == 1:
            return 10
        count = 9
        for i in range(9, 9 - num_digits + 1, -1):
            count *= i
        return count

    total_count = 0
    for num_digits in range(len(str(n)), len(str(m)) + 1):
        if n <= 10 ** (num_digits - 1):
            total_count += count_numbers_with_unique_digits(num_digits)
        else:
            break

    return total_count

n = 10
m = 20
result = count_distinct_numbers(n, m)
print(f"Number of distinct numbers from {n} to {m} without repeating digits: {result}")

from centraltend import average, arithmetic_mean, geometric_mean
def get_user_input():
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    return numbers

if __name__ == "__main__":
    numbers = get_user_input()

    avg = average.calculate_average(numbers)
    ar_mean = arithmetic_mean.calculate_arithmetic_mean(numbers)
    geo_mean = geometric_mean.calculate_geometric_mean(numbers)

    print(f"Average: {avg:.2f}")
    print(f"Arithmetic Mean: {ar_mean:.2f}")
    print(f"Geometric Mean: {geo_mean:.2f}")
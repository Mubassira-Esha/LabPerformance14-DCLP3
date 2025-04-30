import itertools

def find_numbers(T, k):
    # Generate all combinations of k numbers from the range 0 to 9
    numbers = range(0, 10)
    for combo in itertools.product(numbers, repeat=k):
        if product(combo) == T:
            return combo
    return None

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def main():
    T = int(input())
    k = int(input())
    
    result = find_numbers(T, k)
    
    if result:
        print(f"Case#1Input:\nT = {T}\nk = {k}")
        print(f"Case#1Output:\n{' '.join(map(str, result))}")
    else:
        print("No valid combination found.")

if __name__ == "__main__":
    main()

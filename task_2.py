from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or min > 1000:
        return []
    if max < 1 or max > 1000:
        return []
    if min > max:
        min, max = max, min
    if (max - min + 1) < quantity:
        return []

    all_numbers = list(range(min, max + 1))
    picked_numbers = sample(all_numbers, k=quantity)
    picked_numbers.sort()
    return picked_numbers

# Usage examples

print(f"6 out of 49: {get_numbers_ticket(1, 49, 6)}")
print(f"5 out of 36: {get_numbers_ticket(1, 36, 5)}")
print(f"invalid quantity: {get_numbers_ticket(1, 2, 3)}")
print(f"min less than 1: {get_numbers_ticket(-20, 2, 3)}")
print(f"min greater than 1000: {get_numbers_ticket(10_000, 2, 3)}")
print(f"max less than 1: {get_numbers_ticket(10, 0, 3)}")
print(f"max greater than 1000: {get_numbers_ticket(10, 2000, 3)}")

import random

def get_numbers_ticket(min, max, quantity):
    if 1 <= min <= max <= 1000 and 1 <= quantity <= max - min + 1:
        return sorted(random.sample(range(min, max + 1), quantity))
    else:
        print("Некоректні вхідні параметри.")
        return []
        
lottery_numbers = get_numbers_ticket(1, 100, 6)   
print("Ваші лотерейні числа:", lottery_numbers)
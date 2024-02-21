import random

# Чи треба перевіряти, що введені цілі числа? (if str(min).isnumeric() або через try-except)
def get_numbers_ticket(min, max, quantity) -> list:
    if min >= 1 and max <= 1000 and min < max:
        numbers = []
        while quantity > 0:
            number = random.randint(min, max)
            if number in numbers:
                continue
            else:
                numbers.append(number)
                quantity -= 1
        return sorted(numbers)
    else:
        return []
# Ще варіант зробити список від min до max і використати random.sample(list, quantity)    
print(get_numbers_ticket(1, 49, 6))
import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int):
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
    else:
        return []

# Ще варіант зробити список від min до max і використати random.sample(list, quantity): 
# def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
#     if isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int):
#         if min >= 1 and max <= 1000 and min < max:
#             numbers = [x for x in range(max+1)]
#             return sorted(random.sample(numbers, quantity))
#         else:
#             return []
#     else:
#         return []    
# print(get_numbers_ticket(1, 49, 6))
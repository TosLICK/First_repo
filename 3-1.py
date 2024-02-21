from datetime import datetime

# Питання: що від чого віднімати? В завданні протиріччя.
def get_days_from_today(date) -> int:
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Невірний формат"
    current_date = datetime.today().date()
    if date_obj == current_date:
        return 0
    else:
        delta_days = str(date_obj - current_date).split()
        return int(delta_days[0])

# print(get_days_from_today("2024-01-27"))
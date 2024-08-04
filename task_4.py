from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list, today: datetime=datetime.now().date()) -> list:
    congrats = []
    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").replace(year=today.year).date()
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)
        days_delta = (birthday_this_year - today).days
        if days_delta >= 0 and days_delta < 7:
            congrats_date = birthday_this_year
            if birthday_this_year.weekday() == 5:
                congrats_date = congrats_date + timedelta(days=2)
            if birthday_this_year.weekday() == 6:
                congrats_date = congrats_date + timedelta(days=1)
            congrats_date = datetime.strftime(congrats_date, "%Y.%m.%d")
            congrats.append({ "name": user["name"], "congratulation_date": congrats_date })
    return congrats

# Usage examples

users = [
    {"name": "Peter", "birthday": "1985.01.01"},
    {"name": "Joe", "birthday": "1985.01.23"},
    {"name": "Bob", "birthday": "1990.01.27"},
    {"name": "Jade", "birthday": "1990.01.28"},
    {"name": "Phill", "birthday": "1990.01.29"}
]

today = datetime.strptime("2024.01.22", "%Y.%m.%d").date()
print("Congrats list when today is 2024-01-22:", get_upcoming_birthdays(users, today))

today = datetime.strptime("2024.12.30", "%Y.%m.%d").date()
print("Congrats list when today is 2024-12-30:", get_upcoming_birthdays(users, today))

today = datetime.now().date()
print(f"Congrats list when today is {today.strftime("%Y-%m-%d")}:", get_upcoming_birthdays(users))

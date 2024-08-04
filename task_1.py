from datetime import datetime, timedelta

def get_days_from_today(date:str) -> int|None:
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None
    diff = parsed_date - datetime.now().date()
    return diff.days

# Usage examples

today = datetime.now().date()
three_days_ago = datetime.strftime(today - timedelta(days=3), "%Y-%m-%d")
three_days_from_now = datetime.strftime(today + timedelta(days=3), "%Y-%m-%d")

print(f"3 days ago: {get_days_from_today(three_days_ago)}")
print(f"3 days from now: {get_days_from_today(three_days_from_now)}")
print(f"invalid type: {get_days_from_today({})}")
print(f"invalid date format: {get_days_from_today("123-123-123")}")

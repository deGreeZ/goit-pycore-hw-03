import re

def normalize_phone(phone_number: str) -> str:
    digits_only = re.sub(r"\D", "", phone_number)
    padded_number = digits_only.rjust(13, '0')
    number_with_prefix = re.sub(r"^.{4}", "+380", padded_number)
    return number_with_prefix

# Usage examples

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("normalized numbers:", sanitized_numbers)

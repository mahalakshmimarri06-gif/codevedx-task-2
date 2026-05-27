# analyzer.py
# Purpose: Demonstrates the reusability of the security functions defined in main.py
from main import check_password_strength

password_to_test = "MySecurePass123!"
rating = check_password_strength(password_to_test)
print(f"The strength of '{password_to_test}' is {rating}")
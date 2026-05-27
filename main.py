import random
import string

def generate_password(length=12, use_special=True, use_digits=True):
    """Generates a secure password ensuring at least one of each character type."""
    if length < 4:
        return "Error: Password length must be at least 4."

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ""
    special = "!@#$%^&*()-_=+" if use_special else ""
    
    all_chars = lower + upper + digits + special
    
    # --- HERE IS THE LOGIC YOU ASKED ABOUT ---
    # Ensure at least one of each selected type
    password = [
        random.choice(lower),
        random.choice(upper)
    ]
    if use_digits: password.append(random.choice(digits))
    if use_special: password.append(random.choice(special))
    
    # Fill the rest randomly from the full combined pool
    remaining_length = length - len(password)
    password += [random.choice(all_chars) for _ in range(remaining_length)]
    
    # Shuffle to ensure security (random position)
    random.shuffle(password)
    return "".join(password)
   

def check_password_strength(password):
    """Evaluates password complexity and vulnerability level."""
    length = len(password)
    
    # Analyze the presence of different character types
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation or c in "!@#$%^&*()-_=+" for c in password)
    
    # Calculate vulnerability score (0 to 4)
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    # Vulnerability Assessment
    # Weak: Short or lacks variety (High vulnerability)
    # Medium: Moderate length or lacks some variety
    # Strong: Good length and utilizes all character types (Low vulnerability)
    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"

def main():
    print("--- Secure Password Generator & Strength Checker ---")
    while True:
        try:
            user_input = input("\nEnter desired password length (or 'q' to quit): ")
            
            if user_input.lower() == 'q':
                print("Exiting. Goodbye!")
                break
                
            length = int(user_input)
            pwd = generate_password(length)
            
            if "Error:" in pwd:
                print(f"\n{pwd}")
            else:
                print(f"\nGenerated Password: {pwd}")
                print(f"Strength Rating: {check_password_strength(pwd)}")
                
        except ValueError:
            print("Invalid input! Please enter a number or 'q' to quit.")

if __name__ == "__main__":
    main()
import re 
import secrets 
import string
import math

def check_password_strength(password):
    
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    elif len(password) >= 12:
        score += 2  
        feedback.append("Good length")
    elif len(password) >= 16:
        score += 3  
        feedback.append("Excellent length")
    else:
        score += 1
        feedback.append("Acceptable length, but 12+ characters recommended")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include atleast one uppercase letter")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include atleast one lowercase letter")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include atleast one number")
    
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Include atleast one special character")
    
    if len(re.findall(r'[A-Z]', password)) >= 2:
        score += 1
        feedback.append("Good use of multiple uppercase letters")
        
    if len(re.findall(r'[0-9]', password)) >= 2:
        score += 1
        feedback.append("Good use of multiple numbers")
        
    if len(re.findall(r'[^A-Za-z0-9]', password)) >= 2:
        score += 1
        feedback.append("Good use of multiple special characters")

    common_patterns = {
        '123': 'sequential numbers',
        'abc': 'sequential letters',
        'qwerty': 'keyboard pattern',
        'password': 'literal word "password"',
        'test': 'test word',
        'admin': 'admin word',
        '111': 'repeated digits',
        'welcome': 'common word',
        'letmein': 'common password phrase',
        '987': 'reverse sequential numbers'
    }

    found_patterns = []
    for pattern in common_patterns:
        if re.search(pattern, password.lower()):
            found_patterns.append(common_patterns[pattern])

    if found_patterns:
        score -= 2
        patterns_found = ', '.join(found_patterns)
        feedback.append(f"Contains common patterns: {patterns_found}")
    
    if score < 2:
        strength = "Very weak"
    elif score < 4:
        strength = "Weak"
    elif score < 6:
        strength = "Moderate"
    elif score < 8:
        strength = "Strong"
    else:
        strength = "Very strong"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

def display_password_strength(result):
    print(f"\nPassword Strength: {result['strength']} (Score: {result['score']}/10)")

    if result['feedback']:
        print("\nFeedback:")
        for item in result['feedback']:
            print("- " + item)

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    password = []
    
    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_numbers:
        password.append(secrets.choice(string.digits))
    if use_special:
        password.append(secrets.choice(string.punctuation))

    chars = ""
    
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    if not chars:
        print("Error: At least one character type must be selected")
        return None

    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(secrets.choice(chars) for _ in range(remaining_length))

    shuffled = list(password)
    secrets.SystemRandom().shuffle(shuffled)

    return ''.join(shuffled)

def calculate_entropy(password, char_space_size):
    #Entropy = log2(character_space_size) * password_length

    if not password:
        return 0
    return math.log2(char_space_size) * len(password)
    
def main():
    while True:
        print("\nPassword Tool Menu:")
        print("1. Check password strength")
        print("2. Generate strong password")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            password = input("Enter a password to check: ")
            result = check_password_strength(password)
            display_password_strength(result)

        elif choice == '2':
            print("Password generator")
            length = int(input("Enter the desired length of the password(8-30): "))
            if length < 8:
                print("For security , using minimum length of 8")
                length = 8
            elif length > 30:
                print("Using maximum length of 30")
                length = 30
                
            use_upper = input("Include uppercase letters? (y/n): ").lower() != 'n'
            use_lower = input("Include lowercase letters? (y/n): ").lower() != 'n'
            use_nums = input("Include numbers? (y/n): ").lower() != 'n'
            use_special = input("Include special characters? (y/n): ").lower() != 'n'

            if not any([use_upper, use_lower, use_nums, use_special]):
                print("\nAt least one character type must be selected. Using lowercase letters.")
                use_lower = True

            password = generate_password(length, use_upper, use_lower, use_nums, use_special)
            print("\nGenerated Password: ", password)

            char_space = 0
            if use_upper:
                char_space += len(string.ascii_uppercase)
            if use_lower:
                char_space += len(string.ascii_lowercase)
            if use_nums:
                char_space += len(string.digits)
            if use_special:
                char_space += len(string.punctuation)

            entropy = calculate_entropy(password, char_space)
            print(f"\nPassword Entropy: {entropy:.1f} bits")
            print("(40-60 bits: weak, 60-80 bits: reasonable, 80-100 bits: strong, 100+ bits: very strong)")


            print("\nAnalyzing generated password strength:")
            result = check_password_strength(password)
            display_password_strength(result)
        
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

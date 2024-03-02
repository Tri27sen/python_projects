def validate_password(email, password):
    # Check password length and conditions
    if len(password) > 10:
        return False
    
    # Initialize flags to track conditions
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    
    # Check each character of the password
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char == '@':
            has_special_char = True
    
    # Check if all conditions are met for the password
    if has_uppercase and has_lowercase and has_digit and has_special_char:
        # Check email domain
        if email.endswith('@google.com') or email.endswith('@yahoo.com'):
            return True
        else:
            print('Domain not allowed')
            return False
    else:
        print('Password conditions not met')
        return False

# Get user inputs for email and password
email = input('Enter your email address: ')
password = input('Enter your password: ')

# Validate the password
if validate_password(email, password):
    print('Valid password.')
else:
    print('Invalid password.')

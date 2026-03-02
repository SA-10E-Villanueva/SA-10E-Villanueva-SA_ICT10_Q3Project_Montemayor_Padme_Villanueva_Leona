from pyscript import document

def check_username(username):
    errors = []
    if len(username) < 7:
        errors.append("Username must be at least 7 characters long.")
    return errors

def check_password(password):
    errors = []
    if len(password) < 10:
        errors.append("Password must be at least 10 characters long.")
    if not any(char.isalpha() for char in password):
        errors.append("Password must contain at least one letter.")
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one number.")
    return errors

def validate_account(event):
    output_box = document.getElementById("message-box")
    username = document.getElementById("userInput").value
    password = document.getElementById("passInput").value

    username_errors = check_username(username)
    password_errors = check_password(password)
    all_errors = username_errors + password_errors

    if len(all_errors) == 0:
        output_box.innerHTML = "Account successfully created!"
        output_box.className = "success"
    else:
        output_box.innerHTML = "<br>".join(all_errors)
        output_box.className = "error"
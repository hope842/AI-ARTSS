import json
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash

USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists"
    users[username] = generate_password_hash(password)
    save_users(users)
    return True, "User registered successfully"

def login_user(username, password):
    users = load_users()
    if username not in users:
        return False, "User not found"
    if not check_password_hash(users[username], password):
        return False, "Incorrect password"
    session['user'] = username
    return True, "Logged in successfully"

def logout_user():
    session.pop('user', None)

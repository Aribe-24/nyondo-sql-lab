import sqlite3

conn = sqlite3.connect('nyondo_stock.db')


# ======================
# VALIDATION FUNCTIONS
# ======================

def is_valid_name(name):
    if not isinstance(name, str):
        return False
    if len(name) < 2:
        return False
    if any(char in name for char in ['<', '>', ';']):
        return False
    return True


def is_valid_username(username):
    if not isinstance(username, str):
        return False
    if not username or " " in username:
        return False
    return True


def is_valid_password(password):
    if not isinstance(password, str):
        return False
    if len(password) < 6:
        return False
    return True


# ======================
# SECURE FUNCTIONS
# ======================

def search_product_safe(name):
    if not is_valid_name(name):
        print("Invalid product name input")
        return None

    query = "SELECT * FROM products WHERE name LIKE ?"
    param = f"%{name}%"
    rows = conn.execute(query, (param,)).fetchall()
    return rows


def login_safe(username, password):
    if not is_valid_username(username):
        print("Invalid username")
        return None

    if not is_valid_password(password):
        print("Invalid password")
        return None

    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    return row


# ======================
# TEST CASES
# ======================

print("Test 1:", search_product_safe('cement'))          # should work
print("Test 2:", search_product_safe(''))                # rejected
print("Test 3:", search_product_safe('<script>'))        # rejected

print("Test 4:", login_safe('admin', 'admin123'))        # should work
print("Test 5:", login_safe('admin', 'ab'))              # rejected
print("Test 6:", login_safe('ad min', 'pass123'))        # rejected
import sqlite3

conn = sqlite3.connect('nyondo_stock.db')


# Secure product search
def search_product_safe(name):
    query = "SELECT * FROM products WHERE name LIKE ?"
    param = f"%{name}%"
    print(f"Query: {query} | Param: {param}")
    rows = conn.execute(query, (param,)).fetchall()
    return rows


# Secure login
def login_safe(username, password):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    print(f"Query: {query} | Params: ({username}, {password})")
    row = conn.execute(query, (username, password)).fetchone()
    return row


# ======================
# TESTS (must fail attacks)
# ======================

print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))
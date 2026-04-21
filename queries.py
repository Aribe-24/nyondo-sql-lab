# queries.py
import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# Query A - Get every column of every product
print("A:", conn.execute("SELECT * FROM products").fetchall())

# Query B - Get only the name and price of all products
print("B:", conn.execute("SELECT name, price FROM products").fetchall())

# Query C - Get full details of the product with id = 3
print("C:", conn.execute("SELECT * FROM products WHERE id=3").fetchall())

# Query D - Find all products whose name contains 'sheet'
print("D:", conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall())

# Query E - Get all products sorted by price, highest first
print("E:", conn.execute("SELECT * FROM products ORDER BY price DESC").fetchall())

# Query F - Get only the 2 most expensive products
print("F:", conn.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2").fetchall())

# Query G - Update the price of Cement (id=1) to 38,000 then SELECT * to confirm
conn.execute("UPDATE products SET price=38000 WHERE id=1")
conn.commit()
print("G:", conn.execute("SELECT * FROM products").fetchall())
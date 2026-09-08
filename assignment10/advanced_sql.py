import os
import sqlite3
## Task 1
with sqlite3.connect("../db/lesson.db") as conn:
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys =1 ")
    sql_statement = """ SELECT line_items.order_id,
SUM(products.price * line_items.quantity)
FROM line_items
JOIN orders
ON line_items.order_id = orders.order_id
JOIN products
ON line_items.product_id = products.product_id
GROUP BY orders.order_id
LIMIT 5
"""
cursor.execute(sql_statement)
results = cursor.fetchall()
for row in results:
    print(row)
## Task 2 part 1
query ="""
SELECT customers.customer_id, customers.customer_name, AVG(order_totals.total_price)
FROM customers
JOIN (
    SELECT orders.customer_id AS customer_id_b,
           SUM(products.price * line_items.quantity) AS total_price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    JOIN orders ON line_items.order_id = orders.order_id
    GROUP BY orders.order_id
) AS order_totals
ON customers.customer_id = order_totals.customer_id_b
GROUP BY customers.customer_id;"""
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)

## Task 3
query = """
SELECT customers.customer_id
FROM customers
WHERE customers.customer_name = 'Perez and Sons';
"""
cursor.execute(query)
customer_id = cursor.fetchone()[0]

query = """
SELECT products.product_id, products.product_name, products.price
FROM products
ORDER BY products.price ASC
LIMIT 5"""
cursor.execute(query)
product_ids = cursor.fetchall()

query = """
SELECT employees.employee_id
FROM employees
WHERE employees.first_name = "Miranda"
AND employees.last_name = "Harris"
"""
conn.execute("BEGIN")
cursor.execute(query)
employee_id = cursor.fetchone()[0]
cursor.execute(
    "INSERT INTO orders(customer_id,employee_id) VALUES(?,?) returning order_id",(customer_id,employee_id)
)
order_id = cursor.fetchone()[0]
for product in product_ids:
    cursor.execute(
    "INSERT INTO line_items(order_id,quantity,product_id) VALUES(?,?,?)",(order_id,10,product[0]))
    conn.commit()
query = """ SELECT line_items.line_item_id,line_items.quantity,products.product_name
FROM line_items
JOIN products
ON line_items.product_id = products.product_id
WHERE line_items.order_id = ?
"""
cursor.execute(query,(order_id,))
results = cursor.fetchall()
for row in results:
    print(row)

## Task 4
cursor.execute
query = """
SELECT employees.first_name,employees.last_name
FROM employees
JOIN orders
ON employees.employee_id = orders.employee_id
HAVING COUNT(orders.order_id)>5
"""
for row in results:
    print(row)
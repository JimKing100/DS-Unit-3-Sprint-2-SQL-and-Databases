import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

query1 = """
SELECT ProductName
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""

query2 = """
SELECT avg(julianday(HireDate) - julianday(BirthDate)) / 365
FROM Employee
"""

query3 = """
SELECT City, avg(julianday(HireDate) - julianday(BirthDate)) / 365
FROM Employee
GROUP BY City
"""

query4 = """
SELECT ProductName, CompanyName
FROM Product, Supplier
WHERE Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""

query5 = """
SELECT CategoryName, count(CategoryId) AS NumCategories
FROM Product, Category
WHERE Product.CategoryId = Category.Id
GROUP BY CategoryId
ORDER BY NumCategories DESC
LIMIT 1
"""

query6 = """
SELECT FirstName, LastName, COUNT(EmployeeId) AS TerritoryCount
FROM Employee, EmployeeTerritory
WHERE Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY EmployeeId
ORDER BY TerritoryCount DESC
LIMIT 1
"""

curs1 = conn.cursor()
print('Ten most expensive items are: ', curs1.execute(query1).fetchall())

curs2 = conn.cursor()
print('The average age of an employee at hire date = ', curs2.execute(query2).fetchall()[0][0])

curs3 = conn.cursor()
print('The average age of an employee at hire date by city  = ', curs3.execute(query3).fetchall())

curs4 = conn.cursor()
print('Ten most expensive items and their suppliers are: ',
       curs4.execute(query4).fetchall())

curs5 = conn.cursor()
print('The largest category is', curs5.execute(query5).fetchall()[0][0])

curs6 = conn.cursor()
print('The employee with the most territories is',
       curs6.execute(query6).fetchall()[0][0],
       curs6.execute(query6).fetchall()[0][1])

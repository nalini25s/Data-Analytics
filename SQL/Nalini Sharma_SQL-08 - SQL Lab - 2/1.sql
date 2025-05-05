SELECT Customers.CustomerName, SUM(Orders.Total) AS TotalSales
FROM Orders
JOIN Customers ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerName
ORDER BY Customers.CustomerName DESC;
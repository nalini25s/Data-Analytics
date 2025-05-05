
SELECT o.OrderID, LEFT(c.CustomerName, 3) AS ShortCustomerName, p.ProductName, o.Total
From Orders o
JOIN Customers c ON c.CustomerID = o.CustomerID
JOIN Products p ON p.ProductID = o.ProductID
Order BY p.ProductName ASC;

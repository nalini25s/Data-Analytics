SELECT TOP 1 Products.ProductName, SUM(Orders.Quantity) AS TotalQuantity
FROM Orders
JOIN Products ON Products.ProductID = Orders.ProductID
GROUP BY Products.ProductName; 
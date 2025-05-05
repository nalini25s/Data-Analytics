SELECT Products.ProductName, SUM(Orders.Total) AS TotalRevenue
FROM Orders
JOIN Products ON Products.ProductID = Orders.ProductID
GROUP BY Products.ProductName; 
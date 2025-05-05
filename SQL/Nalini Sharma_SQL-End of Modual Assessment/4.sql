SELECT c.CustomerName, COUNT(*) AS OrderCount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN Products p ON o.ProductID = p.ProductID
WHERE 
o.OrderDate >= '2023-12-01' AND o.OrderDate < '2024-01-01'
AND (o.Total) > 100
GROUP BY 
c.CustomerName
HAVING 
COUNT(*) >= 2;
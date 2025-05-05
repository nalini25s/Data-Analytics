SELECT LOWER(p.ProductName) AS ProductNameLower, SUM(o.Quantity) AS TotalQuantityOrdered
FROM Products p
JOIN Orders	o
ON p.ProductID = o.ProductID
GROUP BY LOWER(p.ProductName)
ORDER BY ProductNameLower;
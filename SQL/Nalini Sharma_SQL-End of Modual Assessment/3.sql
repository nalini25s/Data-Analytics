
SELECT p.ProductName, SUM(Total) AS TotalSales,
CASE
	WHEN SUM(Total) > 300 THEN 'High Revenue'
	ELSE 'Low Revenue'
END 
AS RevenueCategory
FROM Orders o
JOIN Products p
ON o.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY ProductName ASC;
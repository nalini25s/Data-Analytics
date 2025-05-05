SELECT OrderDate, COUNT(*) AS OrderCount
FROM Orders
GROUP BY OrderDate;
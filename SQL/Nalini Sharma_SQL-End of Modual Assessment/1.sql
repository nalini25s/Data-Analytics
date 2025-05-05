SELECT OrderID, ProductID, Quantity, Total 
FROM Orders WHERE ProductID IN (
SELECT ProductID FROM Products 
WHERE Price > 25);
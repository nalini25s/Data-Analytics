SELECT AVG(Likes) AS Avg_Likes
FROM user_data
Where Followers > 200
GROUP BY Followers;

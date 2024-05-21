-- Calculates the average temperature (Fahrenheit) by city and orders by temperature (descending)
SELECT city, AVG(temp) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

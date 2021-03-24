
SELECT DATE_FORMAT(CONCAT(YEAR(NOW()), '-', SUBSTRING(birthday_at, 6, 10)), '%W') AS day_week, COUNT(*) AS birthday_count FROM users GROUP BY day_week;

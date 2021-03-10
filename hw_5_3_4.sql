UPDATE users SET
    month_of_b = DATE_FORMAT(birthday_at, '%M');

SELECT * FROM users WHERE month_of_b in ('May', 'August');
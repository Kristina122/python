SELECT 
    `users`.id, 
    `users`.name,
    COUNT(orders.id) AS cnt_order
FROM `users`
JOIN orders ON `users`.id = orders.user_id
GROUP BY `users`.id;
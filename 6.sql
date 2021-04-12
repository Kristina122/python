-- 6. Cкрипты характерных выборок (включающие группировки, JOIN'ы, вложенные таблицы); --
-- 1. Возраст пользователей (физ.лиц)-- 
SELECT
  TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age
FROM individual
ORDER BY age;

-- 2. запрос на количество и сумму активных сделок в разбивке по видам валют, deal_active--
SELECT 
t1.currency_name, 
t1.cnt_sell, 
t1.total_sum_sell, 
t2.cnt_buy, 
t2.total_sum_buy 
FROM
((SELECT
  c_1.name AS currency_name,
  COUNT(da_1.currency_id_sell) AS cnt_sell,
  SUM(da_1.amount_sell) AS total_sum_sell
FROM deal_active da_1 
JOIN currency c_1 ON da_1.currency_id_sell = c_1.id
GROUP BY currency_id_sell) AS t1 
JOIN
(SELECT
  c_1.name AS currency_name,
  COUNT(da_1.currency_id_buy) AS cnt_buy,
  SUM(da_1.amount_buy) AS total_sum_buy
FROM deal_active da_1 
JOIN currency c_1 ON da_1.currency_id_buy = c_1.id
GROUP BY currency_id_buy) AS t2
ON t1.currency_name = t2.currency_name);

-- 3. кол-во открытых счетов c 2011 года --
SELECT 
    YEAR(created_at) AS year_open,
    COUNT(*) AS cnt_open
FROM `account`
GROUP BY year_open
HAVING year_open > 2010
ORDER BY created_at DESC;

-- 4. в табл account добавление столбца с разметкой на 'individual'/'business'
SELECT 
ac.id,
ac.user_id,
ac.amount,
CASE ind.idindividual OR b.idbusiness
   WHEN ind.idindividual IS NOT NULL THEN 'individual'
   WHEN b.idbusiness IS NOT NULL THEN 'business'
END AS user_type
FROM `account` ac
LEFT JOIN individual ind ON ind.user_id = ac.user_id
LEFT JOIN business b ON b.user_id = ac.user_id;
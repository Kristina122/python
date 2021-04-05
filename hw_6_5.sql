SELECT un.from_user_id, sum(count1) AS sum1 FROM (
SELECT from_user_id, count(*) AS count1
FROM vk.message
GROUP BY from_user_id
UNION ALL
SELECT user_id, count(*)
FROM vk.post
GROUP BY user_id
UNION ALL
SELECT user_id, count(*)
FROM vk.like
GROUP BY user_id
) AS un
GROUP BY un.from_user_id
ORDER BY sum1
LIMIT 10

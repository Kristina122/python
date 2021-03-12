SELECT IF(from_user_id = 82, to_user_id, from_user_id) AS friend, count(*)
FROM vk.message
WHERE 82 IN (from_user_id, to_user_id) AND IF(from_user_id = 82, to_user_id, from_user_id) IN (
SELECT IF(from_user_id = 82, to_user_id, from_user_id)
FROM vk.friend_request
WHERE 82 IN (from_user_id, to_user_id)
AND STATUS = 1)
GROUP BY friend
ORDER BY count(*) DESC
LIMIT 1
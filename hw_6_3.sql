SELECT count(*) FROM `like` WHERE `like`.user_id IN (
SELECT user_ages.user_id FROM (
SELECT user_id, TIMESTAMPDIFF(YEAR, birthday, NOW()) AS user_age
FROM vk.profile
ORDER BY user_age
LIMIT 10
) as user_ages
)

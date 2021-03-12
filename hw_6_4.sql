SELECT
    (SELECT gender FROM `profile` WHERE `profile`.user_id = `like`.user_id) AS from_gender,
    COUNT(*) AS cnt
FROM vk.like
GROUP BY
    from_gender
ORDER BY
    cnt DESC LIMIT 1

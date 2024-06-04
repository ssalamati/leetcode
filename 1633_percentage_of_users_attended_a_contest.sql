WITH users_count AS (
    SELECT COUNT(DISTINCT user_id) AS users
    FROM users
)
SELECT 
    contest_id,
    ROUND(CAST(COUNT(DISTINCT user_id) AS NUMERIC) / MAX(users) * 100, 2) AS percentage
FROM Register, users_count
GROUP BY 1
ORDER BY 2 DESC, 1

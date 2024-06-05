-- Write your PostgreSQL query statement below
SELECT today.id
FROM Weather AS today
WHERE EXISTS (
    SELECT 1
    FROM Weather AS yesterday
    WHERE today.temperature > yesterday.temperature
    AND today.recordDate = yesterday.recordDate + 1
);

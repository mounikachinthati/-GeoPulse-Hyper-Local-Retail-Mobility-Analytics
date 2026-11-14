
-- 1. Total locations
SELECT COUNT(*) AS total_locations
FROM retail_locations;

-- 2. Total retail locations
SELECT COUNT(*) AS retail_locations
FROM retail_locations
WHERE is_retail = 1;

-- 3. Retail and non-retail distribution
SELECT
    is_retail,
    COUNT(*) AS total
FROM retail_locations
GROUP BY is_retail;

-- 4. Locations by category
SELECT
    category,
    COUNT(*) AS total_locations
FROM retail_locations
GROUP BY category
ORDER BY total_locations DESC;

-- 5. Top 10 retail categories
SELECT
    category,
    COUNT(*) AS retail_count
FROM retail_locations
WHERE is_retail = 1
GROUP BY category
ORDER BY retail_count DESC
LIMIT 10;

-- 6. Missing values
SELECT
    SUM(CASE WHEN place_name IS NULL OR TRIM(place_name) = '' THEN 1 ELSE 0 END) AS missing_names,
    SUM(CASE WHEN category IS NULL OR TRIM(category) = '' THEN 1 ELSE 0 END) AS missing_categories,
    SUM(CASE WHEN latitude IS NULL THEN 1 ELSE 0 END) AS missing_latitudes,
    SUM(CASE WHEN longitude IS NULL THEN 1 ELSE 0 END) AS missing_longitudes
FROM retail_locations;

-- 7. Retail locations by postcode
SELECT
    postcode,
    COUNT(*) AS total_locations
FROM retail_locations
WHERE is_retail = 1
GROUP BY postcode
ORDER BY total_locations DESC;

-- 8. Check duplicate place names
SELECT
    place_name,
    COUNT(*) AS duplicate_count
FROM retail_locations
GROUP BY place_name
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;

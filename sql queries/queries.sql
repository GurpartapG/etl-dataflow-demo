
-- top 10 airlines by avg delay minutes
SELECT carrier_name, ROUND(AVG(arr_delay), 2) AS avg_delay_minutes,ROUND(AVG(delay_rate)*100, 2) AS avg_delay_rate_pct
FROM flight_delays
GROUP BY carrier_name
HAVING COUNT(*) > 50
ORDER BY avg_delay_minutes DESC
LIMIT 10;

-- worst airports by highest delay %
SELECT airport_name, ROUND(AVG(delay_rate)*100,2) AS avg_delay_pct, COUNT(*) AS total_records
FROM flight_delays
GROUP BY airport_name
HAVING COUNT(*) > 50
ORDER BY avg_delay_pct DESC
LIMIT 10;

-- best airports by lowest delay %
SELECT airport_name, ROUND(AVG(delay_rate)*100,2) AS avg_delay_pct, COUNT(*) AS total_records
FROM flight_delays
GROUP BY airport_name
HAVING COUNT(*) > 50
ORDER BY avg_delay_pct ASC
LIMIT 10;

-- top 10 most reliable airlines with lowest delay %
SELECT carrier_name, ROUND(AVG(delay_rate)*100, 2) AS avg_delay_pct
FROM flight_delays
GROUP BY carrier_name
HAVING COUNT(*) > 50
ORDER BY avg_delay_pct ASC
LIMIT 10;

-- delay trend by month for all airlines
SELECT year, month, ROUND(AVG(delay_rate)*100,2) AS avg_delay_pct
FROM flight_delays
GROUP BY year, month
ORDER BY year, month;

-- delay breakdown by cause
SELECT ROUND(SUM(carrier_delay) / SUM(arr_delay) * 100, 2) AS carrier_delay_pct,
ROUND(SUM(weather_delay) / SUM(arr_delay) * 100, 2) AS weather_delay_pct,
ROUND(SUM(nas_delay) / SUM(arr_delay) * 100, 2) AS nas_delay_pct,
ROUND(SUM(late_aircraft_delay) / SUM(arr_delay) * 100, 2) AS late_aircraft_delay_pct
FROM flight_delays;

-- where was the worst experience (airline and airport combo)
SELECT carrier_name, airport_name, ROUND(AVG(arr_delay), 2) AS avg_delay_pct, COUNT(*) AS flights
FROM flight_delays
GROUP BY carrier_name, airport_name
ORDER BY avg_delay_pct DESC LIMIT 10;


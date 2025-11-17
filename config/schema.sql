CREATE TABLE IF NOT EXISTS flight_delays (
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    month INTEGER,
    carrier TEXT,
    carrier_name TEXT,
    airport TEXT,
    airport_name TEXT,
    arr_flights INTEGER,
    arr_del15 INTEGER,
    arr_cancelled INTEGER,
    arr_diverted INTEGER,
    arr_delay REAL,
    carrier_ct REAL,
    weather_ct REAL,
    nas_ct REAL,
    security_ct REAL,
    late_aircraft_ct REAL,
    carrier_delay REAL,
    weather_delay REAL,
    nas_delay REAL,
    security_delay REAL,
    late_aircraft_delay REAL,
    delay_rate REAL,
    cancel_rate REAL,
    divert_rate REAL,
    delay_category TEXT,
    date TEXT
);

CREATE INDEX IF NOT EXISTS idx_carrier_month ON flight_delays(carrier, year, month);
CREATE INDEX IF NOT EXISTS idx_airport_date ON flight_delays(airport, date);

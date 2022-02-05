DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    continent VARCHAR(255),
    img_url TEXT,
    reason TEXT,
    reflection TEXT
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT REFERENCES countries(id),
    img_url TEXT,
    visited BOOLEAN,
    reason TEXT,
    reflection TEXT
);
CREATE DATABASE products;

USE products;

CREATE TABLE inventory (
	varekode int(6) UNSIGNED PRIMARY KEY,
	varenummer VARCHAR(50) NOT NULL,
	antal int NOT NULL
);
CREATE DATABASE people;

USE people;

CREATE TABLE people_table (
	personid int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	firstname VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL
);
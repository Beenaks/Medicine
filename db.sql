-- Create a new database
CREATE DATABASE medicine_supply;

-- Use the new database
USE medicine_supply;

-- Create a table for medicines
CREATE TABLE medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    expiry_date DATE NOT NULL
);

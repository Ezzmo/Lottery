CREATE DATABASE IF NOT EXISTS lottery;
GRANT ALL ON lottery.* TO 'madmin';
CREATE TABLE IF NOT EXISTS lottery.entries(
    entry_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    code CHAR(8) NOT NULL,
    winnings VARCHAR(6) NOT NULL
);

show databases;
create database finace;
use finace;
show tables;
CREATE TABLE IF NOT EXISTS stock (
date_time DATE,stock_id VARCHAR(20), 
Trading_Volume INT,
Trading_money INT,
open_price DECIMAL(10, 2),
max DECIMAL(10, 2), 
min DECIMAL(10, 2),
close_price DECIMAL(10, 2),
spread DECIMAL(10, 2),
Trading_turnover INT) ; 
show variables like 'secure_file_priv';
SHOW GLOBAL VARIABLES LIKE 'local_infile';
set global local_infile = 'ON';
ALTER TABLE stock MODIFY COLUMN Trading_money bigint;
LOAD DATA INFILE '/var/lib/mysql-files/0050.csv' INTO TABLE stock
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' ignore 1 lines;
show warnings;
show columns from stock;
SELECT COUNT(*) AS column_count
FROM information_schema.columns
WHERE table_schema = 'finace' AND table_name = 'stock';
select * from stock order by date_time,stock_id;


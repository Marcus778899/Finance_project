show databases;
create database finace;
use finace;
show tables;

-- 創建table
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

-- 查詢mysql系統參數
show variables like 'secure_file_priv';
SHOW GLOBAL VARIABLES LIKE 'local_infile';
set global local_infile = 'ON';

-- 變更資料結構
ALTER TABLE stock MODIFY COLUMN Trading_money bigint;

-- 匯入資料(太慢了，利用終端機比較快)
LOAD DATA INFILE '/var/lib/mysql-files/0050.csv' INTO TABLE stock
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' ignore 1 lines;
show warnings;

-- 查看標結構及資料
show columns from stock;
SELECT COUNT(*) AS column_count
FROM information_schema.columns
WHERE table_schema = 'finace' AND table_name = 'stock_price';
select * from stock_price 
where 
stock_id = '0050' and
date_time between '2015-01-05' and '2022-10-01' ;  -- 算頭不算尾


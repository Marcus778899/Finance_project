show databases;
create database finace;
use finace;
show tables;

-- 創建table
CREATE TABLE IF NOT EXISTS stock_prcie (
date_time DATE,stock_id VARCHAR(20), 
Trading_Volume INT,
Trading_money INT,
open_price DECIMAL(10, 2),
max DECIMAL(10, 2), 
min DECIMAL(10, 2),
close_price DECIMAL(10, 2),
spread DECIMAL(10, 2),
Trading_turnover INT) ; 
create table if not exists stock_value (
date_time DATE,
stock_id varchar(20),
dividend_yield decimal(10,2),
PER decimal(10,2),
PBR decimal(10, 2)
);

-- 查詢mysql系統參數
show variables like 'secure_file_priv';
SHOW GLOBAL VARIABLES LIKE 'local_infile';
set global local_infile = 'ON';

-- 變更資料結構
ALTER TABLE stock MODIFY COLUMN Trading_money bigint;

-- 聯合主鍵(好用)
ALTER TABLE stock_price
ADD PRIMARY KEY (date_time, stock_id);
ALTER TABLE stock_value
ADD PRIMARY KEY (date_time, stock_id);



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
select * from stock_price limit 10 offset 0;
select * from stock_price limit 10 offset 10;

select count(*) as row_numbers from stock_price;
select count(*) as row_numbers from stock_value;
select * from stock_price
join stock_value 
on stock_price.stock_id = stock_value.stock_id 
and stock_price.date_time = stock_value.date_time
limit 10;


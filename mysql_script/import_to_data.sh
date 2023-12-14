#!/bin/bash
# 啟動腳本前記得先進資料庫確認local_infile有沒有切換成ON
# csv 檔匯入資料庫
# 取得命令行參數
# p表示目標陸路徑
# h表示資料庫位置
# u表示資料庫使用者
# p表示資料庫密碼
# d表示資料庫名稱
# t表示資料表名稱
while getopts ":p:h:u:P:d:t:" opt; do
  case $opt in
    p) dataset_path="$OPTARG"
    ;;
    h) db_host="$OPTARG"
    ;;
    u) db_user="$OPTARG"
    ;;
    P) db_password="$OPTARG"
    ;;
    d) db_name="$OPTARG"
    ;;
    t) table_name="$OPTARG"
    ;;
    \?) echo "Invalid option: -$OPTARG" >&2
    ;;
  esac
done

# 迭代處理所有CSV文件
for file in "$dataset_path"/*.csv; do
    mysql -h "$db_host" -u "$db_user" -p"$db_password" --local-infile=1 "$db_name" -e "LOAD DATA LOCAL INFILE '$file' INTO TABLE $table_name FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;"
done

#coding=utf-8
__author__ = 'Administrator'

from stockInfoCrawler.Frameworks.dlTrans import DownloadTrans
from stockInfoCrawler.Frameworks.MySQL import MySQL
from stockInfoCrawler.Frameworks.Excel import Excel
from datetime import datetime
import os
from os.path import join


def download_excel():
    dt = DownloadTrans()
    dt.download()


def write2db(db_name, trans_path):
    mysql = MySQL(db_name)
    mysql.connect()
    col_type = list()
    col_type.append("`ID` INT NOT NULL AUTO_INCREMENT")
    col_type.append("`DEAL_DATE` DATETIME NULL")
    col_type.append("`DEAL_PRICE` FLOAT NULL")
    col_type.append("`DEAL_GAP` FLOAT NULL")
    col_type.append("`TOTAL_LOT` INT NULL")
    col_type.append("`TOTAL_AMOUNT` INT NULL")
    col_type.append("`DEAL_TYPE` INT NULL")
    col_type.append("`OTHER` FLOAT NULL")
    try:
        for root1, dirs1, files1 in os.walk(trans_path):
            for dir1 in dirs1:
                mysql.create_table(dir1, "ID", col_type)
                next_dir = root1 + "\\" + dir1
                for root2, dirs2, files2 in os.walk(next_dir):
                    for file2 in files2:
                        if file2.find('.txt') != -1:
                            data = list()
                            file_path = join(next_dir, file2)
                            file_name = file2.split(".")[0]
                            with open(file_path, 'r') as fp:
                                text_list = fp.readlines()
                                print "Processing.... " + file_path
                                for i in range(1, len(text_list)):
                                    text = text_list[i].decode('gb2312').encode('utf-8')
                                    text_elem = text.split("\t")
                                    deal_time_str = file_name + ';' + text_elem[0].strip()
                                    deal_time = datetime.strptime(deal_time_str, "%Y-%m-%d;%H:%M:%S")
                                    deal_price = float(text_elem[1].strip())
                                    deal_gap_str = text_elem[2].strip()
                                    if deal_gap_str[len(deal_gap_str) - 1].isdigit():
                                        deal_gap = float(deal_gap_str)
                                    else:
                                        deal_gap = 0
                                    if deal_gap == deal_price:
                                        deal_gap = 0
                                    deal_lot = int(text_elem[3].strip())
                                    deal_amount = int(text_elem[4].strip())
                                    deal_type_str = text_elem[5].strip()
                                    deal_type = 0
                                    if deal_type_str == "买盘":
                                        deal_type = 1
                                    elif deal_type_str == "卖盘":
                                        deal_type = -1
                                    else:
                                        deal_type = 0
                                    data.append([deal_time, deal_price, deal_gap, deal_lot, deal_amount, deal_type])
                            mysql.insert_many(dir1, "`DEAL_DATE`, `DEAL_PRICE`, `DEAL_GAP`, \
                            `TOTAL_LOT`, `TOTAL_AMOUNT`, `DEAL_TYPE`", data)
                        else:
                            continue
    except IOError, e:
        print "ERROR: " + dir1 + " FILE: " + file2
    mysql.close_connect()


if __name__ == '__main__':
    # download_excel()
    write2db("trans", "D:\\txt")
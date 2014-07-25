#coding=utf-8
__author__ = 'Administrator'

from stockInfoCrawler.Frameworks.dlTrans import DownloadTrans
from stockInfoCrawler.Frameworks.MySQL import MySQL
from stockInfoCrawler.Frameworks.Excel import Excel
import datetime
import os
from os.path import join


def download_excel():
    dt = DownloadTrans()
    dt.download()


def write2db(db_name, trans_path):

    for root1, dirs1, files1 in os.walk(trans_path):
        for dir1 in dirs1:
            next_dir = root1 + "\\" + dir1
            for root2, dirs2, files2 in os.walk(next_dir):
                for file2 in files2:
                    if file2.find('.txt') != -1:
                        file_path = join(next_dir, file2)
                        file_name = file2.split(".")[0]
                        with open(file_path, 'r') as fp:
                            text_list = fp.readlines()
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
                                deal_total_one = int(text_elem[3].strip())
                                deal_total_yuan = int(text_elem[4].strip())
                                deal_type_str = text_elem[5].strip()
                                deal_type = 0
                                if deal_type_str == "买盘":
                                    deal_type = 1
                                elif deal_type_str == "卖盘":
                                    deal_type = -1
                                else:
                                    deal_type = 0
                                print deal_time
                                print deal_price
                                print deal_gap
                                print deal_total_one
                                print deal_total_yuan
                                print deal_type
                    else:
                        continue

    # mysql = MySQL()
    # mysql.connect(db_name)


if __name__ == '__main__':
    download_excel()
    # write2db("trans", "D:\\BaiduYunDownload\\ML\\stockInfoCrawler\\stockInfoCrawler\\trans\\test")
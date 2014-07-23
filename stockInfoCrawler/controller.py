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
    excel = Excel()
    for root1, dirs1, files1 in os.walk(trans_path):
        for dir1 in dirs1:
            next_dir = root1 + "\\" + dir1
            for root2, dirs2, files2 in os.walk(next_dir):
                for file2 in files2:
                    if (file2.find('.xls') != -1) or (file2.find('.xlsx') != -1):
                        file_path = join(next_dir, file2)
                        file_name = file2.split('.')[0]
                        excel.open_book(file_path)
                        excel.open_sheet_by_name(file_name)
                        max_col = excel.get_max_col()
                        max_row = excel.get_max_row()
                        print max_col
                        print max_row
                        mat_data = excel.read_block(1, max_row, 0, max_col)
                        print mat_data[0]
                        date_db = datetime.strptime(file_name + ';' + mat_data[0][0], "%Y-%m-%d;%H:%M:%S")
                        print date_db
                    else:
                        continue

    # mysql = MySQL()
    # mysql.connect(db_name)


if __name__ == '__main__':
    download_excel()
    # write2db("trans", "D:\\BaiduYunDownload\\ML\\stockInfoCrawler\\stockInfoCrawler\\trans\\test")
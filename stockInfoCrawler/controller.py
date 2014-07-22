__author__ = 'Administrator'

from stockInfoCrawler.Frameworks.dlTrans import DownloadTrans
from stockInfoCrawler.Frameworks.MySQL import MySQL
from stockInfoCrawler.Frameworks.Excel import Excel
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
                    else:
                        continue

    mysql = MySQL()
    mysql.connect(db_name)



if __name__ == '__main__':
    pass
__author__ = 'Administrator'

from stockInfoCrawler.Frameworks.dlTrans import DownloadTrans
from stockInfoCrawler.Frameworks.MySQL import MySQL
from stockInfoCrawler.Frameworks.Excel import Excel


def download_excel():
    dt = DownloadTrans()
    dt.download()


def write2db(db_name, excel_path):


    mysql = MySQL()
    mysql.connect(db_name)



if __name__ == '__main__':
    pass
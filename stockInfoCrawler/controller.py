__author__ = 'Administrator'

from stockInfoCrawler.Frameworks.dlTrans import DownloadTrans
import stockInfoCrawler.Frameworks.Excel


def download_excel():
    dt = DownloadTrans()
    dt.download()

if __name__ == '__main__':
    pass
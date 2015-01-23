# stockInfoCrawler
__author__ = '80101845'

import threading
import time
import Queue
import urllib, urllib2
from BeautifulSoup import BeautifulSoup

hosts = ["http://www.baidu.com", "http://blog.jobbole.com/",
         "http://blog.csdn.net/songchunyi/article/details/6532276", "http://www.ibm.com/developerworks/cn/aix/library/au-threadingpython/",
         "http://www.ibm.com", "http://www.cnpythoner.com/post/pythonduoxianchen.html"]


host_queue = Queue.Queue()
web_queue = Queue.Queue()


class ThreadUrl(threading.Thread):
    def __init__(self, input_queue, out_queue):
        threading.Thread.__init__(self)
        self.input_queue = input_queue
        self.out_queue = out_queue

    def run(self):
        while True:
            host = self.input_queue.get()
            url = urllib.urlopen(host)
            chunk = url.read()
            self.out_queue.put(chunk)
            self.input_queue.task_done()


class ThreadDataMine(threading.Thread):
    def __init__(self, input_queue):
        threading.Thread.__init__(self)
        self.input_queue = input_queue

    def run(self):
        while True:
            chunk = self.input_queue.get()
            soup = BeautifulSoup(chunk)
            print soup.findAll(['title'])
            self.input_queue.task_done()


if __name__ == '__main__':
    t_url = ThreadUrl(host_queue, web_queue)
    t_url.setDaemon(True)
    t_url.start()

    for host in hosts:
        host_queue.put(host)

    t_web = ThreadDataMine(web_queue)
    t_web.setDaemon(True)
    t_web.start()

    host_queue.join()
    web_queue.join()

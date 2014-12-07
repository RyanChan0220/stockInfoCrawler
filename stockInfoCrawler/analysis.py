__author__ = 'ryan'

from datetime import datetime
from datetime import timedelta
from stockInfoCrawler.Frameworks.MySQL import MySQL
import matplotlib.pyplot as plt


class Analyzer(object):
    def run(self):
        start_date = datetime.strptime('2012-09-26;00:00:00', "%Y-%m-%d;%H:%M:%S")
        end_date = datetime.strptime('2014-09-26;23:59:59', "%Y-%m-%d;%H:%M:%S")
        stock_name = 'sz002410'
        fig = plt.figure()
        ax = fig.gca()
        # self.analysis_deal_price(stock_name, start_date, end_date, ax, 'r')
        self.analysis_close_price(stock_name, start_date, end_date, ax, 'b')
        plt.show()

    def analysis_close_price(self, stock_name, start_date, end_date, ax, color):
        one_day = timedelta(days=1)
        delta_days = (end_date - start_date).days
        mysql = MySQL('daily')
        mysql.connect()
        for day in xrange(0, delta_days, 1):
            query_day = start_date + timedelta(days=day)
            state_where = "DATE = '%s'" % query_day
            data = mysql.query_where(stock_name, state_where)
            if len(data) > 0:
                ax.scatter(query_day, data[0][5], c=color)
            else:
                ax.scatter(query_day, 0, c=color)
        mysql.close_connect()

    def analysis_deal_price(self, stock_name, start_date, end_date, ax, color):
        one_day = timedelta(days=1)
        delta_days = (end_date - start_date).days
        mysql = MySQL('trans')
        mysql.connect()
        for day in xrange(0, delta_days, 1):
            query_day = start_date + timedelta(days=day)
            state_where = "DEAL_DATE > '%s' and DEAL_DATE < '%s'" % (query_day, query_day + one_day)
            data = mysql.query_where(stock_name, state_where)
            ret = self.max_data(data)
            # ax.scatter(query_day, ret, c=color)
            ax.plot(query_day, ret, 'o-', c=color)
        mysql.close_connect()

    def show_data(self, data):
        prices = []
        for index in xrange(len(data)):
            prices.append(int(data[index][2] * 100))
        x_axis = {}
        for price in range(min(prices) - 1, max(prices) + 1, 1):
            x_axis[price] = 0
        for index in xrange(len(prices)):
            x_axis[prices[index]] += data[index][4]
        print x_axis
        fig = plt.figure()
        ax = fig.gca()

        for price in x_axis:
            ax.scatter(price, x_axis[price])
        plt.show()

    def mean_data(self, data):
        gate_amount = 100000
        day_total = 0
        lot_total = 0
        if len(data) > 0:
            for index in xrange(len(data)):
                if data[index][5] > gate_amount:
                    day_total += data[index][5]
                    lot_total += data[index][4]
            mean_total = day_total / lot_total
        else:
            mean_total = 0
        return mean_total / 100

    def max_data(self, data):
        max_amount = 0
        max_lot = 0
        max_price = 0
        if len(data) > 0:
            for index in xrange(len(data)):
                if data[index][5] > max_amount:
                    max_amount = data[index][5]
                    max_lot = data[index][4]
                    max_price = data[index][2]
        else:
            max_price = 0
        return max_price
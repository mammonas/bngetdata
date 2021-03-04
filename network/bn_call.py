import requests
import datetime
import csv
GET_PRICE_ENDPOINT = 'https://binance.com/api/v3/ticker/24hr?symbol='

class BNCall:

    def get_price(self, symbols):
        global highest_perc
        end_point = GET_PRICE_ENDPOINT + symbols
        r = requests.get(end_point)
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        price_current = '%.4f' % float(r.json()['lastPrice'])

        print('%s: %s' %(time_str, price_current))
        with open('%s.csv' % symbols, mode='a') as csv_file:
            employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow([time_str, price_current])

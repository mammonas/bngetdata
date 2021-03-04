import sys
from timeloop import Timeloop
from datetime import timedelta

from network.bn_call import BNCall

tl = Timeloop()
bn_call = BNCall()


# @tl.job(interval=timedelta(seconds=5))
# def execute_cron_job():
#     bn_call.get_price(symbols='BNBUSDT')


if __name__ == "__main__":
    syms = sys.argv[1]

    @tl.job(interval=timedelta(seconds=5))
    def execute_cron_job():
        bn_call.get_price(symbols=syms)

    tl.start(block=True)

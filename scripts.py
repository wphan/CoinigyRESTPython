#!/usr/bin/python

import os
import logging
from logging.config import dictConfig
import click
import timeit
import pandas as pd

from coinigy import CoinigyREST
from collections import namedtuple

logging.basicConfig()
logger = logging.getLogger(__name__)

Credentials = namedtuple('credentials', ('api', 'secret', 'endpoint'))

def find_arbitrage(coinigy):
    start_time = timeit.default_timer()
    exchanges = coinigy.exchanges()#['exch_code']
    # remove non trading excahnges
    exchanges = exchanges[exchanges["exch_trade_enabled"].isin(["1"])]

    # get all the markets
    exch_markets = []
    for exchange in exchanges.itertuples():
        exch_markets.append(coinigy.markets(exchange.exch_code))
    exch_markets.sort(key=lambda x: x.shape[0], reverse=True)

    # find key pairs that are shared between exchanges
    for idx, exchange in enumerate(exch_markets[:-1]):
        for idx_next in list(range(idx + 1, len(exch_markets))):
            # all matches between exch[i] and exch[i+1], returned pd.Series is lenght of exch[i]
            for idx_match, match in ((exchange.mkt_name).isin(exch_markets[idx_next].mkt_name)).iteritems():
                if match:
                    print("{0} is traded in both {1} and {2}".format(exchange.loc[[idx_match]].mkt_name.values[0],
                                                                     exchange.loc[[0]].exch_code.values[0],
                                                                     exch_markets[idx_next].loc[[0]].exch_code.values[0]))

    print("Time elapsed: {0}".format(timeit.default_timer() - start_time))


def test(coinigy):
    print(coinigy.accounts())

@click.command()
@click.option('--arbitrage', is_flag=True, default=False, help="Identify arbitrage opportunities")
def main(arbitrage):
    account = Credentials(
        api=str(os.environ["COINIGY_KEY"]),
        secret=str(os.environ["COINIGY_SECRET"]),
        endpoint="https://api.coinigy.com/api/v1")

    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_columns", 1000)
    pd.set_option("display.max_colwidth", 1000)
    pd.set_option("display.width", 5000)

    coinigy = CoinigyREST(account)

    if arbitrage:
        find_arbitrage(coinigy)
    else:
        test(coinigy)
        print("called with no options")
        exit(1)
    

if __name__ == "__main__":
    main()

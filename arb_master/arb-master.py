import sys
from  getopt import getopt
import logging

import asyncio
import aiohttp

from aiohttp.client_exceptions import ClientError

from api import get_all_depth_binance
from monitoring import check_for_arb


async def main(pairs):
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                while True:
                    orderbooks = await get_all_depth_binance(session, pairs)
                    o = check_for_arb(*orderbooks)
                    cw = o['clockwise']
                    cc = o['counter_clockwise']
                    if cw > 1 or cc > 1:
                        logging.info(f'cw: {cw}, cc: {cc} YES!')
                    else:
                        logging.debug(f'cw: {cw}, cc: {cc} NO D:')
        except ClientError:
            logging.error('Cannot connect to server, creating new session after 10s.')
            await asyncio.sleep(10)


def init(argv):
    log_opts = {'level': logging.INFO, 'filename': 'arbitrage.log', 'format': '%(asctime)s %(levelname)s: %(message)s'}
    opts, args = getopt(argv, '-d', ['logfile='])
    for opt, val in opts:
        if opt == '-d':
            log_opts['level'] = logging.DEBUG
        if opt == '--logfile':
            log_opts['filename'] = val

    logging.basicConfig(level=log_opts['level'], filename=log_opts['filename'], filemode='w', format=log_opts['format'])
#    logging.basicConfig(level=log_opts['level'], format=log_opts['format'])  # replace line above with this to log to stdout
    logging.info('Monitoring for arbitrage opportunities with: {} {} {}'.format(*args))
    logging.debug('Debug is enabled. All query results regardless of profitability will be shown.')
    return args


if __name__ == '__main__':
    pairs = init(sys.argv[1:])
    asyncio.get_event_loop().run_until_complete(main(pairs))

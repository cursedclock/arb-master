
def check_for_arb(ab_orders, cb_orders, ca_orders, volume=0, fee=0.001):
    clockwise = float(ab_orders['bids'][0][0]) / float(cb_orders['asks'][0][0]) * float(ca_orders['bids'][0][0]) * (1-fee)**3
    counter_clockwise = 1/float(ca_orders['asks'][0][0]) * float(cb_orders['bids'][0][0]) / float(ab_orders['asks'][0][0]) * (1-fee)**3

    return {
        'clockwise': clockwise,
        'counter_clockwise': counter_clockwise
    }

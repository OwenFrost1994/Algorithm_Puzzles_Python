import numpy as np
from scipy.stats import norm
from dataclasses import dataclass

class Calculator:
    def add(self, x, y):
        pass

    def subtract(self, x, y):
        pass

    def multiply(self, x, y):
        pass

    def divide(self, x, y):
        pass

    def square(self, x):
        pass

    def root(self, x):
        pass

@dataclass
class Equity:
    spot: float
    dividend_yield: float
    volatility: float
# class Equity():
#     def __init__(self, spot: float, dividend_yield: float, volatility: float):
#         self.spot = spot
#         self.dividend_yield = dividend_yield
#         self.volatility = volatility

@dataclass
class EquityOption:
    strike: float
    time_to_maturity: float
    put_call: str
# class EquityOption():
#     def __init__(self, strike: float, time_to_maturity: float, put_call: str):
#         self.strike = strike
#         self.time_to_maturity = time_to_maturity
#         self.put_call = put_call

@dataclass
class EquityForward:
    strike: float
    time_to_maturity: float
# class EquityForward():
#     def __init__(self, strike: float, time_to_maturity: float):
#         self.strike = strike
#         self.time_to_maturity = time_to_maturity

def bsm_pricer(underlying: Equity, option: EquityOption, rate: float) -> float:
    S = underlying.spot
    K = option.strike
    T = option.time_to_maturity
    q = underlying.dividend_yield
    sigma = underlying.volatility
    r = rate

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option.put_call == "call":
        price =  S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option.put_call == "put":
        price =  K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
    else:
        raise ValueError("Invalid Option Type")

    return price

def bsm_delta(underlying: Equity, option: EquityOption, rate: float) -> float:
    bump = 0.001
    bum_spot_for = underlying.spot * (1 + bump)
    bum_spot_bac = underlying.spot * (1 - bump)

    bum_underlying_for = Equity(bum_spot_for, underlying.dividend_yield, underlying.volatility)
    bum_underlying_bac = Equity(bum_spot_bac, underlying.dividend_yield, underlying.volatility)

    bum_price_for = bsm_pricer(bum_underlying_for, option, rate)
    bum_price_bac = bsm_pricer(bum_underlying_bac, option, rate)

    delta = (bum_price_for - bum_price_bac) / (2 * bump * underlying.spot)
    return delta

def bsm_gamma(underlying: Equity, option: EquityOption, rate: float) -> float:
    bump = 0.001
    bum_spot_for = underlying.spot * (1 + bump)
    bum_spot_bac = underlying.spot * (1 - bump)

    bum_underlying_for = Equity(bum_spot_for, underlying.dividend_yield, underlying.volatility)
    bum_underlying_bac = Equity(bum_spot_bac, underlying.dividend_yield, underlying.volatility)

    ori_price = bsm_pricer(underlying, option, rate)
    bum_price_for = bsm_pricer(bum_underlying_for, option, rate)
    bum_price_bac = bsm_pricer(bum_underlying_bac, option, rate)

    gamma = (bum_price_for - 2 * ori_price + bum_price_bac) / (bump * underlying.spot) ** 2
    return gamma

def fwd_pricer(underlying: Equity, option: EquityForward, rate: float):
    S = underlying.spot
    K = option.strike
    T = option.time_to_maturity
    q = underlying.dividend_yield
    r = rate
    
    price = S * np.exp((r - q) * T) - K
    return price
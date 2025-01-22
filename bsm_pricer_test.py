from bsm_pricer import Equity, EquityOption, EquityForward, bsm_pricer, bsm_delta, bsm_gamma, fwd_pricer

print(bsm_pricer(Equity(4450, 0.015, 0.15), EquityOption(4700, 0.25, "call"), 0.055))
print(bsm_pricer(Equity(4450, 0.0, 0.15), EquityOption(1e-16, 0.25, "call"), 0.0))
print(bsm_pricer(Equity(4450, 0.0, 1e-9), EquityOption(5000, 0.25, "put"), 0.0))

print(bsm_delta(Equity(4450, 0.015, 0.15), EquityOption(4700, 0.25, "call"), 0.055))
print(bsm_delta(Equity(4450, 0.0, 0.15), EquityOption(1e-16, 0.25, "call"), 0.0))
print(bsm_delta(Equity(4450, 0.0, 1e-9), EquityOption(5000, 0.25, "put"), 0.0))

print(bsm_gamma(Equity(4450, 0.015, 0.15), EquityOption(4700, 0.25, "call"), 0.055))
print(bsm_gamma(Equity(4450, 0.0, 0.15), EquityOption(1e-16, 0.25, "call"), 0.0))
print(bsm_gamma(Equity(4450, 0.0, 1e-9), EquityOption(5000, 0.25, "put"), 0.0))
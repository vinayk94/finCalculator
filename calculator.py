import argparse

def payment(pv, rate, n):
    """Calculate payment for an ordinary annuity given present value, rate, and number of periods."""
    if n <= 0:
        raise ValueError("Number of periods must be greater than 0.")
    if rate <= 0:
        return pv / n
    pmt = pv * rate / (1 - (1 + rate) ** -n)
    return pmt

def future_value(pv, rate, n):
    """Calculate future value for given present value, rate, and number of periods."""
    fv = pv * ((1 + rate) ** n)
    return fv

def present_value(fv, rate, n):
    """Calculate present value for a given future value, rate, and number of periods."""
    pv = fv / ((1 + rate) ** n)
    return pv

def net_present_value(rate, cash_flows):
    """Calculate the Net Present Value of a series of cash flows given a discount rate."""
    npv = sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cash_flows))
    return npv

def derivative_of_npv(rate, cash_flows, h):
    """Calculate the derivative of the NPV function for use in the IRR calculation."""
    return (net_present_value(rate + h, cash_flows) - net_present_value(rate - h, cash_flows)) / (2 * h)


def internal_rate_of_return(cash_flows, guess=0.1):
    """Calculate the Internal Rate of Return of a series of cash flows."""
    if not cash_flows or cash_flows[0] >= 0:
        raise ValueError("Cash flows must start with a negative value (outflow).")
    step = 0.0001
    epsilon = 0.0001
    limit = 10000
    iteration = 0
    rate = guess

    while iteration < limit:
        npv = net_present_value(rate, cash_flows)
        derivative = derivative_of_npv(rate, cash_flows, step)
        if derivative == 0:
            raise ValueError("NPV derivative is zero, cannot continue iteration.")
        iteration += 1
        rate -= (npv / derivative)
        if abs(npv) < epsilon:
            return rate

    raise ValueError("IRR not converging with these cash flows and the initial guess provided.")

def main():
    parser = argparse.ArgumentParser(description="Financial Calculator")
    parser.add_argument('--future_value', action='store_true', help='Calculate future value')
    parser.add_argument('--present_value', action='store_true', help='Calculate present value')
    parser.add_argument('--payment', action='store_true', help='Calculate payment')
    parser.add_argument('--npv', action='store_true', help='Calculate NPV')
    parser.add_argument('--irr', action='store_true', help='Calculate IRR')
    parser.add_argument('--pv', type=float, help='Present value', default=0)
    parser.add_argument('--rate', type=float, help='Interest rate', default=0)
    parser.add_argument('--n', type=int, help='Number of periods', default=0)
    parser.add_argument('--fv', type=float, help='Future value', default=0)
    parser.add_argument('--cash_flows', nargs='+', type=float, help='List of cash flows', default=[])

    args = parser.parse_args()

    if args.future_value:
        print(future_value(args.pv, args.rate, args.n))
    elif args.present_value:
        print(present_value(args.fv, args.rate, args.n))
    elif args.payment:
        print(payment(args.pv, args.rate, args.n))
    elif args.npv:
        print(net_present_value(args.rate, args.cash_flows))
    elif args.irr:
        print(internal_rate_of_return(args.cash_flows))
    else:
        print("No valid calculation type provided.")

if __name__ == '__main__':
    main()
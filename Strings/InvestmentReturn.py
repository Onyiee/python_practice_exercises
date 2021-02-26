# (7% Investment Return) Some investment advisors say that it’s reasonable to expect a 7%
# return over the long term in the stock market. Assuming that you begin with
# $1000 and leave your money invested, calculate and display how much money you’ll have
# after 10, 20 and 30 years. Use the following formula for determining these amounts:
# a = p(1 + r)
# n
# where
# p is the original amount invested (i.e., the principal of $1000),
# r is the annual rate of return (7%),
# n is the number of years (10, 20 or 30) and
# a is the amount on deposit at the end of the nth year

def calculate_investment_return(p: float, r: float, n: float):
    """
     p - principal:
    r - rate [0 -> 1
    n - number of years
    :returns the investment return according to the expression  [p* (1 + r) ** n
    """
    return p * (1 + r) ** n


def main():
    p_given = 1000
    r_given = 7 / 100
    years_given = [10, 20, 30]

    for year in years_given:
        inv_returns = calculate_investment_return(p_given, r_given, year)
        print(f"year = {year}, return = {inv_returns:.2f}")


if __name__ == '__main__':
    main()

    # a = p * (1 + r) ** year
    # print(f"year = {year}, a = {a:.2f}")

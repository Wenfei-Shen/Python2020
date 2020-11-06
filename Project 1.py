import numpy as np

# Set up the default_rng from Numpy
rng = np.random.default_rng()

# Make a function for the news
def news(chance, volatility):
    '''
    This function models randomly occurring news and its impact on the stock price.
    :param chance: The possibility of the news happening
    :param volatility: The volatility of a given stock
    :return: the impact of the news
    '''
    # Choose whether there's news today
    news_today = rng.choice([0, 1], p=[1-chance, chance])
    # If news occurs today
    if news_today == 1:
        # Calculate m which is subject to N(0,4)
        m = rng.normal(0, 2)
        # Calculate drift which is proportional ro volatility
        drift = m * volatility
        # Randomly choose the duration which is subject to U{3, 14}
        duration = rng.integers(3, 14)
        # Calculate the impact of news
        news_impact = [drift] * duration
    # If news does not occur today
    else:
        news_impact = [0]
    # return the impact of the news
    return news_impact


def generate_stock_price(days, initial_price, volatility):
    '''
    This function gives simulated stock price over a period of time
    :param days: the given time period
    :param initial_price: the given initial price
    :param volatility: the given volatility of the stock
    :return: simulated stock price
    '''
    # Set stock_prices to be a zero array with length days
    stock_prices = np.zeros(days)
    # Set stock_prices in row 0 to be initial_price
    stock_prices[0] = initial_price
    # Set total_drift to be a zero array with length days
    totalDrift= np.zeros(days)
    # Loop over a range(1, days)
    for day in range(1, days):
        # Get the random normal increment
        inc = rng.normal(0, volatility)
        # Add stock_prices[day-1] to inc to get NewPriceToday
        NewPriceToday = stock_prices[day-1] + inc
        # Get the drift from the news
        d = news(0.5, volatility)
        # Get the duration
        duration = len(d)
        # Decide whether the duration is longer then the left time
        if duration <= (days-day):
            totalDrift[day:day+duration] += d
        else:
            totalDrift[day:days] += d[0:(days-day)]
        # Add today's drift to today's price
        NewPriceToday += totalDrift[day]
        # Set stock_prices[day] to NewPriceToday or to NaN if it's negative
        if NewPriceToday <= 0:
            stock_prices[day] = np.nan
        else:
            stock_prices[day] = NewPriceToday

    return stock_prices


print(generate_stock_price(6, 1, 1))


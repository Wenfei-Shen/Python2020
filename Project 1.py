import numpy as np
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
        m = rng.normal(0, 4)
        # Calculate drift which is proportional ro volatility
        drift = m * volatility
        # Randomly choose the duration which is subject to U{3, 14}
        duration = rng.integers(3, 14)
        # Calculate the impact of news
        news_impact = [drift] * duration
    # If news does not occur today
    else:
        news_impact = [0]

    return news_impact


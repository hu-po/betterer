""" Fermi Problem for startup investing. """

import matplotlib.pyplot as plt
import numpy as np

import random
from typing import List, Dict, Tuple, Union, Optional


def one_year_sp500(capital: float, year: int) -> float:

    # https://www.dontworkanotherday.com/average-etf-return
    ROIC_per_year = {
        '2010': 0.1278,
        '2011': 0.0,
        '2012': 0.1341,
        '2013': 0.296,
        '2014': 0.1139,
        '2015': -0.0073,
        '2016': 0.0954,
        '2017': 0.1942,
        '2018': -0.0624,
        '2019': 0.2888,
        '2020': 0.1626,
    }

    # Randomly select a year
    return_year = random.choice(list(ROIC_per_year.keys()))
    # print(f'The S&P500 in {year} returned: {ROIC_per_year[return_year]}%')

    # Calculate the return
    eoy_capital = capital * (1 + ROIC_per_year[return_year])
    # print(f'Your index fund investment of {capital:.2f} is now {eoy_capital:.2f}')

    return eoy_capital


def multi_year_sp500(capital: float, num_years: int, new_capital: float) -> float:

    # Total capital invested
    capital_in = capital + (new_capital * num_years)

    for year in range(num_years):
        capital += new_capital
        capital = one_year_sp500(capital, year)

    # print(f'The value of your capital in the SP500 is {capital:.2f}')

    # The total return on investment
    roi = (capital - capital_in) / capital_in

    # print(f'The ROI on your investment is {roi:.2f}%')
    return roi


def multi_year_startup(capital: float, num_year: int, name: str = 'Startuply') -> float:

    # Chance that startup fails and you lose all your money
    failure_chance: Dict[int, float] = {
        0: 0.30,
        1: 0.50,
        2: 0.50,
        3: 0.20,
        4: 0.20,
        5: 0.20,
        6: 0.05,
        7: 0.05,
        8: 0.05,
        9: 0.05,
        10: 0.05,
    }

    # Growth rate of the startup per year of life
    growth_rate: Dict[int, float] = {
        0: random.uniform(0.68, 1.60),
        1: random.uniform(0.45, 0.93),
        2: random.uniform(0.68, 0.80),
        3: random.uniform(0.10, 0.50),
        4: random.uniform(0.05, 0.40),
        5: random.uniform(-0.1, 0.40),
        6: random.uniform(-0.1, 0.20),
        7: random.uniform(-0.1, 0.20),
        8: random.uniform(-0.1, 0.20),
        9: random.uniform(-0.1, 0.20),
    }

    # Value of investment at the end of the year
    for year in range(num_years):
        if random.random() < failure_chance[year]:
            # print(f'Your startup {name} failed in year {year}')
            return 0

        # Calcualte the return
        capital = capital * (1 + growth_rate[year])
        # print(f'Your startup {name} grew by {growth_rate[year]*100:.1f}% in year {year}, your investment is now {capital:.2f}')

    # Make it to the end
    # print(f'Your startup {name} made it to the end of the simulation, your investment is now {capital:.2f}')
    return capital


def startup_name_generator() -> str:

    for name in [
        'Juicero',
        'Opty',
        'Ephermal',
        'Toolio',
        'Blink',
        'Pebble',
        'Klout',
        'Gawker',
        'Myspace',
        'Groupon',
        'Zynga',
        'Dropbox',
        'Instagram',
        'Snapchat',
        'Uber',
    ]:
        yield name


def multi_year_multi_startup(capital: float, num_years: int, new_capital: float) -> float:

    # Total capital invested
    capital_in = capital + (new_capital * num_years)

    # Invest in 3 startups to begin with
    total_startups = 3
    investment_per_startup = capital / total_startups

    startup_name = startup_name_generator()

    # Initial investments
    capital += multi_year_startup(investment_per_startup,
                                  num_years, name=next(startup_name))
    capital += multi_year_startup(investment_per_startup,
                                  num_years, name=next(startup_name))
    capital += multi_year_startup(investment_per_startup,
                                  num_years, name=next(startup_name))

    # Additional investments every year
    for year in range(num_years):
        capital += multi_year_startup(new_capital,
                                      (num_years - year), name=next(startup_name))

    # print(f'The value of your capital in the startups is {capital:.2f}')

    # The total return on investment
    roi = (capital - capital_in) / capital_in

    # print(f'The ROI on your investment is {roi:.2f}%')

    return roi


if __name__ == '__main__':

    # Set the initial capital
    start_capital = 100000

    # How much are you investing per year
    new_capital = 10000

    # Total number of years to run the simulation
    num_years = 10

    # Run the simulation with the sp500
    sp500_capital = multi_year_sp500(start_capital, num_years, new_capital)

    # Run the simulation with the startup
    startup_capital = multi_year_multi_startup(
        start_capital, num_years, new_capital)

    # Run the simulation 100 times
    sp500_capital_list = []
    startup_capital_list = []
    for i in range(1000):
        sp500_capital_list.append(multi_year_sp500(
            start_capital, num_years, new_capital))
        startup_capital_list.append(multi_year_multi_startup(
            start_capital, num_years, new_capital))

    # Plot the results
    plt.hist(sp500_capital_list, bins=20, alpha=0.5, label='S&P500')
    plt.hist(startup_capital_list, bins=20, alpha=0.5, label='Startups')
    plt.legend(loc='upper right')
    plt.title(f'ROI after {num_years} years')
    plt.xlabel('ROI')
    plt.ylabel('Frequency')
    plt.show()

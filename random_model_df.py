import numpy as np
import random
import pandas as pd
pd.set_option('display.float_format', '{:.2f}'.format)

class Risk:
    risk_started_amount = 50
    first_n_losses = 9
    rr = 2

    def total_drawdown(self, x):
        total_drawdown = 0
        for i in range(self.first_n_losses):
            total_drawdown = total_drawdown + self.risk_started_amount * x**i
        return total_drawdown

    def find_optimal_x(self):
        min_diff = float('inf')
        optimal_x = 1
        for x in np.arange(1, 2, 0.001):
            cumulative_losses = self.total_drawdown(x)
            target_risk_amount_10th_trade = (1.3 * cumulative_losses) / self.rr
            risk_amount_10th_trade = self.risk_started_amount * x**self.first_n_losses
            diff = abs(risk_amount_10th_trade - target_risk_amount_10th_trade)
            if diff < min_diff:
                min_diff = diff
                optimal_x = x
        return optimal_x

    def create_results_df(self, optimal_x, start_trade=1, end_trade=first_n_losses+1):
        results = []
        for winning_trade in range(start_trade, end_trade + 1):
            cases = [self.risk_started_amount * optimal_x**i for i in range(self.first_n_losses)]
            cum_loss = sum(cases[:winning_trade - 1])
            risk_amount_winning_trade = self.risk_started_amount * optimal_x**(winning_trade - 1)
            win_amount = risk_amount_winning_trade * self.rr
            total_profit = win_amount - cum_loss
            results.append([winning_trade, risk_amount_winning_trade, win_amount, cum_loss, total_profit])

        results_df = pd.DataFrame(results, columns=['Winning Trade', 'Risk Amount', 'Winning Amount', 'Cumulative Loss', 'Total Profit'])
        return results_df



risk = Risk()
optimal_x = risk.find_optimal_x()
print(optimal_x)
results_df = risk.create_results_df(optimal_x)  # Change the range here
print(results_df)

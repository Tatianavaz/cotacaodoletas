# Caio Anchesqui
# https://www.mql5.com/hfttiradentes

from ctypes import _NamedFuncPointer
from datetime import datetime


# import random
import threading
import time

class HighFrequencyTrader:
    def _init_(self, start_price):
        self.starting_price = start_price
        self.running = True
        self.lock = threading.Lock()
        self.execution_thread = threading.Thread(target=self.execute_trades)
        self.execution_thread.start()

    def stop(self):
        self.running = False
        self.execution_thread.join()

    def execute_trades(self):
        while self.running:
            with self.lock:
                min_price = self.starting_price
                max_price = self.starting_price
                price = self.starting_price

                print("XAU/USD Price Range:", min_price, "-", max_price)
                print("XAU/USD Current Price:", price)

                grid_spacing = 5
                min_grid_distance = 10
                take_profit = 30

                for level in range(int(min_price), int(max_price), grid_spacing):
                    if price < level:
                        take_profit += 10
                        take_profit = min(take_profit, price + max_take_profit_pips)

                        stop_loss = max(level - 10, price - 10)
                        stop_loss = max(stop_loss, price - max_stop_loss_pips)

                        while abs(level - price) < min_grid_distance:
                            level += grid_spacing

                        self.execute_order("XAUUSD", "buy", 1, level, take_profit, stop_loss)
                    elif price > level + grid_spacing:
                        take_profit += 10
                        take_profit = min(take_profit, price - max_take_profit_pips)

                        stop_loss = min(level + 10, price + 10)
                        stop_loss = min(stop_loss, price + max_stop_loss_pips)

                        while abs(level - price) < min_grid_distance:
                            level -= grid_spacing

                        self.execute_order("XAUUSD", "sell", 1, level + grid_spacing, take_profit, stop_loss)

            time.sleep(execution_delay_ms / 1000)

    def execute_order(self, symbol, action, quantity, entry_price, take_profit, stop_loss):
        print(f"Order executed: {action} {quantity} {symbol} at {entry_price}")
        print(f"Take Profit: {take_profit}, Stop Loss: {stop_loss}")

if _NamedFuncPointer == "_main_":
    starting_price = 1735.0  # Defina o preço inicial conforme necessário
    max_take_profit_pips = 100
    max_stop_loss_pips = 80
    execution_delay_ms = 10
    runtime_seconds = 60

    hft_robot = HighFrequencyTrader(starting_price)

    try:
        time.sleep(runtime_seconds)
    finally:
        hft_robot.stop()

#
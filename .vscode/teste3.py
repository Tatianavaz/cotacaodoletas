import dataclasses
import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta
import time 

mt5.initialize()
symbol = "WINV22"
lot = 1.0

while True:
 Data = pd.DataFrame(mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 90))
 Data['time'] = pd.to_datetime(Data['time'], unit = "s")
 Data['mm9'] = Data.ta.sma(9)

 media = (list(Data['mm9'])(-1))
 fechamento = (list(Data['close'])[-1])

 # print(Data)
 print(media)
 print(fechamento)
 print("")



 if(fechamento > media):
  print('Pode comprar')
 elif(fechamento < media):
  print('Fehar a posição')
 else:
  print('esperar')


  time.sleep(20)


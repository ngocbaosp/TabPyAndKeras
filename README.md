# TabPy and Keras
TabPy does not support Keras directly, so we will
 - Create an api (getStockPrice) to work with Keras model (api/api.py)
 - Create and deploy a StockPricePredictApiOneCall function to TabPy server. This function will call the getStockPrice api directly
## Install & Configure TabPy
https://github.com/ngocbaosp/TabPyAndKeras/blob/main/Install.md
## View Demo workbook
- Open project in python IDE (ex: Pycharm)
- Run api/api.py
- Run notebook/LSTMStock.ipynb to check the getStockPrice api
- Open workbook/TestTabpyFunction.twb in Tableau Desktop to see the result (the workbook will call the StockPricePredictApiOneCall function in the calculated field script) 
## Ref
- https://github.com/tableau/TabPy/issues/120

# TabPy and Keras
TabPy does not support Keras directly, so we will
 - Create an api to load Keras model (api/api.py)
 - Create and deploy the StockPricePredictApiOneCall function to TabPy server. This function will call the the getStockPrice api 
## Install & Configure TabPy
https://github.com/ngocbaosp/TabPyAndKeras/blob/main/Install.md
## View Demo workbook
- Open project in python IDE (ex: Pycharm)
- Run api/api.py
- Run notebook/LSTMStock.ipynb to check the getStockPrice api
- Open workbook/TestTabpyFunction.twb in Tableau Desktop to see the result (call the StockPricePredictApiOneCall function in the calculated field script) 
## Ref
- https://github.com/tableau/TabPy/issues/120

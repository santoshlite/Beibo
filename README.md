# The Oracle, predict the stock market 💸

<br/>
<br/>

<p align="center">
  <img height="150" src="https://user-images.githubusercontent.com/61618641/147692854-f7001d42-9dca-414c-9301-819389729c43.png" alt="The Oracle logo")
</p>

<br/>
<br/>
  
**The Oracle** is a **Python** library that uses several **prediction models** to predict **stocks returns** over a defined period of time.
  
_Disclaimer: Information is provided 'as is' and solely for informational purposes, not for trading purposes or advice._



## How to install 📥

```py
pip install the-oracle
```
  
## How to use ⚙️

  
```py
from the_oracle import oracle
  
oracle(
      portfolio=["TSLA", "AAPL", "NVDA", "NFLX,], #stocks you want to predict
      start_date = "2020-01-01", #date from which it will take data to predict
      weights = [0.3, 0.2, 0.3, 0.2], #allocate 30% to TSLA and 20% to AAPL... (equal weighting  by default)
      prediction_days=30 #number of days you want to predict
)
  
```

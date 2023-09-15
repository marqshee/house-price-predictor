# House Price Prediction API
Predicts the house price based on key features.

## Data Analysis Takeaways
- Split data to prevent snooping.
- Explore data:
    - Check data types.
    - Missing values.
    - User error values / general incorrect values like `??`
    - Use [seaborn](https://seaborn.pydata.org/index.html) and [matplotlib](https://matplotlib.org/) to visualize data.
    - drop extreme outliers
    - Num / Num analysis
    - Cat / Num analysis
- Build preprocessor
    - Preprocess test / train data
- Create training pipelines
    - [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
    - [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
    - [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)
    - [XGBRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)
- Tune hyper-parameters

## Pickle
Used for saving the best model. GB gave our best model and is stored in this directly as `gb.pkl`.

## FastApi
[FastApi](https://fastapi.tiangolo.com/) is a web framework for making quick apis.

## Pydantic
[Pydantic](https://docs.pydantic.dev/latest/) helps with type checking validation.

## Uvicorn
[Uvicorn](https://www.uvicorn.org/) 

## Postman
There are other ways to test the API, but [Postman](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html) is my prefered way.

## Heroku
Host the API. Must have `git` installed. Requires `runtime.txt`, `requirements.txt` and `Procfile` file.

```
heroku login
heroku create
git push heroku master
```

Not longer a free service, so sad...

## How to see a prediction
In `app` directory run `uvicorn api:app --reload` to start the web server.

Use Postman:
POST `http://127.0.0.1:8000`

body:
`{
    "TransactionDate":"2020.12",
    "HouseAge":17.0,
    "DistanceToStation":467.6447748,
    "NumberOfPubs":4.0,
    "PostCode":"5222.0"
}`



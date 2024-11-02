import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error

def visualize_passenger_flow(daily_passengers):
    #визуал поток людей
    plt.figure(figsize=(10, 5))
    plt.plot(daily_passengers.index, daily_passengers['passenger_count'], label="Actual data")
    plt.xlabel("Date")
    plt.ylabel("Passenger count")
    plt.title("Daily Passenger Flow")
    plt.legend()
    plt.show()

    #считание сред
    daily_passengers['moving_average'] = daily_passengers['passenger_count'].rolling(window=7).mean()

    #визуал средн
    plt.figure(figsize=(10, 5))
    plt.plot(daily_passengers.index, daily_passengers['passenger_count'], label="Actual data")
    plt.plot(daily_passengers.index, daily_passengers['moving_average'], label="7-Day Moving Average", color="orange")
    plt.xlabel("Date")
    plt.ylabel("Passenger count")
    plt.title("Passenger Flow with Moving Average")
    plt.legend()
    plt.show()

def visualize_forecast_with_regression(daily_passengers, forecast):
    # График с предсказанием
    plt.figure(figsize=(10, 5))
    plt.plot(daily_passengers.index, daily_passengers['passenger_count'], label="Actual data")
    plt.plot(daily_passengers.index, daily_passengers['moving_average'], label="7-Day Moving Average", color="orange")
    plt.plot(forecast.index, forecast['forecast'], label="Forecast", color="red", linestyle="--")
    plt.xlabel("Date")
    plt.ylabel("Passenger count")
    plt.title("Passenger Flow Forecast")
    plt.legend()
    plt.show()

    # Линейная регрессия
    daily_passengers.reset_index(inplace=True)
    X = daily_passengers.index.values.reshape(-1, 1)
    y = daily_passengers['passenger_count'].values

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Вычисление метрик
    rmse = root_mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    # График регрессии
    plt.figure(figsize=(10, 5))
    plt.scatter(daily_passengers.index, daily_passengers['passenger_count'], label="Actual data", color="blue")
    plt.plot(daily_passengers.index, y_pred, color="green", label="Linear Regression")
    plt.xlabel("Date")
    plt.ylabel("Passenger count")
    plt.title(f"Linear Regression Fit (RMSE: {rmse:.2f}, R2: {r2:.2f})")
    plt.legend()
    plt.show()
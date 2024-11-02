import pandas as pd

def forecast_passenger_flow(daily_passengers):
    # предсказание на средн
    last_date = daily_passengers.index[-1]
    forecast_dates = pd.date_range(last_date, periods=7, freq='D')
    last_avg = daily_passengers['moving_average'].iloc[-1]

    # создание DataFrame для предсказ
    forecast = pd.DataFrame({'date': forecast_dates, 'forecast': last_avg})
    forecast.set_index('date', inplace=True)

    return forecast

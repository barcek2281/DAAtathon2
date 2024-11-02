import matplotlib.pyplot as plt
import data_loader
import data_processing
import visualization
import forecasting

def main():
    #загрузка данных
    data = data_loader.load_data("bus_bts.csv")

    daily_passengers = data_processing.process_data(data)
    if daily_passengers is None:
        return

    #визуализация потока пасс
    visualization.visualize_passenger_flow(daily_passengers)

    #форкаст потока пасс
    forecast = forecasting.forecast_passenger_flow(daily_passengers)

    #визуализация форкаста
    plt.figure(figsize=(10, 5))
    plt.plot(daily_passengers.index, daily_passengers['passenger_count'], label="Actual data")
    plt.plot(daily_passengers.index, daily_passengers['moving_average'], label="7-Day Moving Average", color="orange")
    plt.plot(forecast.index, forecast['forecast'], label="Forecast", color="red", linestyle="--")
    plt.xlabel("Date")
    plt.ylabel("Passenger count")
    plt.title("Passenger Flow Forecast")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

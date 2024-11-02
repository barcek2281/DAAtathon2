import matplotlib.pyplot as plt

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

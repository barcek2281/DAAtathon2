import pandas as pd
def process_data(data):
    # уникальные значения в get on_time
    print("Unique geton_time values:", data['geton_time'].unique())

    # regex pattern for HH:MM:SS format
    data = data[data['geton_time'].str.match(r'^\d{1,2}:\d{2}:\d{2}$')]  # Keep only valid HH:MM:SS format

    # размер фрейма данных после фильтрации
    print("Filtered data size:", data.shape)

    # остались действительные записи
    if data.empty:
        print("No valid entries in geton_time after filtering.")
        return None

    #time strings -> hours
    data['geton_hour'] = pd.to_datetime(data['geton_time'], format='%H:%M:%S').dt.hour
    data['getoff_hour'] = pd.to_datetime(data['getoff_time'], format='%H:%M:%S', errors='coerce').dt.hour

    #aggregate data by date
    daily_passengers = data.groupby('geton_date')['user_card_id'].nunique().reset_index()
    daily_passengers.rename(columns={'user_card_id': 'passenger_count'}, inplace=True)
    daily_passengers.set_index('geton_date', inplace=True)

    # есть ли у daily_passengers данные
    print("Daily passengers data:", daily_passengers)

    return daily_passengers

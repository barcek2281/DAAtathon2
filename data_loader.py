import pandas as pd

def load_data(filename):
    # загрузка данных
    data = pd.read_csv(filename)

    #date columns -> datetime
    data['geton_date'] = pd.to_datetime(data['geton_date'])
    data['getoff_date'] = pd.to_datetime(data['getoff_date'])

    #Очистка тайм данные, чтобы удалить нач. и конеч пробелы
    data['geton_time'] = data['geton_time'].str.strip()
    data['getoff_time'] = data['getoff_time'].str.strip()

    return data

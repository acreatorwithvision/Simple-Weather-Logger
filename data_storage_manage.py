class DataStorageManager:
    def __init__(self):
        self.weather_data = []  # List to store weather records.

    def add_record(self, record):
        self.weather_data.append(record)

    def get_all_records(self):
        return self.weather_data

    def get_records_by_city(self, city):
        # Filter and return records for a specific city.
        return [record for record in self.weather_data if record["city"].lower() == city.lower()]

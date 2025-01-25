class WeatherCollector:
    def __init__(self, storage_manager):
        self.storage_manager = storage_manager

    def add_weather_data(self, city, temperature, humidity, description):
        # Create a weather record.
        record = {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "description": description
        }
        self.storage_manager.add_record(record)
        return f"Weather data for '{city}' added."

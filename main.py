from weather_collector import WeatherCollector
from data_storage_manager import DataStorageManager
from analysis_system import AnalysisSystem

def main():
    # Initialize components.
    storage_manager = DataStorageManager()
    collector = WeatherCollector(storage_manager)
    analysis = AnalysisSystem()

    # Add weather data.
    print(collector.add_weather_data("New York", 25, 60, "Sunny"))
    print(collector.add_weather_data("Los Angeles", 28, 50, "Clear"))
    print(collector.add_weather_data("New York", 22, 65, "Cloudy"))
    print(collector.add_weather_data("Chicago", 18, 70, "Rainy"))

    # Display all weather records.
    print("\nAll Weather Data:")
    for record in storage_manager.get_all_records():
        print(record)

    # Perform analysis.
    city = "New York"
    city_records = storage_manager.get_records_by_city(city)
    print(f"\nAnalysis for {city}:")
    print(f"Average Temperature: {analysis.calculate_average_temperature(city_records):.2f}°C")
    print(analysis.find_highest_temperature(city_records))
    print(analysis.find_lowest_temperature(city_records))

    # Overall analysis.
    print("\nOverall Analysis:")
    print(f"Average Temperature: {analysis.calculate_average_temperature(storage_manager.get_all_records()):.2f}°C")
    print(analysis.find_highest_temperature(storage_manager.get_all_records()))
    print(analysis.find_lowest_temperature(storage_manager.get_all_records()))

if __name__ == "__main__":
    main()

class AnalysisSystem:
    def calculate_average_temperature(self, records):
        if not records:
            return "No data available for analysis."
        total_temp = sum(record["temperature"] for record in records)
        return total_temp / len(records)

    def find_highest_temperature(self, records):
        if not records:
            return "No data available for analysis."
        highest = max(records, key=lambda r: r["temperature"])
        return f"Highest temperature: {highest['temperature']}°C in {highest['city']}."

    def find_lowest_temperature(self, records):
        if not records:
            return "No data available for analysis."
        lowest = min(records, key=lambda r: r["temperature"])
        return f"Lowest temperature: {lowest['temperature']}°C in {lowest['city']}."

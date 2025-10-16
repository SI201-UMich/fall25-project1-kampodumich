#Name: Kamila Podsiadlo
# Student ID: [Your ID]
# Email: kampod@umich.edu
# Collaborators: Ava Anderson, Luther Hoy, and generative AI (ChatGPT, DeepAI)
#
# Function Authorship:
# Kamila: avg_yield_maize_north_temp_range, percentage_maize_east_high_rainfall
# Ava: avg_yield_temp_range_west, percentage_wheat_high_yield_south
# Luther: avg_rainfall_east_high_yield, most_frequent_crop_high_yield_rain
# All: def main():, read_csv, write_results_to_txt, mock and edge cases (collaborative)

import csv
import os

def read_csv(filename):
    """
    Reads a CSV file (located in the same folder as this script)
    and returns a list of dictionaries.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    if not os.path.exists(filepath):
        print(f" File not found: {filepath}")
        return []

    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Kamila's calculations
def avg_yield_maize_north_temp_range(data):
    """
    Kamila: Average yield for Maize in North region with temperature 15-25 C.
    Uses: Crop, Region, Temperature_Celsius, Yield_tons_per_hectare
    """
    filtered = [
        row for row in data
        if row['Crop'] == 'Maize'
        and row['Region'] == 'North'
        and row['Temperature_Celsius'] and 15 <= float(row['Temperature_Celsius']) <= 25
        and row['Yield_tons_per_hectare']
    ]
    if not filtered:
        return 0
    total_yield = sum(float(row['Yield_tons_per_hectare']) for row in filtered)
    return total_yield / len(filtered)
def percentage_maize_east_high_rainfall(data):
    """
    Kamila: % of crops in East region that are Maize with rainfall > 700mm.
    Uses: Crop, Region, Rainfall_mm
    """
    filtered = [
        row for row in data
        if row['Region'] == 'East' and row['Rainfall_mm'] and float(row['Rainfall_mm']) > 700
    ]
    if not filtered:
        return 0
    maize_count = sum(1 for row in filtered if row['Crop'] == 'Maize')
    return (maize_count / len(filtered)) * 100
# Ava's calculations
def avg_yield_temp_range_west(data):
    """
    Ava: Average yield in West region where temperature is between 15–25°C.
    Uses: Region, Temperature_Celsius, Yield_tons_per_hectare
    """
    filtered = [
        row for row in data
        if row['Region'] == 'West'
        and row['Temperature_Celsius'] and 15 <= float(row['Temperature_Celsius']) <= 25
        and row['Yield_tons_per_hectare']
    ]
    if not filtered:
        return 0
    total_yield = sum(float(row['Yield_tons_per_hectare']) for row in filtered)
    return total_yield / len(filtered)

def percentage_wheat_high_yield_south(data):
    """
    Ava: % of Wheat crops in South region with yield > 3.0 tons/hectare.
    Uses: Crop, Region, Yield_tons_per_hectare
    """
    filtered = [
        row for row in data
        if row['Region'] == 'South'
        and row['Crop'] == 'Wheat'
        and row['Yield_tons_per_hectare']
    ]
    if not filtered:
        return 0
    high_yield_count = sum(1 for row in filtered if float(row['Yield_tons_per_hectare']) > 3)
    return (high_yield_count / len(filtered)) * 100
# Luther's calculations
def avg_rainfall_east_high_yield(data):
    """
    Luther: Average rainfall in East region where yield > 3.5 tons/hectare.
    Uses: Region, Yield_tons_per_hectare, Rainfall_mm
    """
    filtered = [
        row for row in data
        if row['Region'] == 'East'
        and row['Yield_tons_per_hectare'] and float(row['Yield_tons_per_hectare']) > 3.5
        and row['Rainfall_mm']
    ]
    if not filtered:
        return 0
    total_rainfall = sum(float(row['Rainfall_mm']) for row in filtered)
    return total_rainfall / len(filtered)

def most_frequent_crop_high_yield_rain(data):
    """
    Luther: Most frequent crop overall where rainfall > 800mm and yield > 3.5 tons/hectare.
    Uses: Crop, Rainfall_mm, Yield_tons_per_hectare
    """
    crops = [
        row['Crop'] for row in data
        if row['Rainfall_mm'] and float(row['Rainfall_mm']) > 800
        and row['Yield_tons_per_hectare'] and float(row['Yield_tons_per_hectare']) > 3.5
    ]
    if not crops:
        return None
    freq = {}
    for crop in crops:
        freq[crop] = freq.get(crop, 0) + 1

    most_common_crop = max(freq, key=freq.get)
    return most_common_crop
def write_results_to_txt(results, filename="agriculture_results.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(results)
    print(f"Results written to {filename}")

def main():
    csv_filename = "crop_yield.csv"
    print("Reading data from crop_yield.csv...")
    data = read_csv(csv_filename)

    if not data:
        print(" No data loaded. Please check your CSV file.")
        return

    kamila_avg_yield = avg_yield_maize_north_temp_range(data)
    kamila_percent_maize = percentage_maize_east_high_rainfall(data)
    ava_avg_yield_west = avg_yield_temp_range_west(data)
    ava_percent_wheat_south = percentage_wheat_high_yield_south(data)
    luther_avg_rainfall = avg_rainfall_east_high_yield(data)
    luther_most_common_crop = most_frequent_crop_high_yield_rain(data)

    results = (
        "AGRICULTURE CROP YIELD ANALYSIS RESULTS\n"
        "----------------------------------------\n"
        f"1. Avg yield for Maize in North between range 15–25°C: {kamila_avg_yield:.2f} tons/hectare\n"
        f"2. % of Maize crops in East with rainfall >700mm: {kamila_percent_maize:.2f}%\n"
        f"3. Avg yield in West between range 15–25°C: {ava_avg_yield_west:.2f} tons/hectare\n"
        f"4. % of Wheat in South with yield >3.0 tons/hectare: {ava_percent_wheat_south:.2f}%\n"
        f"5. Avg rainfall in East with yield >3.5 tons/hectare: {luther_avg_rainfall:.2f} mm\n"
        f"6. Most frequent crop where rain > 800mm and yield >3.5 tons/hectare): {luther_most_common_crop}\n"
    )
    print("\n" + results)
    write_results_to_txt(results)

mock_data = [
    {'Temperature_Celsius': '16', 'Yield_tons_per_hectare': '3.2', 'Crop': 'Maize', 'Region': 'North', 'Rainfall_mm': '720'},
    {'Temperature_Celsius': '22', 'Yield_tons_per_hectare': '4.5', 'Crop': 'Maize', 'Region': 'East', 'Rainfall_mm': '820'},
    {'Temperature_Celsius': '14', 'Yield_tons_per_hectare': '3.9', 'Crop': 'Wheat', 'Region': 'South', 'Rainfall_mm': '600'},
    {'Temperature_Celsius': '25', 'Yield_tons_per_hectare': '4.0', 'Crop': 'Wheat', 'Region': 'West', 'Rainfall_mm': '750'},
    {'Temperature_Celsius': '30', 'Yield_tons_per_hectare': '4.2', 'Crop': 'Rice', 'Region': 'East', 'Rainfall_mm': '910'},
]

if __name__ == "__main__":
    main()

    print("\n===== RUNNING TESTS =====\n")
    print("1. Avg yield (Maize, North, 15–25°C):")
    print(avg_yield_maize_north_temp_range(mock_data))

    print("\n2. % Maize in East with rainfall >700mm:")
    print(percentage_maize_east_high_rainfall(mock_data))

    print("\n3. Avg yield in West (15–25°C):")
    print(avg_yield_temp_range_west(mock_data))

    print("\n4. % Wheat in South with yield >3.0:")
    print(percentage_wheat_high_yield_south(mock_data))

    print("\n5. Avg rainfall in East, yield >3.5:")
    print(avg_rainfall_east_high_yield(mock_data))

    print("\n6. Most frequent crop (rain >800mm & yield >3.5):")
    print(most_frequent_crop_high_yield_rain(mock_data))

    print("\n===== EDGE TEST CASES =====")

    # Empty data
    empty_data = []
    print("\nEdge 1 - Empty data:")
    print("Avg yield:", avg_yield_maize_north_temp_range(empty_data))
    print("Most frequent crop:", most_frequent_crop_high_yield_rain(empty_data))

    # 2Missing numeric values
    missing_values_data = [
        {'Crop': 'Maize', 'Region': 'North', 'Temperature_Celsius': '', 'Yield_tons_per_hectare': '3.2', 'Rainfall_mm': ''},
        {'Crop': 'Wheat', 'Region': 'South', 'Temperature_Celsius': '20', 'Yield_tons_per_hectare': '', 'Rainfall_mm': '600'}
    ]
    print("\nEdge 2 - Missing values:")
    print("Avg yield:", avg_yield_maize_north_temp_range(missing_values_data))
    print("Avg rainfall:", avg_rainfall_east_high_yield(missing_values_data))

    # Extremely high/low values
    extreme_data = [
        {'Crop': 'Rice', 'Region': 'East', 'Temperature_Celsius': '100', 'Yield_tons_per_hectare': '9.9', 'Rainfall_mm': '2000'},
        {'Crop': 'Maize', 'Region': 'North', 'Temperature_Celsius': '-10', 'Yield_tons_per_hectare': '0.1', 'Rainfall_mm': '50'},
    ]
    print("\nEdge 3 - Extreme values:")
    print("Most frequent crop:", most_frequent_crop_high_yield_rain(extreme_data))
    print("Avg yield (Maize, North):", avg_yield_maize_north_temp_range(extreme_data))

    # Only one matching row
    single_match_data = [
        {'Crop': 'Maize', 'Region': 'East', 'Temperature_Celsius': '23', 'Yield_tons_per_hectare': '4.1', 'Rainfall_mm': '710'},
        {'Crop': 'Rice', 'Region': 'South', 'Temperature_Celsius': '22', 'Yield_tons_per_hectare': '2.9', 'Rainfall_mm': '600'}
    ]
    print("\nEdge 4 - Single matching row:")
    print("Percentage Maize East:", percentage_maize_east_high_rainfall(single_match_data))
    print("Avg rainfall East high yield:", avg_rainfall_east_high_yield(single_match_data))

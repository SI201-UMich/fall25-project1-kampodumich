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


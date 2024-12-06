import matplotlib.pyplot as plt

# Dataset
countries = [
    "United States", "India", "Brazil", "United Kingdom", "South Africa",
    "Germany", "Canada", "Australia", "Russia", "China",
    "Japan", "France", "Italy", "Spain", "Mexico"
]
covid_cases = [
    20000000, 10000000, 8000000, 3500000, 1000000,
    1500000, 500000, 300000, 2000000, 5000000,
    3000000, 2000000, 1800000, 1700000, 1500000
]

# Create the bar graph
plt.figure(figsize=(12, 8))
plt.bar(countries, covid_cases, color='skyblue')

# Adding titles and labels
plt.title("COVID-19 Cases by Country", fontsize=16)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Number of Cases", fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()

# Display the graph
plt.show()

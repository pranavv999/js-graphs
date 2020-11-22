import csv

# Following are the ASEAN countries


def extract_data(file):
    """Return the population data for ASEAN countries for year 2004"""
    countries = [
        "Brunei Darussalam",
        "Cambodia",
        "Indonesia",
        "Lao People's Democratic Republic",
        "Malaysia",
        "Myanmar",
        "Philippines",
        "Singapore",
        "Thailand",
        "Viet Nam",
    ]

    population_data = {
        "gTitle": "ASEAN Countries Population For Year 2014",
        "xLabels": [
            "Brunei",
            "Combodia",
            "Indonesia",
            "Laos",
            "Malaysia",
            "Myanmar",
            "Philippines",
            "Singapore",
            "Thailand",
            "Vietnam",
        ],
        "xText": "Countries",
        "yText": "Population in millions",
    }
    population = []
    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row["Region"] in countries and row["Year"] == "2014":
                value = int(float(row["Population"]) / 1000)
                population.append(value)

        population_data["data"] = population

    return population_data

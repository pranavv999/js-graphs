import csv

# We are refering data from year 2004 to 2014


def extract_data(file):
    """Return the population data for India for year 2004 to 2014"""
    population_data = {
        "gTitle": "Indian Population For Year 2004 - 2014",
        "xLabels": [
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
        ],
        "xText": "Years",
        "yText": "Population in millions",
    }
    population = []
    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if (row["Region"] == "India" and
                    row["Year"] in population_data["xLabels"]):
                # truncating values
                value = int(float(row["Population"]) / 1000)
                population.append(value)

        population_data["data"] = population

    return population_data

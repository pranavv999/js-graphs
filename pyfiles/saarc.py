import csv


saarc_countries = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka",
]


def extract_data(file_name):
    """Return the population data for SAARC countries for year 2004 to 2014"""
    population_data = {
        "gTitle": "SAARC Countries Population For Year 2004 - 2014",
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
        "data": [],
    }
    temp = {}
    with open(file_name, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if (
                row["Region"] in saarc_countries
                and row["Year"] in population_data["xLabels"]
            ):
                value = float(row["Population"])
                temp[row["Year"]] = temp.get(row["Year"], 0) + value

    for val in population_data["xLabels"]:
        population_data["data"].append(int((temp[val] / 1000)))

    return population_data

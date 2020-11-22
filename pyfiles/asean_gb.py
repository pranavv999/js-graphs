import csv


def extract_data(file):
    """Return the population data for ASEAN countries for year 2004 to 2014"""
    population_data = {
        "gTitle": "ASEAN Countries Population For Year 2004 - 2014",
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
    temp = {
        "Brunei Darussalam": [],
        "Cambodia": [],
        "Indonesia": [],
        "Lao People's Democratic Republic": [],
        "Malaysia": [],
        "Myanmar": [],
        "Philippines": [],
        "Singapore": [],
        "Thailand": [],
        "Viet Nam": [],
    }
    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")

        for row in csv_reader:
            if (row["Region"] in temp and
                    row["Year"] in population_data["xLabels"]):

                value = int(float(row["Population"]) / 1000)
                temp[row["Region"]].append(value)

        for key, val in temp.items():
            if key == "Brunei Darussalam":
                key = "Brunei"

            if key == "Lao People's Democratic Republic":
                key = "Laos"

            if key == "Viet Nam":
                key = "Vietnam"

            small_dic = {
                "name": key,
                "data": val
                }
            population_data["data"].append(small_dic)

    return population_data

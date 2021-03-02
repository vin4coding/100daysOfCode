travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country_name, visits_count, places_visited):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = visits_count
    new_country["cities"] = places_visited
    travel_log.append(new_country)
    return travel_log


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

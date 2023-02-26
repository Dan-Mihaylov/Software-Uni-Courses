country = input().split(", ")
city = input().split(",")
country_city = {key: value for (key, value) in zip(country, city)}

for key, value in country_city.items():
    print(f"{key} -> {value}")


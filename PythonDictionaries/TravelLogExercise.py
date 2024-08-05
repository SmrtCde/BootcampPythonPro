"""
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
"""
country = "Brazil"
visits = 2
list_of_cities = ["Sao Paulo","Rio de Janeiro"]

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

######################################################################################

def add_new_entry(c_name,v_num,c_visits):
  new_entry = {}
  new_entry["country"] = c_name
  new_entry["visits"] = v_num
  new_entry["cities"] = c_visits
  travel_log.append(new_entry)

######################################################################################
add_new_entry(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
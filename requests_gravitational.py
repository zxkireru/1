import requests

def get_nasa_data():
    url = "https://api.le-systems.nasa.gov/planets"  
    response = requests.get(url)
    data = response.json()
    return data

def convert_ly_to_km(light_years):
    km = light_years * 9.461e12
    return km

def calculate_gravitational_force(mass1, mass2, distance):
    G = 6.67430e-11  
    force = G * (mass1 * mass2) / (distance ** 2)
    return force

nasa_data = get_nasa_data()

masses = {
    "Earth": 5.972e24,
    "Mars": 6.39e23,
}

average_distances_ly = {
    "Earth": 0,  
    "Mars": 0.52,  
}

average_distances_km = {planet: convert_ly_to_km(dist) for planet, dist in average_distances_ly.items()}

for planet in masses:
    force = calculate_gravitational_force(masses["Earth"], masses[planet], average_distances_km[planet])
    print(f"The attraction between the Earth and {planet}: {force:.2e} Н")

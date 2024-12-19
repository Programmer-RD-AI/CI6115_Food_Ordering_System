import requests

# OSRM API endpoint
base_url = "http://router.project-osrm.org/route/v1/driving"

# Coordinates for origin and destination (latitude, longitude)
origin = "-73.985428,40.748817"  # Example: NYC
destination = "-118.243683,34.052235"  # Example: LA

# Make a request to the API
response = requests.get(f"{base_url}/{origin};{destination}?overview=false")
data = response.json()

# Extract travel duration
duration = data["routes"][0]["duration"] / 60  # in minutes
print(f"Estimated delivery time: {duration} minutes")

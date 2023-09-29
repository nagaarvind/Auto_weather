import requests

# Define the API base URL and your API key
base_url = "http://api.openweathermap.org/geo/1.0/direct"
api_key = "c6e708d0cbd57de925e26e107f23d44b"

# Define the city name
city_name = input("enter city:")

# Construct the API request URL
api_url = f"{base_url}?q={city_name}&limit=2&appid={api_key}"
print(api_url)

# Send the API request and get the response
response = requests.get(api_url)

# Print the response content
print(response.json())

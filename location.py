import requests
import webbrowser

# Get the device's IP address
response = requests.get('https://api.ipify.org/')
ip_address = response.text.strip()

# Get the device's location using the IP address
response = requests.get(f'https://ipapi.co/{ip_address}/json/')
location_data = response.json()

# Extract the latitude and longitude from the location data
latitude = location_data['latitude']
longitude = location_data['longitude']

# Create the Google Maps URL
google_maps_url = f'https://www.google.com/maps/@?api=1&map_action=map&center={latitude},{longitude}&zoom=15'

# Open the Google Maps URL in the default web browser
webbrowser.open(google_maps_url)
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode
import folium

key = "050df201dfaf48618857654f169ebc2b"  # Geocoder API Key
number = input("Please give your number: ")
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number, "en")
tz = timezone.time_zones_for_number(new_number)
print(service_name)
print(tz)

geocoder_service = OpenCageGeocode(key)
query = str(tz)
result = geocoder_service.geocode(query)

if len(result) > 0:
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']

    print(lat, lng)

    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(my_map)

    my_map.save("location.html")

    print("Location tracking completed")
else:
    print("No location found for the given query. Please check your input.")

print("Thank you")

from geopy.geocoders import Nominatim
def location():
    geolocator = Nominatim(user_agent="geopy")
    location = geolocator.reverse("13.036051,77.566617")
    result=location.address
    return(result)


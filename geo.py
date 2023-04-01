from geopy.geocoders import Nominatim
def location():
    geolocator = Nominatim(user_agent="geopy")
    location = geolocator.reverse("LATITUDE_VALUE , LONGITUDE_VALUE")
    result=location.address
    return(result)


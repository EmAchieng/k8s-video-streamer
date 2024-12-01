from utils import get_geolocation

def route_video(ip):
    location = get_geolocation(ip)
    if location == 'CH':
        return 'ch-server'
    else:
        return 'default-server'
        
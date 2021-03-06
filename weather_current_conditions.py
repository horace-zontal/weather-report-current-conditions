import urllib2
import json

f = urllib2.urlopen('http://api.wunderground.com/api/your_API_key_here/geolookup/conditions/q/your_location.json')

json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

station_id = parsed_json['current_observation'] ['station_id']

weather = parsed_json['current_observation'] ['weather']

wind_mph = parsed_json['current_observation']['wind_mph']

wind_gust_mph = parsed_json['current_observation'] ['wind_gust_mph']

wind_dir = parsed_json['current_observation'] ['wind_dir']

windchill_c  = parsed_json['current_observation'] ['windchill_c']

temp_c = parsed_json['current_observation'] ['temp_c']

feelslike_c = parsed_json['current_observation'] ['feelslike_c']

visibility_mi = parsed_json['current_observation'] ['visibility_mi']

pressure_mb = parsed_json['current_observation'] ['pressure_mb']

pressure_trend = parsed_json['current_observation'] ['pressure_trend']

precip_1hr_metric = parsed_json['current_observation'] ['precip_1hr_metric']

solarradiation = parsed_json['current_observation'] ['solarradiation']

UV = parsed_json['current_observation'] ['UV']

print "Your station ID: %s" % (station_id)

print "Weather type in %s: %s" % (location, weather)

print "Wind speed: %s mph, with gusts of up to: %s mph and it is blowing from the: %s. Windchill factor: %s c" % (wind_mph, wind_gust_mph, wind_dir, windchill_c)

print "Current temprature:%s c and it feels like %s c" % (temp_c, feelslike_c)

print "Visibility: %s miles" % (visibility_mi)

print "Current pressure: %s mb and pressure trend: %s" % (pressure_mb, pressure_trend)

print "The precipitation (last hour): %s mm" % (precip_1hr_metric)

print "Solar radiation: %s and UV index: %s" % (solarradiation, UV)

f.close()

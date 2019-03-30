import requests, json

class WeatherClass:


	def GetCurrentWeather(self,city_name):
		api_key = "57feef68f65ebda86fcaec59e33312fb"
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		x = self.posts(complete_url)
		if x["cod"] != "404":
			y = x["main"]
			current_temperature = y["temp"]
			current_pressure = y["pressure"]
			current_humidiy = y["humidity"]
			z = x["weather"]
			weather_description = z[0]["description"]

			if (current_temperature > 300):
				clothes = "short clothes!!!"
			elif (current_temperature < 300 and current_temperature > 296):
				clothes = "Long, thin clothes!!!"
			elif (current_temperature < 296 and current_temperature > 286):
				clothes = "Warm clothing!!!"
			elif (current_temperature < 286):
				clothes = "Bring your best coat!!"

			return(" Temperature (in kelvin unit) = " +
				  str(current_temperature) +
				  "\n atmospheric pressure (in hPa unit) = " +
				  str(current_pressure) +
				  "\n humidity (in percentage) = " +
				  str(current_humidiy) +
				  "\n description = " +
				  str(weather_description) +
				  "\n Offer of clothing: " + clothes)
		else:
			return("City Not Found")

	def Compare(self,city_name1,city_name2):
		api_key = "57feef68f65ebda86fcaec59e33312fb"
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name1
		x = self.posts(complete_url)
		if x["cod"] != "404":
			y = x["main"]
			current_temperature_location1 = y["temp"]
		else:
			return(" Location 1 Not Found ")

		complete_url = base_url + "appid=" + api_key + "&q=" + city_name2
		x = self.posts(complete_url)
		if x["cod"] != "404":
			y = x["main"]
			current_temperature_location2 = y["temp"]
		else:
			return(" Location 2 Not Found ")

		if (current_temperature_location1 > current_temperature_location2):
			return("In " + city_name1 + " it is warmer!")
		else:
			return("In " + city_name2 + " it is warmer!")

	def posts(self, url):
		response = requests.get(url)
		return response.json()


w = WeatherClass()
print("Current weather in London is: \n")
print(w.GetCurrentWeather("London"))
print("\n")
print("Comparison between Israel and London weather:\n")
print(w.Compare("Israel","London"))


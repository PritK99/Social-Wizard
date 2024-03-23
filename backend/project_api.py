import requests

url = "https://instagram-statistics-api.p.rapidapi.com/community"

querystring = {"url":"https://www.instagram.com/verve_0304"}

headers = {
	"X-RapidAPI-Key": "9c33797ae9msh214c753802a05b9p1b7330jsn391debf27903",
	"X-RapidAPI-Host": "instagram-statistics-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
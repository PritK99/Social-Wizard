import requests



url = "https://twitter241.p.rapidapi.com/followings"

querystring = {"user":"2455740283","count":"20"}

headers = {
	"X-RapidAPI-Key": "9c33797ae9msh214c753802a05b9p1b7330jsn391debf27903",
	"X-RapidAPI-Host": "twitter241.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
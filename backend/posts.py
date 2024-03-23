import requests

url = "https://twitter241.p.rapidapi.com/user-tweets"

querystring = {"user":"2455740283","count":"20"}

headers = {
	"X-RapidAPI-Key": "1564210467msh4411bee5b04f222p1e09dcjsn04cef6c0a400",
	"X-RapidAPI-Host": "twitter241.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()


# Assuming 'json_data' contains the JSON data you provided


# Initialize an empty list to store views
views_list = []

# Extract views from each tweet entry
for entry in data['result']['timeline']['instructions'][1]['entries']:
    if 'views' in entry['content']['itemContent']:
        views = entry['content']['itemContent']['views']
        views_list.append(views)

# Print the extracted views
print(views_list)

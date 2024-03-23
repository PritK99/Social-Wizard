import requests
from PIL import Image
from io import BytesIO
import subprocess

url = "https://openjourney1.p.rapidapi.com/models/stabilityai/stable-diffusion-xl-base-1.0"

payload = { "inputs": "Computer Vision " }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "9c33797ae9msh214c753802a05b9p1b7330jsn391debf27903",
	"X-RapidAPI-Host": "openjourney1.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    # Assuming the response contains an image (change the content type accordingly)
    if 'image/jpeg' in response.headers['content-type'] or 'image/png' in response.headers['content-type']:
        # Extract image data from the response content
        image_data = response.content

        # Save the image to a file
        with open('./image.png', 'wb') as f:
            f.write(image_data)

        # Open the image using the default image viewer
        subprocess.run(['xdg-open', '/tmp/image.png'])
    else:
        print("Response does not contain an image.")
else:
    print("Request was not successful. Status code:", response.status_code)
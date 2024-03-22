# Workflow
'''
Step 1 is to generate a post for the given title, description and metadata. Title is compulsory, description is optional, metadata is compulsory.
Metadata comprises of the following:
1. List of top 10 trending topics
2. Age category
3. Country
The post generated should have the following:
1. Text
2. Hashtags
In addition to this, we need to provide a link to an image which is relevant to the post. For this we need an API to accept user title and description combined into a summary as an input and return a relevant image link.
'''
import google.generativeai as genai
from bs4 import BeautifulSoup
import markdown
import requests
import re
import random

GEMINI_API_KEY = "AIzaSyCGOYJNkoztEVxDN28qgzhe1VCb-RGSh6c"
UNSPLASH_ACCESS_KEY = "Tu32Z8QsAUfhs0VAODyy4i0Vv3ddwDPf1Ba2N-EMB3s"

# We use Gemini Pro for our implementation
model = genai.GenerativeModel('gemini-pro')
genai.configure(api_key=GEMINI_API_KEY)

def get_image_link(search_query, page=1, per_page=1):
    url = f"https://api.unsplash.com/search/photos?query={search_query}&per_page={per_page}&page={page}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["total"] > 0:
            image_link = data['results'][0]['urls']['regular']
            return image_link
    return None

# Part 1: Generate post for the given title, description and metadata
def gen_post(title, description = ""):
    if GEMINI_API_KEY == "":
        raise ValueError("Please set your API key.")

    # We have user_prompt, database_schema and template as inputs to the model. However, database_schema and template are optional.
    if (title == ""):
        raise ValueError("Prompt is required.")
    
    if (description == ""):
        description = title
    
    metadata_prompt = "Age category: " + "20-30" + ". Country: " + "India" + ". Top trending topics: " + "AI, ML, Data Science"
    
    prompt = (
        "For the topic: " + title + " and description: " + description + ", provide a social media post which I can post directly. The post should have emojis and hashtags. You can make it targeting audience with: " + metadata_prompt
    )

    post_prompt = "Give me a social media post which I can directly post on topic: " + title + ". " + description + " Provide personalized content suggestions, including text, emojis and hashtags. Make it very captivating and interesting based on the topics or memes which are currently trending on social media."

    post_result = model.generate_content(post_prompt)
    post_text = post_result.text

    img_prompt = ("In one word only give me the main subject in one word only for which an image should be generated: " + title)
    
    img_result = model.generate_content(img_prompt)
    img_text = img_result.text

    image_link = get_image_link(img_text)
    if image_link:
        post= {'text': post_text, 'image_link': image_link}
    else:
        post = {'text': post_text, 'image_link': None}

    return post


# def remove_markdown(markdown_text):
#     html = markdown.markdown(markdown_text)
#     soup = BeautifulSoup(html, features="lxml")
#     text_elements = soup.find_all(string=True)
#     cleaned_text = "".join(text_elements)
#     return cleaned_text

# def insert_spaces_before_caps(text):
#     # Insert space before capital letters (except at the beginning)
#     return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# def remove_code_markdown(code):
#     lines = code.split('\n')
#     trimmed_code = '\n'.join(lines[1:-1])
#     return trimmed_code


# Uncomment the below code to run the standalone model
post = gen_post("A smart-phone")
print(post['text'])
if post['image_link']:
    print("Image Link:", post['image_link'])
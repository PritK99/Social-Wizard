import google.generativeai as genai
import requests 
from utils import clean_text 

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

class ContentGenerator:
    def __init__(self, analyzer = None ):
        self.analyzer = analyzer  
        GEMINI_API_KEY = "AIzaSyCGOYJNkoztEVxDN28qgzhe1VCb-RGSh6c"

        self.model = genai.GenerativeModel('gemini-pro')
        genai.configure(api_key=GEMINI_API_KEY)
        
    
    def get_image_link(self, search_query, page=1, per_page=1):
        UNSPLASH_ACCESS_KEY = "Tu32Z8QsAUfhs0VAODyy4i0Vv3ddwDPf1Ba2N-EMB3s"

        url = f"https://api.unsplash.com/search/photos?query={search_query}&per_page={per_page}&page={page}&client_id={UNSPLASH_ACCESS_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["total"] > 0:
                image_link = data['results'][0]['urls']['regular']
                return image_link
        return None

    def gen_post(self,title, description = ""):
       

        if (title == ""):
            raise ValueError("Prompt is required.")
        
        if (description == ""):
            description = title

        if self.analyzer :
            metadata_prompt = f"No of people of age 0-20 : {self.analyzer.age_groups[0]} . No of people of age 20-40 : { self.analyzer.age_groups[1] }. No of people of age 40+ : { self.analyzer.age_groups[2] } .Average age : { self.analyzer.age} . Top 3 locations : { self.analyzer.locations } . Hot topics : { self.analyzer.hot_topics } "


        
            prompt = (
                "For the topic: " + title + " and description: " + description + ", provide a social media post which I can post directly. The post should have emojis and hashtags. You can make it targeting audience with: " + metadata_prompt
            )

        else:
            prompt = "Give me a social media post which I can directly post on topic: " + title + ". " + description + " Provide personalized content suggestions, including text, emojis and hashtags. Make it very captivating and interesting based on the topics or memes which are currently trending on social media."

        post_result = self.model.generate_content(prompt,safety_settings=safety_settings)
        post_text = clean_text(post_result.text)

        img_prompt = ("In one word only give me the main subject in one word only for which an image should be generated: " + title + ". " + description)
        
        img_result = self.model.generate_content(img_prompt,safety_settings=safety_settings)
        img_text = img_result.text

        image_link = self.get_image_link(img_text)
        if image_link:
            post= {'text': post_text, 'image_link': image_link}
        else:
            post = {'text': post_text, 'image_link': None}

        return post





    
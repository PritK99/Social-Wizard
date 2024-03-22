import google.generativeai as genai


class ContentGenerator:
    def __init__(self, userList, analyzer = None ):
        self.userList = userList 
        self.analyzer = analyzer  
        GEMINI_API_KEY = "AIzaSyCGOYJNkoztEVxDN28qgzhe1VCb-RGSh6c"
        self.model = genai.GenerativeModel('gemini-pro')
        genai.configure(api_key=GEMINI_API_KEY)
        
    
    def get_image_link(self, search_query, page=1, per_page=1):
        url = f"https://api.unsplash.com/search/photos?query={search_query}&per_page={per_page}&page={page}&client_id={UNSPLASH_ACCESS_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["total"] > 0:
                image_link = data['results'][0]['urls']['regular']
                return image_link
        return None
    def gen_post(title, description = ""):
       

        if (title == ""):
            raise ValueError("Prompt is required.")
        
        if (description == ""):
            description = title

        if self.analyzer is None:
            metadata_prompt = "Age category: " + "20-30" + ". Country: " + "India" + ". Top trending topics: " + "AI, ML, Data Science"
        else:
            metadata_promp = "Age category: " + self.analyzer.get_age_category() + ". Country: " + self.analyzer.get_country() + ". Top trending topics: " + self.analyzer.get_top_trending_topics()


        
        prompt = (
            "For the topic: " + title + " and description: " + description + ", provide a social media post which I can post directly. The post should have emojis and hashtags. You can make it targeting audience with: " + metadata_prompt
        )

        post_prompt = "Give me a social media post which I can directly post on topic: " + title + ". " + description + " Provide personalized content suggestions, including text, emojis and hashtags. Make it very captivating and interesting based on the topics or memes which are currently trending on social media."

        post_result = self.model.generate_content(post_prompt)
        post_text = post_result.text

        img_prompt = ("In one word only give me the main subject in one word only for which an image should be generated: " + title)
        
        img_result = self.model.generate_content(img_prompt)
        img_text = img_result.text

        image_link = self.get_image_link(img_text)
        if image_link:
            post= {'text': post_text, 'image_link': image_link}
        else:
            post = {'text': post_text, 'image_link': None}

        return post





    
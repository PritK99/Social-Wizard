
import google.generativeai as genai
import requests

# GEMINI_API_KEY = "AIzaSyCGOYJNkoztEVxDN28qgzhe1VCb-RGSh6c"
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

def gemini_prompt(prompt,GEMINI_API_KEY):
    # GEMINI_API_KEY = "AIzaSyCUILsC42O2soKx8_P0VQhHKL44i9qhqhs"
    # UNSPLASH_ACCESS_KEY = "Tu32Z8QsAUfhs0VAODyy4i0Vv3ddwDPf1Ba2N-EMB3s"

    # We use Gemini Pro for our implementation
    model = genai.GenerativeModel('gemini-pro')
    genai.configure(api_key=GEMINI_API_KEY)
    if GEMINI_API_KEY == "":
        raise ValueError("Please set your API key.")

    if (prompt == ""):
        raise ValueError("Prompt is required.")
    
    
    
    

    result = model.generate_content(prompt,safety_settings=safety_settings)
    print(result)
    res = result.text

  
    return res 



def mistral_prompt(prompt):


    url = "https://open-ai32.p.rapidapi.com/conversationgpt4"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": "hello"
            }
        ],
        "web_access": False
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "1564210467msh4411bee5b04f222p1e09dcjsn04cef6c0a400",
        "X-RapidAPI-Host": "open-ai32.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    # print(response.json())
    return response.json()['result']

# if __name__=='__main__':
#     gemini_prompt("Hi", "AIzaSyCGOYJNkoztEVxDN28qgzhe1VCb-RGSh6c")
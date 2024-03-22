import openai

OPENAI_API_KEY = "your_openai_api_key_here"

# Setting OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to generate post using OpenAI
def gen_post(title, description=""):
    if OPENAI_API_KEY == "":
        raise ValueError("Please set your OpenAI API key.")

    if title == "":
        raise ValueError("Title is required.")

    # Constructing the prompt
    prompt = f"Generate a social media post for the topic '{title}'"
    if description:
        prompt += f" with the description '{description}'"
    prompt += ". Include emojis and hashtags. Target audience: Age category: 20-30, Country: India, Top trending topics: AI, ML, Data Science."

    # Generating post using OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,  # Adjust max_tokens as needed
        n=1,
        stop="\n",
        temperature=0.5,
    )

    # Extracting generated text from OpenAI's response
    post_text = response.choices[0].text.strip()

    # Generating image link using OpenAI
    img_prompt = f"Generate an image for the topic '{title}'"
    if description:
        img_prompt += f" with the description '{description}'"

    img_response = openai.Image.create(
        search_model="clip",  # Using CLIP model for image search
        query=img_prompt,
        max_images=1,
    )

    # Extracting image link from OpenAI's response
    if img_response and img_response.status == "success" and img_response.output and len(img_response.output.images) > 0:
        image_link = img_response.output.images[0].url
    else:
        image_link = None

    post = {'text': post_text, 'image_link': image_link}
    return post


# Example usage
post = gen_post("A smart-phone")
print(post['text'])
if post['image_link']:
    print("Image Link:", post['image_link'])

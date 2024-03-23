import re

def extract_python_list(string):
    # Define a regular expression pattern to match Python lists
    pattern = r'\[.*?\]'

    # Use re.findall to find all matches of the pattern in the string
    matches = re.findall(pattern, string)

    # If there are matches, return the first one
    if matches:
        return matches[0]
    else:
        return None

def clean_text(string):
    import re

def clean_text(text):
    # Define the regular expression pattern to match special characters except newline (\n)
    pattern = r'[^\w\s\n]'
    # Substitute the special characters with an empty string
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text


if __name__ == '__main__':
        
    example_text = """
    Text:
    \ud83d\udca6 Say goodbye to boring plastic bottles! \ud83d\udca6
    Introducing the Tupperware Water Bottle \u2013 the hydration revolution you've been waiting for! \ud83d\udca7\u2728

    Emoji: \ud83d\udca7 \u2728 \u267b\ufe0f

    Trending Content Suggestion:
    GIF: A GIF of a person struggling to lift a heavy plastic water jug, then switching to a lightweight Tupperware Water Bottle with a sly smile.
    Meme: "Me: I'm saving the planet one sip at a time. My reusable Tupperware Water Bottle: You got this, champ!"

    Personalized Content Suggestion:
    Text:
    "[Insert Name], you deserve hydration that's as unique as you are! Customize your Tupperware Water Bottle with your favorite color and pattern, and show the world your style." \ud83c\udfa8\ud83c\udf08

    Hashtag: #HydrateInStyle
    """
    cleaned_example_text = clean_text(example_text)

    # Print the cleaned text
    print(cleaned_example_text)

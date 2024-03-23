from user import User 
from gemini import gemini_prompt , mistral_prompt
import datetime
import pytz
from fuzzywuzzy import process
from utils import extract_python_list

GEMINI_API_KEY_1 = "AIzaSyCUILsC42O2soKx8_P0VQhHKL44i9qhqhs"
GEMINI_API_KEY_2 = "AIzaSyCGOYJNkoztEVxDN28qgzhe1VCb-RGSh6c"
class Analyzer:

    def __init__(self, userList ) -> None:
        self.userList = userList 
        self.locations = None 
        self.hot_topics = None 
        self.frequencies = None 
        self.average_age = None
        self.age_groups = [0,0,0] 
    
    def get_age(self):
        total_age = 0 
        count = 0
        for user in self.userList :
            if user.expected_age:
                total_age += user.expected_age
                if user.expected_age < 20 :
                    self.age_groups[0] += 1 
                elif user.expected_age < 40 :
                    self.age_groups[1] += 1 
                else:
                    self.age_groups[2] += 1
                count +=1 
        
        self.age = total_age/count 

        return self.age,self.age_groups 
    
    def get_locations(self):
        
        locations = []
        for user in self.userList :
            locations.append(user.location)
        prompt = f"""
        Below is a list of locations , you just need to give me a list of countries in which they are in . 
        {locations}
        Just return me the countries in python list format . If countries repeat , let them . I do 
        not want unique names in the list . Size of output list from you should be same as input list by me . 

        """
        p = gemini_prompt(prompt,GEMINI_API_KEY_1)
        # p = mistral_prompt(prompt)
        # print(p)

        countries = extract_python_list(p)[1:-1].split(",")
        countries = [x for x in countries if x.strip() != "''" and x]
        print(countries)
        freq_map = {}
        for c in countries : 
            
            country_name = c.strip()[1:-1].lower()
            freq_map[country_name] =  freq_map.get(country_name,0) + 1 
        sorted_items = sorted(freq_map.items(), key=lambda item: item[1],reverse=True)

        # Storing keys in one list
        self.locations = [item[0] for item in sorted_items]

        # Storing values in another list
        self.frequencies = [item[1] for item in sorted_items]
        return self.locations,self.frequencies 

    def get_recommended_time(self):
        if self.locations is None : 
            self.get_locations()
        gmt_time = self.convert_to_gmt(self.locations[0])
        if gmt_time:
            print("GMT Time:", gmt_time)
        return gmt_time 
    
    def convert_to_gmt(self,location):
        all_timezones = pytz.all_timezones

        best_match = process.extractOne(location, all_timezones)

        

        timezone = pytz.timezone(best_match[0])

        # Get the current time in the specified timezone
        local_time = datetime.datetime.now(timezone)

        # Convert the local time to GMT
        gmt_time = local_time.astimezone(pytz.utc)

        return gmt_time.strftime("%m/%d/%Y, %H:%M:%S")
        
    def get_hot_topics(self):
        descriptions = []
        for user in self.userList :
            if user.description != "":
                descriptions.append(user.description)

        prompt = f"""
        Below is a list of description of some people :
        {descriptions}
        give me a list of  hot topics from the descriptions .Just return me the top 10 hot topics . 
        It should be sorted descending by popularity . 
        Give it in python list format only i.e surrounded by brackets and separated by comma.
        """
        p = gemini_prompt(prompt,GEMINI_API_KEY_2)
        # p = mistral_prompt(prompt)
        print(p)
        hot_topics = extract_python_list(p)[1:-1].split(",")
        self.hot_topics = [h.strip()[1:-1] for h in hot_topics]
            
        print(self.hot_topics)
        return self.hot_topics 
        
        

if __name__=='__main__':
    from twitter import twitterHandler
    UsertwitterHandle = twitterHandler('SRAVJTI')
    analyzer = Analyzer(UsertwitterHandle.get_user_related())
    analyzer.get_locations()
    analyzer.get_recommended_time()
    analyzer.get_hot_topics()


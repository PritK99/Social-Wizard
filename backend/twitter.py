import requests
import json 
from user import User 
import os 

class twitterHandler:
    def __init__(self,name):
        self.username = name
        self.user_id = self.get_username_by_id(name)
        self.following = None 
        self.followers = None 

    def get_followers_data(self):
        url = "https://twitter241.p.rapidapi.com/followings"

        querystring = {"user":self.user_id,"count":"20"}

        # headers = {
        #     "X-RapidAPI-Key": "9c33797ae9msh214c753802a05b9p1b7330jsn391debf27903",
        #     "X-RapidAPI-Host": "twitter241.p.rapidapi.com"
        # }
        headers = {
            "X-RapidAPI-Key": os.environ['RAPID_API_KEY'],
            "X-RapidAPI-Host": "twitter241.p.rapidapi.com"
        }
        data = requests.get(url, headers=headers, params=querystring)
        data = json.loads(data.text)
        self.followers = data 
        return data
 

   
    def get_username_by_id(self,name):

        url = "https://twitter241.p.rapidapi.com/user"

        querystring = {"username":name}

        # headers = {
        #     "X-RapidAPI-Key": "9c33797ae9msh214c753802a05b9p1b7330jsn391debf27903",
        #     "X-RapidAPI-Host": "twitter241.p.rapidapi.com"
        # }
        headers = {
            "X-RapidAPI-Key": os.environ['RAPID_API_KEY'],
            "X-RapidAPI-Host": "twitter241.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        dictv = json.loads(response.text)
        print(dictv)
        return dictv['result']['data']['user']['result']['rest_id']

    def get_following_data(self):
        url = "https://twitter241.p.rapidapi.com/followers"

        
        querystring = {"user": self.user_id ,"count":"20"}

        # headers = {
        #     "X-RapidAPI-Key": "9c33797ae9msh214c753802a05b9p1b7330jsn391debf27903",
        #     "X-RapidAPI-Host": "twitter241.p.rapidapi.com"
        # }

        headers = {
            "X-RapidAPI-Key": os.environ['RAPID_API_KEY'],
            "X-RapidAPI-Host": "twitter241.p.rapidapi.com"
        }
        data = requests.get(url, headers=headers, params=querystring)
        data = json.loads(data.text)
        self.following = data
        return data

    def get_following(self):
        # if self.followers == None:
        #     self.get_followers_data()
        if self.following is None:
            self.get_following_data()
        user_following = []
        for entry in self.following['result']['timeline']['instructions']:
            if 'entries' in entry:
               
                user_entries= entry['entries']
                for user in user_entries:
                    
                    u = User()
                    try:
                        user_id = user['content']['itemContent']['user_results']['result']['rest_id']
                        u.set_id(user_id)
                    except:
                        continue 

                    try: 
                        user_name = user['content']['itemContent']['user_results']['result']['legacy']['name']
                        u.set_name(user_name)
                    except:
                        pass 

                    try:
                        user_desc = user['content']['itemContent']['user_results']['result']['legacy']['description']
                        u.set_description(user_desc)
                    except:
                        pass 

                    try:
                        user_loc = user['content']['itemContent']['user_results']['result']['legacy']['location']
                        u.set_location(user_loc)
                    except:
                        pass 


                    user_following.append(u)
                    
                    

        return user_following
    
    def get_followers(self):
        # if self.followers == None:
        #     self.get_followers_data()
        if self.followers is None:
            self.get_followers_data()
        
        user_followers = []

        for entry in self.followers['result']['timeline']['instructions']:
            if 'entries' in entry:
               
                user_entries= entry['entries']
                for user in user_entries:
                    
                    u = User()
                    try:
                        user_id = user['content']['itemContent']['user_results']['result']['rest_id']
                        u.set_id(user_id)
                    except:
                        continue 

                    try: 
                        user_name = user['content']['itemContent']['user_results']['result']['legacy']['name']
                        u.set_name(user_name)
                    except:
                        pass 

                    try:
                        user_desc = user['content']['itemContent']['user_results']['result']['legacy']['description']
                        u.set_description(user_desc)
                    except:
                        pass 

                    try:
                        user_loc = user['content']['itemContent']['user_results']['result']['legacy']['location']
                        
                        u.set_location(user_loc)
                    except:
                        pass 
                    
                    try:
                        user_expected_age = 12.6 + 2024 - int(user['content']['itemContent']['user_results']['result']['legacy']['created_at'][-4:]) 
                        u.set_age(user_expected_age)
                    except:
                        pass

                    user_followers.append(u)
                    
                    

        return user_followers
    
    def get_user_related(self,depth = 1):
        if depth>1 :
            raise Exception("Depth>1 functionality not implemented")
        return self.get_following() + self.get_followers()
    

# for entry in data['result']['timeline']['instructions']:
#     if 'entries' in entry:
#         user_id = entry['entries']['itemContent']['user_results']['result']['rest_id']
        
#         for follower_entry in entry['entries']:
#             follower_id = follower_entry['entries']['content']['user_results']['result']['rest_id']
#             users[user_id]['followers'].append(follower_id)
#             users[follower_id]['following'].append(user_id)


if __name__ == '__main__':
    twitterHandle = twitterHandler('SRAVJTI')
    relatedUsers = twitterHandle.get_user_related()



# def bfs_depth(user_id, users, target_depth):
#     users_at_depth = set()
#     visited = set()
#     queue = [(user_id, 0)]
    
#     while queue:
#         current_user, depth = queue.pop(0)
#         visited.add(current_user)
        
#         if depth == target_depth:
#             users_at_depth.add(current_user)
#             continue
        
#         if depth < target_depth:
#             for follower in users[current_user]['followers']:
#                 if follower not in visited:
#                     queue.append((follower, depth + 1))
#             for following in users[current_user]['following']:
#                 if following not in visited:
#                     queue.append((following, depth + 1))
    
#     return users_at_depth

# print(bfs_depth(userid,users,1))
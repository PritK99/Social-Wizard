from flask import current_app as app,request,jsonify,Response
from flask_restful import  Resource, fields, marshal_with, reqparse
import json
from main import api

import os 
from twitter import twitterHandler 
from analysis import Analyzer 
from generator import ContentGenerator

# message_context_args = {
#     "description",
#     "top_3_locations" , 
#     "recommended_time" , 
#     "hot_topics"
    
# }

message_analysis_args = {
    "userName"
    
}


message_content_args = {
    "title", 
    "description", 

}


analyzer_global = None 


class AnalysisAPI(Resource):
    
    
    def post(self):
        global analyzer_global
        for arg in request.json :
            
            if arg not in message_analysis_args:
                return "Invalid JSON",400
        print(request.json)
        print(type(request.json))
        name = request.json['userName']
        UsertwitterHandle = twitterHandler(name)
        analyzer = Analyzer(UsertwitterHandle.get_user_related())
        analyzer_global = analyzer
       
        top_3_locations , freq   = analyzer.get_locations()
        if len(top_3_locations)>3:
            top_3_locations = top_3_locations[:3]
            freq = freq[:3]
        
        rec_time = analyzer.get_recommended_time()
        hot_topics =  analyzer.get_hot_topics()
        avg_age,age_groups = analyzer.get_age()
        final_res = {
            'top_3_locations': top_3_locations , 
            'recommended_time':rec_time , 
            'hot_topics': hot_topics , 
            'location_frequencies': freq , 
             'average_expected_age':avg_age , 
             'age_groups': age_groups}
        
        print(final_res)
        return Response(json.dumps(final_res),status=200)
        # return Response(json.dumps({}),status=200)
        
        

class ContentGeneratorAPI(Resource):
    
    
    def post(self):
        global analyzer_global
        analyzed = False 
        for arg in request.json :
            
            if arg not in message_content_args:
                return "Invalid JSON",400
        
         
        if analyzer_global:
            cg = ContentGenerator(analyzer_global)
            analyzed = True 
        else:
            cg = ContentGenerator()
            analyzed = False 

        print(request.json)
        print(type(request.json))
        title = request.json['title']
        description = request.json['description']

        
       
        final_res = cg.gen_post(title,description)
        final_res['analyzed'] = analyzed
        
        print(final_res)
        analyzer_global = None
        return Response(json.dumps(final_res),status=200)
        # return Response(json.dumps({}),status=200)
        

      

api.add_resource(AnalysisAPI,  '/getAnalysis')
api.add_resource(ContentGeneratorAPI,  '/getContent')

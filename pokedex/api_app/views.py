from rest_framework.views import APIView
from rest_framework.response import Response
import requests # <== import requests so we can utilize it within our CBV to make API calls
from requests_oauthlib import OAuth1 #<== import OAuth1 which will essentially authenticate our keys when we send a request
from pokedex_proj.settings import env
import pprint

pp = pprint.PrettyPrinter(indent=2, depth=2)

class Noun_Project(APIView):
    # In our CBV lets create a method to interact with the NounAPI
    def get(self, request, types):
        auth = OAuth1(env.get("NOUN_API_KEY"), env.get("NOUN_API_SECRET"))
        endpoint = f"https://api.thenounproject.com/v2/icon?query={types}&limit=1"

        response = requests.get(endpoint, auth=auth)

        responseJSON = response.json()
        pp.pprint("noun_project.get() response json")
        pp.pprint(responseJSON)

        return Response(responseJSON['icons'][0]['thumbnail_url'])
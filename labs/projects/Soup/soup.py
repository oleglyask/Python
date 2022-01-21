# from ingredient import Ingredient
import requests
from pprint import pprint

class Soup:

    def __init__(self, *args) -> None:
        self.ingredients = args


    def cook(self):
        api_key = 'e1134e3deb5d448596a6ac8f06cc4f57'
        ingredient_list = ""
        for ingreditent in self.ingredients:
            ingredient_list += f'{ingreditent.name.lower()},'
        url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query=soup&includeIngredients={ingredient_list}'
        results = requests.get(url).json()
        
        if results['totalResults'] > 0:
            self.name = results['results'][0]['title']
            print(f'You got a tasty {self.name}')
        else:
            print('No soup with these ingredients')
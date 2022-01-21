# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.


from ingredient import Ingredient
import webbrowser

carrot = Ingredient("carrot", 25)

carrot.get_info()
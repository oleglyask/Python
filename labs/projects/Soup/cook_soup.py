from soup import Soup
from ingredient import Ingredient

c = Ingredient('potato', 5)
p = Ingredient('carrot', 3)

soup = Soup(c, p)

soup.cook()

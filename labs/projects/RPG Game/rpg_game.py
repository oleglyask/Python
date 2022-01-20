from hero import Hero
import random

hero = Hero(len('oleg'), 10)
bad_guy = Hero(random.randint(2,10), 10)

hero.battle(bad_guy)

print(hero)
print(bad_guy)
import webbrowser

class Ingredient:

    def __init__(self, name, amount) -> None:
        self.name = name.capitalize()
        self.amount = amount

    def __str__(self) -> str:
        return f"name = {self.name}\namount = {self.amount}\n"

    def get_info(self):
        webbrowser.open(f"https://en.wikipedia.org/wiki/{self.name.capitalize()}")

    
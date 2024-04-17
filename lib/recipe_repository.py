from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM recipes")
        recipes = []
        for row in rows:
            item = Recipe(row['id'], row['recipe_name'], row['average_cooking_time'], row['rating'])
            recipes.append(item)
        return recipes
        
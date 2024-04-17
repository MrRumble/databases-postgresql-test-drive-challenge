from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipes.sql")

# Retrieve all artists
recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

# List them out
for recipe in recipes:
    print(recipe)
    print(type(recipe.id))
    print(type(recipe.recipe_name))
    print(type(recipe.average_cooking_time))
    print(type(recipe.rating))
print(recipes)


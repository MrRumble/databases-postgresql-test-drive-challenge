from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe
"""
When we call RecipeRepository all() 
We get a list of recipe objects reflecting the seed data.
"""

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipes.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new ArtistRepository

    recipes = repository.all() # Get all artists
    # Assert on the results
    assert recipes == [
        Recipe(1, 'Fish and Chips', 20, 3),
        Recipe(2, 'Steak and Eggs', 12, 4),
        Recipe(3, 'Roast Dinner', 60, 5),
        Recipe(4, 'Vegan Nut Roast', 30, 1),
        Recipe(5, 'Korean Fried Chicken and Rice', 25, 5),
    ]

def test_find_recipe_method(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(1)
    assert recipe == Recipe(1, 'Fish and Chips', 20, 3)



from lib.recipe import Recipe

"""
Test recipe constructs with id, recipe name, average_cooking_time and rating
"""
def test_recipe_construct():
    recipe = Recipe(1, 'test dish', '20', '3')
    assert recipe.id == 1
    assert recipe.recipe_name == 'test dish'
    assert recipe.average_cooking_time == '20'
    assert recipe.rating == '3'

"""
Test we can format recipe strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, 'test dish', '20', '3')
    assert str(recipe) == "Recipe(1, test dish, 20, 3)"


"""
Test compare two identical recipes
and have them be equal
"""
def test_identical_recipes_equate():
    recipe1 = Recipe(1, 'test dish', '20', '3')
    recipe2 = Recipe(1, 'test dish', '20', '3')
    assert recipe1 == recipe2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import DATABASE_URL
from models import Recipe, Chef

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


# Open Session Here, so you don't need to open and close all the time, close at the end of exercises.
session = Session()


# 02 Create Recipe
def create_recipe(name: str, ingredients: str, instructions: str) -> None:

    new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
    session.add(new_recipe)
    session.commit()


# Create some recipes.

# recipes = [
#     {
#         "name": "paghetti Carbonara",
#         "ingredients": "Pasta, Eggs, Pancetta, Cheese",
#         "instructions": "Cook the pasta, mix it with eggs, pancetta, and cheese",
#     },
#     {
#         "name": "Chicken Stir-Fry",
#         "ingredients": "Chicken, Bell Peppers, Soy Sauce, Vegetables",
#         "instructions": "Stir-fry chicken and vegetables with soy sauce",
#     },
#     {
#         "name": "Caesar Salad",
#         "ingredients": "Romaine Lettuce, Croutons, Caesar Dressing",
#         "instructions": "Toss lettuce with dressing and top with croutons",
#     }
# ]
#
# for recipe in recipes:
#     create_recipe(name=recipe["name"], ingredients=recipe["ingredients"], instructions=recipe["instructions"])


# 03 Update Recipe
def update_recipe_by_name(name: str, new_name: str,  new_ingredients: str, new_instructions: str) -> None:
    recipe_to_update = session.query(Recipe).filter_by(name=name).first()

    recipe_to_update.name = new_name
    recipe_to_update.ingredients = new_ingredients
    recipe_to_update.instructions = new_instructions

    session.commit()


# 04 Delete Recipe
def delete_recipe_by_name(name: str) -> None:
    session.query(Recipe).filter_by(name=name).delete()
    session.commit()


# 05 Filter Recipes
def get_recipes_by_ingredient(ingredient_name: str) -> list:
    found_recipes = session.query(Recipe).filter(Recipe.ingredients.ilike(f"%{ingredient_name}%")).all()
    return found_recipes


# 06 Recipe Ingredients Swap Transaction
def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str) -> None:

    try:
        session.begin()
        first_recipe = session.query(Recipe).filter_by(name=first_recipe_name).first()
        second_recipe = session.query(Recipe).filter_by(name=second_recipe_name).first()

        first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients
        session.commit()

    except Exception as error:
        session.rollback()  # Rollback if an error occurs.
        return str(error)

    finally:
        session.close()


# 09 Recipe and Chef Relations
def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str):

    session.begin()

    try:
        recipe = session.query(Recipe).filter_by(name=recipe_name).first()
        chef = session.query(Chef).filter_by(name=chef_name).first()

        if not recipe.chef_id:
            recipe.chef = chef
        else:
            raise Exception(f"Recipe: {recipe.name} already has a related chef")

        session.commit()

        return f"Related recipe {recipe.name} with chef {chef.name}"

    except Exception as error:
        session.rollback()
        return str(error)

    finally:
        session.close()


# 10 Chef and Recipe Integration
def get_recipes_with_chef():

    recipes_with_chefs = session.query(Recipe.name, Chef.name.label("chef_name")).join(Chef, Recipe.chef).all()
    result = []
    for rec_name, chef_name in recipes_with_chefs:
        result.append(f"Recipe: {rec_name} made by chef: {chef_name}")

    return "\n".join(result)


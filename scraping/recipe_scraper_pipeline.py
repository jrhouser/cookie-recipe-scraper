import fetch_recipes as fr
import get_categories as gc
import fetch_links_to_recipies as flr



rec_link_file = 'recipe_links.csv'
rawfileout = 'raw_ingredients.csv'
fileout = 'ingredient_stars.csv'
category_filename='category_list.csv'

gc.fetch(category_filename)   				# get the list of categories
flr.fetch(category_filename,rec_link_file)	# get the links to the recipes in each category
fr.fetch(fileout,rawfileout,rec_link_file)	# get the recipes and ratings from each recipe



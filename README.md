# cookie-recipe-scraper

These collection of scripts are for scraping of easyrecipes.com for cookie recipes and associated ratings. Also included is some basic analysis of the resultant data and scripts to build a family tree of different cookie recipes. These scripts may one day be a nice user friendly package, but not today. A description of some interesting results found from this analysis is given below.

# Which cookies are the most popular?
I found that pumpkin cookie recipes, although representing a small proportion of recipies overall, had the second highest average number of reviews across the major categories of cookies (Figure 1). The first and third highest average number of reviews were from chocolate chip and oatmeal cookies. As it turned out the average rating for all categories was just over 4 stars (although there were many unrated/0 star recipes).

# Rating system is (almost) entirely useless 
As it turned out the average rating for all categories was just over 4 stars (although there were many unrated/0 star recipes).This data suggests that either the allrecipies.com ratings are inflated or that people who dislike a recipie are unlikely to post a review. In either case active solicitation of reviews, restructuring of the rating system, or implementation of a trusted reviewer (such as in yelp) would be worth considering if the allrecipies.com staff wanted to improve their site. 

# Pumpkin cookies are in a class of their own and family tree of cookies
To discover how closely different types of cookies are related, I built a family tree of different cookie categories. To do this,  I used hierarchical clustering. Specifically I clustered on the fraction (by total volume) of the top 25 most common ingredients averaged for each category. A heat map of the log of the fraction of ingredients averaged for each category is plotted in figure 2 along with a dendrogram displaying the hierarchical relationship of the cookie categories.  In this figure we see that two of the top three most reviewed cookies -pumpkin and oatmeal cookies- are much less similar to other cookies compared to other cookie types. Here we see that pumpkin cookies are in a class of their own. What was surprising to me was that pumpkin cookies are not at all similar to fruit cookies. However, fruit and nut cookies are closely related. 



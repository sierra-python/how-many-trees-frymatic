# first, we counted the number of trees visible along a street in the 40s of midtown sacramento in google streetview
trees = 54
streetLength = 1000 # measuring the length of the street where we counted trees in google maps, we found ~1000 ft

# finding the density of trees per foot using the tree count divided by the length of street measured
treesPerFt = trees / streetLength

# we found on Google that the estimated area of Sacramento was ~100 square miles
sqft = (10 * 5280) ** 2 # square footage of sac 

# density trees
treesPerSqFt = treesPerFt ** 2

# total trees out of square footage multiplied by tree density
totalTrees = sqft * treesPerSqFt
print(totalTrees) # +~813k, cap radio estimates there are 1 million trees... sooooo, pretty close


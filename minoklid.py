import numpy as np
from itertools import combinations

# 1. Defining the Points
points = np.arange(8).reshape(4, 2)
print(points)

# 2. Defining a Function for Euclidean Distance
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
#    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) # alternative
#    return np.linalg.norm(point1 - point2) # alternative 2

# 3. Calculating Distances
distances = []
for p1, p2 in combinations(points, 2):
    distances.append(euclideanDistance(p1, p2))

# 4. Finding the Minimum Distance
min_distance = min(distances)
print(f"Minimum distance: {min_distance}")


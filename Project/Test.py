"""Constellations"""
dic = {}
stars = [[0, 1], [16, 3], [1, 0], [2, 7], [9, 0], [4, 1], [2, 2], [8, 1]]
dist_list = []

constellations = []

for i in range(len(stars)):
    if i == len(stars) - 1:
        break
    else:
        for d in range(len(stars)):
            
        dist = ((stars[i + 1][0] - stars[i][0])**2 + (stars[i + 1][1] - stars[i][1])**2)**0.5
        dist_list.append(dist)

#
# def distance():
#     for i in range(len(stars)):
#         dist = stars[i][0]

sorted_list = sorted(dist_list)
print(sorted_list)
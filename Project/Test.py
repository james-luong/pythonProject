"""Constellations"""

dic = {}
stars = [[0, 1], [16, 3], [1, 0], [2, 7], [9, 0], [4, 1], [2, 2], [8, 1], [9, 3], [15, 5]]

dist_list = []

constellations = []

for i in range(len(stars)):

    if i == len(stars) - 1:
        break

    else:
        reset_point = True
        shortest_dist = []

        for d in range(len(stars)):
            if i == d:
                continue

            else:
                dist = ((stars[d][0] - stars[i][0])**2 + (stars[d][1] - stars[i][1])**2)**0.5

                if reset_point:
                    shortest_dist = [i, d, dist]
                    reset_point = False

                else:
                    if shortest_dist[2] > dist:
                        shortest_dist = [i, d, dist]

                    elif shortest_dist[2] == dist:
                        shortest_dist.append([i, d, dist])

        dist_list.append(shortest_dist)

for star in range(len(dist_list)):
    dist_list[star] = dist_list[star][:2]

print(dist_list)

for cons in range(len(dist_list)):
    dic[f'constellation {cons + 1}'] =

dic['constellation 1'] =  2,3
print(dic)
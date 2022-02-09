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

        for d in range(i + 1, len(stars)):
            dist = ((stars[d][0] - stars[i][0])**2 + (stars[d][1] - stars[i][1])**2)**0.5
            print(i, d, dist)

            if reset_point:
                shortest_dist = [i, d, dist]
                reset_point = False

            else:
                if shortest_dist[2] > dist:
                    shortest_dist = [i, d, dist]

                elif shortest_dist[2] == dist:
                    shortest_dist.append([i, d, dist])

        dist_list.append(shortest_dist)

print(dist_list)

def merge_overlapping_sublists(lst):
    output, refs = {}, {}
    for index, sublist in enumerate(lst):
        output[index] = set(sublist)
        for elem in sublist:
            refs[elem] = index
    changes = True
    while changes:
        changes = False
        for ref_num, sublist in list(output.items()):
            for elem in sublist:
                current_ref_num = refs[elem]
                if current_ref_num != ref_num:
                    changes = True
                    output[current_ref_num] |= sublist
                    for elem2 in sublist:
                        refs[elem2] = current_ref_num
                    output.pop(ref_num)
                    break
    return list(output.values())

print(merge_overlapping_sublists(shortest_dist))

print(dist_list)


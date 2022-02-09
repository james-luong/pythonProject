shortest_list = []

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



# time complexity: O（nlogn)
# space complexity: O（nlogn)

def finddatalocations(locations,moveFrom,moveTo)
    if not locations:
        return


    new_set = set()
    for location in locations:
        if location not in new_set:
        new_set.add(location)


    for i in range(len(moveFrom)):
        new_set.remove(moveFrom[i])
    new_set.add(moveTo[i])
    result = list(new_set)
    result.sort()
    return result



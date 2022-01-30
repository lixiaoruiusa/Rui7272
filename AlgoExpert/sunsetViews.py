# O(N) time | O(N) space

def sunsetViews(buildings, direction):
    result = []
    if not buildings: return result

    runningMaxHeight = 0

    if direction == "WEST":
        for i in range(len(buildings)):
            if buildings[i] > runningMaxHeight:
                result.append(i)
            runningMaxHeight = max(runningMaxHeight, buildings[i])

    if direction == "EAST":
        for j in reversed(range(len(buildings))):
            if buildings[j] > runningMaxHeight:
                result.append(j)
            runningMaxHeight = max(runningMaxHeight, buildings[j])
        result = result[::-1]
    return result


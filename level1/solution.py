def solution(area):

    result = []
    remaining_area = area
    covered_area = 0


    while covered_area < area:

        root = 0

        if remaining_area == 0 or remaining_area == 1:
            s = remaining_area

        n = 1
        perfect_square = 1
        while perfect_square <= remaining_area:

            n += 1
            perfect_square = n * n

        root = n - 1

        current_square = root * root

        remaining_area = remaining_area - current_square

        result.append(current_square)

        covered_area = covered_area + current_square

    return result


print(solution(15324))

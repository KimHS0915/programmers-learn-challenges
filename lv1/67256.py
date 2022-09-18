# 키패드 누르기

def solution(numbers, hand):
    answer = ""
    keypad = [[3, 1]] + [[j, i] for j in range(4) for i in range(3)]
    left_thumb, right_thumb = 10, 12
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left_thumb = number
        elif number in [3, 6, 9]:
            answer += "R"
            right_thumb = number
        else:
            row, col = keypad[number]
            lrow, lcol = keypad[left_thumb]
            rrow, rcol = keypad[right_thumb]
            left_distance = abs(row - lrow) + abs(col - lcol)
            right_distance = abs(row - rrow) + abs(col - rcol)
            if left_distance < right_distance:
                answer += "L"
                left_thumb = number
            elif right_distance < left_distance:
                answer += "R"
                right_thumb = number
            else:
                if hand == "left":
                    answer += "L"
                    left_thumb = number
                elif hand == "right":
                    answer += "R"
                    right_thumb = number
    return answer

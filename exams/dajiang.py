input_list = list(map(int, input()[1:-1].split(',')))
left, right, ans = 0, len(input_list) -1, 0
while left <  right:
    if input_list[left] < input_list[right]:
        ans = max(ans, input_list[left] * (right - left))
        left += 1
    else:
        ans = max(ans, input_list[right] * (right - left))
        right -= 1
print(ans)
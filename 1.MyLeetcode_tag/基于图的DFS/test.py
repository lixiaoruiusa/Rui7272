s = "aaabbaa"
# 输出为 a3b2a2

res = []
count = 1

left = 0
right = 0
while left < len(s)and right < len(s):

    while left < len(s) and right < len(s) and s[left] == s[right]:
        right += 1
    res.append(s[left])
    res.append(str(right - left))
    left = right

print(res)
result = "".join(res)
print(result)

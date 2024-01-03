def validate_ip(s):
    if not s:
        return -1

    nums = s.split(".")
    if len(nums) != 4:
        return -1

    # num is x1
    for num in nums:
        # handle 00
        if len(num) > 1 and num[0] == "0":
            return -1

        if num.isdigit():
            x = int(num)
            if x < 0 or x > 255:
                return -1
        else:
            return -1

    return "IPv4"


s1 = "x1.x2.x3.x4"
res1 = validate_ip(s1)
print(res1)

s2 = "0.0.0.0"
res2 = validate_ip(s2)
print(res2)

s3 = "255.255.255.255"
res3 = validate_ip(s3)
print(res3)

s4 = "01.02.03.04"
res4 = validate_ip(s4)
print(res4)

s5 = "03.04"
res5 = validate_ip(s5)
print(res5)

s6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
res6 = validate_ip(s6)
print(res6)
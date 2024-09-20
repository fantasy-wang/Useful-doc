

def sort_two_sortlists(num1, m, num2, n):
    if m == 0:
        return num2
    if n == 0:
        return num1
    big = m + n
    result = []
    num1_index = 0
    num2_index = 0
    if num1[0] >= num2[0]:
        result.append(num2[0])
        num2_index += 1
    else:
        result.append(num1[0])
        num1_index += 1
    for i in range(big):
        if num1_index < m:
            num1_value = num1[num1_index]
        else:
            result += num2[num2_index:]
            return result
        if num2_index < n:
            num2_value = num2[num2_index]
        else:
            result += num1[num1_index:]
            return result
        if num1_value <= num2_value:
            result.append(num1_value)
            num1_index += 1
        elif num1_value >= num2_value:
            result.append(num2_value)
            num2_index += 1
    return result



nums1 = [1,2,3,7,10,22]
m = 6
nums2 = [2,5,6,8,11,19,20,23]
n = 8

print(sort_two_sortlists(nums1, m, nums2, n))
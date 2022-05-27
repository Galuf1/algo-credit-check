def credit_check(str):
    lis = list(str)
    ans = []
    sum = 0
    for j, i in enumerate(lis[::-1]):
        num = int(i)
        ele = 0
        if j % 2 == 1:
            ele = num*2
        else:
            ele = num

        if ele >=10:
            ele = ele%10 + (ele-(ele%10))//10
            ans.append(ele)
        else:
            ans.append(ele)

        sum = sum + ele
    
    #print(sum)
    return "The number is valid!" if sum%10==0 else "The number is invalid!"

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"


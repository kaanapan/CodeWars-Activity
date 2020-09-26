def longest_slide_down(pyramid):
    dp = [pyramid[0][0]]
    for line in pyramid[1:]:
        new_dp = [0]*len(dp)
        for j,num in enumerate(line):
            if j == len(new_dp):
                new_dp.append(dp[j-1]+num)
            elif j == 0:
                new_dp[j] = dp[j] + num
            else:
                new_dp[j] += max(dp[j-1]+num, dp[j]+num)
        dp = new_dp
    return max(dp)
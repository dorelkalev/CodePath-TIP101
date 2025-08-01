# Aang from Avatar: The Last Airbender needs to balance his spiritual energy through meditation sessions to prepare for upcoming battles. Each day, the energy he gains from meditation is the sum of the energy gained on the two previous days.

# On days 1 & 2, he gains 1 unit of energy each. Write a function energy_on_nth_day() that accepts an integer n and returns the total amount of energy Aang has gained on day n. Use a dynamic programming approach in your solution.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

#understand
#input: integer
#output: integer

#plan 
# created 2 vars, 
# rotate the value of the variables using a temp
# use a for loop until n, 

# Time: O(n)
# Space: O(1)

def energy_on_nth_day(n):
    secondprev = firstprev = 1

    for i in range(3, n + 1): 
        temp = secondprev + firstprev
        secondprev = firstprev
        firstprev = temp
    
    return firstprev

# Example Usage:

# print(energy_on_nth_day(1))
# print(energy_on_nth_day(2))
# print(energy_on_nth_day(5))
# print(energy_on_nth_day(7))
# Example Output:

# 1
# 1
# 5
# 13



# Toph is training her earthbending skills by climbing a staircase made of rock steps. Each step requires a certain amount of energy to climb, represented by an integer array cost where cost[i] is the energy cost to step on the i-th step.

# Once Toph pays the energy cost for a step, she can either climb one or two steps. She can start from either the first step (index 0) or the second step (index 1). Help Toph minimize the total energy required to reach the top of the staircase.

# Write a function toph_training() that accepts the integer array cost and returns the minimum energy required to reach the top.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# dp[i] = min(dp[i-1], dp[i-2]) + cost[i] 
# dp[0], dp[1] can be initialized 
# using a for loop from 2 to len(dp)
# return dp[-1]
def toph_training(cost):
    dp = [0] * len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, len(dp)):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

    return min(dp[-1], dp[-2])

# Example Usage:

print(toph_training([10, 15, 20]))
print(toph_training([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# Example Output:

# 15
# Example 1 Explanation: Toph will start at index 1, pay 15 units of energy, and jump 
# two steps to the top. Total energy: 15.
# 6
# Example 2 Explanation: Toph will minimize energy by taking steps in a pattern that uses the
# least energy, resulting in a total energy cost of 6.




# Aang and Zuko take turns in a strategic duel to control the elements, with Aang going first. The duel begins with a number n representing the strength of the elements on the battlefield.

# On each turn, a player must:

# Choose any x such that 0 < x < n and n % x == 0.
# Reduce the battlefield’s strength by x, replacing n with n - x.
# If a player cannot make a move, they lose the duel.

# Write a function aang_wins() that accepts an integer n and returns True if Aang wins the duel (assuming both Aang and Zuko play optimally), and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def aang_wins(n):
    pass
# Example Usage: 
# n = 4
# aang can choose 2 or 1
# same case as aang_wins(2) or aang_wins(3) but for zuko
# dp[1:n]
# for i O(n)
# calculate all divisors for i O(i)
# for all divisors O(i)
# if they win any of them. O(1) 
#

# n = 16
# 1, 2, 4, 8
# 
print(aang_wins(2))
print(aang_wins(3))
# Example Output:

# True
# Example 1 Explanation: Aang reduces the strength by 1, and Zuko has no more moves.

# False
# Example 2 Explanation: Aang reduces the strength by 1, then Zuko does the same, leaving 
# Aang with no moves.
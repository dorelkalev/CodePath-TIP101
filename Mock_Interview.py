""""
Understand: 
Input: Tree and an integer
Output: boolean

Plan:
Recursion (trees)
Helper function that helps traverse through the tree.
    while traversing:
        track the sum in a variable
        if the sum > target sum - return False

    if at the bottom, the sum is equal to the target - return True
    if less than - return false

"""

#Implement:
def mystery_function(root, target_sum):
    sum = 0
    def helper(root, target_sum, sum):
        
        if not root:
            return sum
    
        sum += root.val
        if sum > target_sum:
            return False
        if not root.left and not root.right and sum != target_sum:
            return False
        else:
            return True

        return helper(root.left, target_sum, sum) or helper(root.right, target_sum, sum)
    
    return helper(root, target_sum, sum)
    

"""
            5
           / \
          4   8
         /     
        11    
       /  \
      7    2

    target_sum = 22

    Output: True
"""

"""
Evaluate:
Time complexity: O(n)
Space complexity: O(1)
"""

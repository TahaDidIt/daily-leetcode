class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        #Create new variables needed (n, result list)
        n = len(code)
        result = [0]*n
        
        #test print
        print("code: " + str(code))
        print("k: " + str(k))
        print("n: " + str(n))
        print(result)


        # k == 0, because its easier to get it out the way now
        if k == 0:
            return result
        
        """
        For the next two cases, our method involves using the modulo (%) operator.
        This means that if the next k element(s) in the sequence go beyond the last element of "code",
        We simply get the remainder of how far beyond it went and use that as the index.
        
        Modulo is different to pythons actual remainder function as it handles negative numbers differently,
        allowing for things to "wrap around" the divisor when going backwards.
        On top of that, a % b is always positive (for b > 0), even if a is negative.
        
        This is because for a a < 0, python's modulo adds b to it until it is positive; e.g instead (a + b) % b

        i.e. -1 % 4 is 3, instead of -1. This is perfect for a circular array or looped list idea.
        """
        
        # k > 0
        if k > 0:
            for i in range(n):
                #temporary variable to hold the sum as we iterate over the next k elements
                tempsum = 0
                for j in range(1, k + 1): #element +1 till element +k
                    tempsum += code[(i + j) % n]
                #store sum in ith position of new array
                result[i] = tempsum
            
            return result
        
        # k < 0
        if k < 0:
            for i in range(n):
                tempsum = 0
                for j in range(k, 0):
                    tempsum += code[(i + j) % n]
                result[i] = tempsum

            return result



### OUTSIDE LEETCODE ~ TEST WITH YOUR OWN EXAMPLES

# Create solution object instance
solutiontest = Solution()

# Test values
code = [0, 1, 2, 3]
k = 3

print(solutiontest.decrypt(code, k))

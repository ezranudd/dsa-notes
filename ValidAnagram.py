from collections import Counter

# Given two lowercase strings s and t, return true if the two strings are
# anagrams of each other and false otherwise.
class Solution:

    # Brute Force
    # Time: O(nlogn + mlogm)
    # Space: O(n + m)
    def isAnagramBruteForce(self, s: str, t: str) -> bool:

        # Check length
        if len(s) != len(t):
            return False

        # Sort both strings and compare
        return sorted(s) == sorted(t)

    # Hash Map
    # Time: O(n + m)
    # Space: O(1) since we have at most 26 different chars
    def isAnagramHash(self, s: str, t: str) -> bool:

        # First check length
        if len(s) != len(t):
            return False

        # Create two hash maps
        countS, countT = {}, {}

        # Count frequency of each letter and store
        # We use .get to provide a default count for missing keys
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Compare
        return countS == countT

    # Array
    # Time: O(n + m)
    # Space: O(1) since we have at most 26 chars
    def isAnagramArray(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True
    
    # In python, we can do this:
    # Same time/space complexity as Hash Map
    def isAnagramCounter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    # Sorted solution
    # Time: O(nlogn + mlogm)
    # Space: O(n + m) in Python because sorted() creates new lists
    def isAnagramSorted(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

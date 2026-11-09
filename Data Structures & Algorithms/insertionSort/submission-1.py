class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Handle empty array edge case
        if not pairs:
            return []
            
        res = []
        # Record the initial state
        res.append(list(pairs))
        
        for i in range(1, len(pairs)):
            j = i
            # Shift elements to the left while the current key is smaller than the previous
            while j > 0 and pairs[j].key < pairs[j - 1].key:
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1
            # Append a copy of the current state of the array
            res.append(list(pairs))
            
        return res
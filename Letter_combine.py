class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
       
        phone_map = {"2":"abc", "3":"def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []

        def backtrack(current,index):
            if len(current)==len(digits):
                return result.append("".join(current))
            current_d = digits[index]
            letter_pool = phone_map[current_d]

            for letter in letter_pool:
                current.append(letter)
                backtrack(current, index+1)
                current.pop()
        backtrack([],0)
        return result   

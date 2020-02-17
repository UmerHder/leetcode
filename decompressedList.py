
class Solution:
    def decompressRLElist(self, nums):
        adjacent_list = []
        freq_list = []
        
        for n in nums:
            adjacent_list.append(n)
            if len(adjacent_list) == 2:
                for i in range(adjacent_list[0]):
                    freq_list.append(adjacent_list[1])
                adjacent_list = []
        
        return freq_list
            
if __name__ == '__main__':
    solution = Solution()
    rle_list = [1,2,3,4]
    print(solution.decompressRLElist(rle_list))
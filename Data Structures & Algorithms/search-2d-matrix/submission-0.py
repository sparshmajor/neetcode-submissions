class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row_binary_search():
            l = 0
            r = len(matrix)-1
            while l<r:
                mid = l+(r-l)//2
                if matrix[mid][-1] >= target:
                    r=mid
                else:
                    l= mid+1
            return l

        def binary_search(row):
            l = 0
            r = len(matrix[row])-1
            while l<r:
                mid = l+(r-l)//2
                if target <= matrix[row][mid]:
                    r=mid
                else:
                    l= mid+1
            return l if target== matrix[row][l] else -1 

        row =  find_row_binary_search() 
        print(row)
        search = binary_search(row)
        print("search",search)
        return False if search == -1 else True




        
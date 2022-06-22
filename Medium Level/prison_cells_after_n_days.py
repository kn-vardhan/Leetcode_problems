class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        new_cells = [0] * len(cells)
        if n % 14 != 0:
            n = n % 14
        else:
            n = 14
            
        while n > 0:
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    new_cells[i] = 1
                else:
                    new_cells[i] = 0
            cells = new_cells.copy()
            n -= 1
            
        return new_cells



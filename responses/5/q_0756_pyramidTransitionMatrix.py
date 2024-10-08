from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def build_pyramid(row, next_row, index, current_layer):
            if row == len(bottom) - 1:  # If we have reached the last row
                if len(next_row) == 1:  # If we have reached the top of the pyramid
                    return True
                else:
                    return build_pyramid(next_row, '', 0, 0)  # Move to the next row
            else:
                block = allowed[current_layer][index]  # Get the potential block for the current position
                if index == len(allowed[current_layer]) - 1:  # If we have reached the end of the current layer
                    return build_pyramid(row, next_row + block, 0, current_layer + 1)  # Move to the next layer
                else:
                    # Check if the combination of blocks is allowed, if so, move to the next position
                    if row + 1 < len(bottom) and bottom[row:row + 2] + block in allowed[current_layer]:
                        if build_pyramid(row, next_row + block, index + 1, current_layer):
                            return True
                    return build_pyramid(row, next_row, index + 1, current_layer)

        return build_pyramid(bottom, '', 0, 0)

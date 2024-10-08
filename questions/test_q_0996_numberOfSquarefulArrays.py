import pytest
from q_0996_numberOfSquarefulArrays import Solution


@pytest.mark.parametrize("nums, output", [([1, 17, 8], 2), ([2, 2, 2], 1)])
class TestSolution:
    def test_numSquarefulPerms(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.numSquarefulPerms(
                nums,
            )
            == output
        )

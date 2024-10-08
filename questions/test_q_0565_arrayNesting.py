import pytest
from q_0565_arrayNesting import Solution


@pytest.mark.parametrize("nums, output", [([5, 4, 0, 3, 1, 6, 2], 4), ([0, 1, 2], 1)])
class TestSolution:
    def test_arrayNesting(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.arrayNesting(
                nums,
            )
            == output
        )

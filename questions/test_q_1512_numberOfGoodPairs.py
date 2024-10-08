import pytest
from q_1512_numberOfGoodPairs import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 1, 1, 3], 4), ([1, 1, 1, 1], 6), ([1, 2, 3], 0)]
)
class TestSolution:
    def test_numIdenticalPairs(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.numIdenticalPairs(
                nums,
            )
            == output
        )

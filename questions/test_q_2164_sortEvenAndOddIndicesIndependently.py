import pytest
from q_2164_sortEvenAndOddIndicesIndependently import Solution


@pytest.mark.parametrize(
    "nums, output", [([4, 1, 2, 3], [2, 3, 4, 1]), ([2, 1], [2, 1])]
)
class TestSolution:
    def test_sortEvenOdd(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.sortEvenOdd(
                nums,
            )
            == output
        )

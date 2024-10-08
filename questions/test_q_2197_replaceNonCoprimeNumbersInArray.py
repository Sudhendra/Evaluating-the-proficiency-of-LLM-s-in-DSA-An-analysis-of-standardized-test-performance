import pytest
from q_2197_replaceNonCoprimeNumbersInArray import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([6, 4, 3, 2, 7, 6, 2], [12, 7, 6]), ([2, 2, 1, 1, 3, 3, 3], [2, 1, 1, 3])],
)
class TestSolution:
    def test_replaceNonCoprimes(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.replaceNonCoprimes(
                nums,
            )
            == output
        )

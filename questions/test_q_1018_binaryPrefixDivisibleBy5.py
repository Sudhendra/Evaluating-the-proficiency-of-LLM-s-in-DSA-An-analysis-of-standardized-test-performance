import pytest
from q_1018_binaryPrefixDivisibleBy5 import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([0, 1, 1], [True, False, False]), ([1, 1, 1], [False, False, False])],
)
class TestSolution:
    def test_prefixesDivBy5(self, nums: List[int], output: List[bool]):
        sc = Solution()
        assert (
            sc.prefixesDivBy5(
                nums,
            )
            == output
        )

import pytest
from q_2932_maximumStrongPairXorI import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 2, 3, 4, 5], 7), ([10, 100], 0), ([5, 6, 25, 30], 7)]
)
class TestSolution:
    def test_maximumStrongPairXor(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maximumStrongPairXor(
                nums,
            )
            == output
        )

import pytest
from q_0810_chalkboardXorGame import Solution


@pytest.mark.parametrize(
    "nums, output", [([1, 1, 2], False), ([0, 1], True), ([1, 2, 3], True)]
)
class TestSolution:
    def test_xorGame(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.xorGame(
                nums,
            )
            == output
        )

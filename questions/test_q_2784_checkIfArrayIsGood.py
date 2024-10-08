import pytest
from q_2784_checkIfArrayIsGood import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([2, 1, 3], False),
        ([1, 3, 3, 2], True),
        ([1, 1], True),
        ([3, 4, 4, 1, 2, 1], False),
    ],
)
class TestSolution:
    def test_isGood(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.isGood(
                nums,
            )
            == output
        )

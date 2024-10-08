import pytest
from q_1752_checkIfArrayIsSortedAndRotated import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 4, 5, 1, 2], True), ([2, 1, 3, 4], False), ([1, 2, 3], True)]
)
class TestSolution:
    def test_check(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.check(
                nums,
            )
            == output
        )

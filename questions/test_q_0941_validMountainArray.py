import pytest
from q_0941_validMountainArray import Solution


@pytest.mark.parametrize(
    "arr, output", [([2, 1], False), ([3, 5, 5], False), ([0, 3, 2, 1], True)]
)
class TestSolution:
    def test_validMountainArray(self, arr: List[int], output: bool):
        sc = Solution()
        assert (
            sc.validMountainArray(
                arr,
            )
            == output
        )

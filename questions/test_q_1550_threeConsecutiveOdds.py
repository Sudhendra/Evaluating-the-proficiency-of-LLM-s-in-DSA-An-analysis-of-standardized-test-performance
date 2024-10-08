import pytest
from q_1550_threeConsecutiveOdds import Solution


@pytest.mark.parametrize(
    "arr, output", [([2, 6, 4, 1], False), ([1, 2, 34, 3, 4, 5, 7, 23, 12], True)]
)
class TestSolution:
    def test_threeConsecutiveOdds(self, arr: List[int], output: bool):
        sc = Solution()
        assert (
            sc.threeConsecutiveOdds(
                arr,
            )
            == output
        )

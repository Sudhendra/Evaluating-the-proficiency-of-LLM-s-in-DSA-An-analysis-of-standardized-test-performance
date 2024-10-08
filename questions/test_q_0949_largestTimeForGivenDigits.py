import pytest
from q_0949_largestTimeForGivenDigits import Solution


@pytest.mark.parametrize("arr, output", [([1, 2, 3, 4], "23:41"), ([5, 5, 5, 5], "")])
class TestSolution:
    def test_largestTimeFromDigits(self, arr: List[int], output: str):
        sc = Solution()
        assert (
            sc.largestTimeFromDigits(
                arr,
            )
            == output
        )

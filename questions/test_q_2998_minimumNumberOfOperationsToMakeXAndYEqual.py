import pytest
from q_2998_minimumNumberOfOperationsToMakeXAndYEqual import Solution


@pytest.mark.parametrize("x, y, output", [(26, 1, 3), (54, 2, 4), (25, 30, 5)])
class TestSolution:
    def test_minimumOperationsToMakeEqual(self, x: int, y: int, output: int):
        sc = Solution()
        assert (
            sc.minimumOperationsToMakeEqual(
                x,
                y,
            )
            == output
        )

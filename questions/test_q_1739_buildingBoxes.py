import pytest
from q_1739_buildingBoxes import Solution


@pytest.mark.parametrize("n, output", [(3, 3), (4, 3), (10, 6)])
class TestSolution:
    def test_minimumBoxes(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.minimumBoxes(
                n,
            )
            == output
        )

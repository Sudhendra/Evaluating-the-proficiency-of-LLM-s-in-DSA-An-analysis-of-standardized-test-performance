import pytest
from q_0119_pascalsTriangleIi import Solution


@pytest.mark.parametrize("rowIndex, output", [(3, [1, 3, 3, 1]), (0, [1]), (1, [1, 1])])
class TestSolution:
    def test_getRow(self, rowIndex: int, output: List[int]):
        sc = Solution()
        assert (
            sc.getRow(
                rowIndex,
            )
            == output
        )

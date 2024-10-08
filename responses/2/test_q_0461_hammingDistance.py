import pytest
from q_0461_hammingDistance import Solution


@pytest.mark.parametrize("x, y, output", [(1, 4, 2), (3, 1, 1)])
class TestSolution:
    def test_hammingDistance(self, x: int, y: int, output: int):
        sc = Solution()
        assert (
            sc.hammingDistance(
                x,
                y,
            )
            == output
        )

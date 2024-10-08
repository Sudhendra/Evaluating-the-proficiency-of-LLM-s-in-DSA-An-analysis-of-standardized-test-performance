import pytest
from q_1362_closestDivisors import Solution


@pytest.mark.parametrize("num, output", [(8, [3, 3]), (123, [5, 25]), (999, [40, 25])])
class TestSolution:
    def test_closestDivisors(self, num: int, output: List[int]):
        sc = Solution()
        assert (
            sc.closestDivisors(
                num,
            )
            == output
        )

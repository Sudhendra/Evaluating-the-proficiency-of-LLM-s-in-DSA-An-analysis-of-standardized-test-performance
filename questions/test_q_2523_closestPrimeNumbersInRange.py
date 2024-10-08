import pytest
from q_2523_closestPrimeNumbersInRange import Solution


@pytest.mark.parametrize("left, right, output", [(10, 19, [11, 13]), (4, 6, [-1, -1])])
class TestSolution:
    def test_closestPrimes(self, left: int, right: int, output: List[int]):
        sc = Solution()
        assert (
            sc.closestPrimes(
                left,
                right,
            )
            == output
        )

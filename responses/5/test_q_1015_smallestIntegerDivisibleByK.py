import pytest
from q_1015_smallestIntegerDivisibleByK import Solution


@pytest.mark.parametrize("k, output", [(1, 1), (2, -1), (3, 3)])
class TestSolution:
    def test_smallestRepunitDivByK(self, k: int, output: int):
        sc = Solution()
        assert (
            sc.smallestRepunitDivByK(
                k,
            )
            == output
        )

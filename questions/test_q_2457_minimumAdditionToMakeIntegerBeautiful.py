import pytest
from q_2457_minimumAdditionToMakeIntegerBeautiful import Solution


@pytest.mark.parametrize("n, target, output", [(16, 6, 4), (467, 6, 33), (1, 1, 0)])
class TestSolution:
    def test_makeIntegerBeautiful(self, n: int, target: int, output: int):
        sc = Solution()
        assert (
            sc.makeIntegerBeautiful(
                n,
                target,
            )
            == output
        )

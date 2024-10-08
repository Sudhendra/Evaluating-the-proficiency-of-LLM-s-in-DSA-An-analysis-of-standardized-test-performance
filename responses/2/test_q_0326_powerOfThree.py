import pytest
from q_0326_powerOfThree import Solution


@pytest.mark.parametrize("n, output", [(27, True), (0, False), (-1, False)])
class TestSolution:
    def test_isPowerOfThree(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.isPowerOfThree(
                n,
            )
            == output
        )

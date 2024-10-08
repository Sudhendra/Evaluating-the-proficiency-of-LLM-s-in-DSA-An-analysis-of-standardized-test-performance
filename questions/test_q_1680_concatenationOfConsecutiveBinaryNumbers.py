import pytest
from q_1680_concatenationOfConsecutiveBinaryNumbers import Solution


@pytest.mark.parametrize("n, output", [(1, 1), (3, 27), (12, 505379714)])
class TestSolution:
    def test_concatenatedBinary(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.concatenatedBinary(
                n,
            )
            == output
        )

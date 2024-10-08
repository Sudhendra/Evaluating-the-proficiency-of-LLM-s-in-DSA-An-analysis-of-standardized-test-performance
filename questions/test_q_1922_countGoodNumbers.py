import pytest
from q_1922_countGoodNumbers import Solution


@pytest.mark.parametrize("n, output", [(1, 5), (4, 400), (50, 564908303)])
class TestSolution:
    def test_countGoodNumbers(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countGoodNumbers(
                n,
            )
            == output
        )

import pytest
from q_2376_countSpecialIntegers import Solution


@pytest.mark.parametrize("n, output", [(20, 19), (5, 5), (135, 110)])
class TestSolution:
    def test_countSpecialNumbers(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countSpecialNumbers(
                n,
            )
            == output
        )

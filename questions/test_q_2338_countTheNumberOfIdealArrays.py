import pytest
from q_2338_countTheNumberOfIdealArrays import Solution


@pytest.mark.parametrize("n, maxValue, output", [(2, 5, 10), (5, 3, 11)])
class TestSolution:
    def test_idealArrays(self, n: int, maxValue: int, output: int):
        sc = Solution()
        assert (
            sc.idealArrays(
                n,
                maxValue,
            )
            == output
        )

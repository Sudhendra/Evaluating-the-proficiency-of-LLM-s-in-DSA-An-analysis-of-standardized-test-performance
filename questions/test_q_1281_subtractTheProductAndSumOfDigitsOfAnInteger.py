import pytest
from q_1281_subtractTheProductAndSumOfDigitsOfAnInteger import Solution


@pytest.mark.parametrize("n, output", [(234, 15), (4421, 21)])
class TestSolution:
    def test_subtractProductAndSum(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.subtractProductAndSum(
                n,
            )
            == output
        )

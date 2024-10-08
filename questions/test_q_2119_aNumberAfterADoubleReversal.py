import pytest
from q_2119_aNumberAfterADoubleReversal import Solution


@pytest.mark.parametrize("num, output", [(526, True), (1800, False), (0, True)])
class TestSolution:
    def test_isSameAfterReversals(self, num: int, output: bool):
        sc = Solution()
        assert (
            sc.isSameAfterReversals(
                num,
            )
            == output
        )

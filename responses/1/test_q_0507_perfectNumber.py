import pytest
from q_0507_perfectNumber import Solution


@pytest.mark.parametrize("num, output", [(28, True), (7, False)])
class TestSolution:
    def test_checkPerfectNumber(self, num: int, output: bool):
        sc = Solution()
        assert (
            sc.checkPerfectNumber(
                num,
            )
            == output
        )

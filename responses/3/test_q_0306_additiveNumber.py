import pytest
from q_0306_additiveNumber import Solution


@pytest.mark.parametrize("output", [(True), (True)])
class TestSolution:
    def test_isAdditiveNumber(self, num: str, output: bool):
        sc = Solution()
        assert sc.isAdditiveNumber() == output

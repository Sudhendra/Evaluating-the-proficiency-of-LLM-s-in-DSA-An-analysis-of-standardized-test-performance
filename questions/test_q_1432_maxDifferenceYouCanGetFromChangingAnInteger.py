import pytest
from q_1432_maxDifferenceYouCanGetFromChangingAnInteger import Solution


@pytest.mark.parametrize("num, output", [(555, 888), (9, 8)])
class TestSolution:
    def test_maxDiff(self, num: int, output: int):
        sc = Solution()
        assert (
            sc.maxDiff(
                num,
            )
            == output
        )

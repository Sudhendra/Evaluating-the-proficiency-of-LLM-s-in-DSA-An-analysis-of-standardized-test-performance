import pytest
from q_1399_countLargestGroup import Solution


@pytest.mark.parametrize("n, output", [(13, 4), (2, 2)])
class TestSolution:
    def test_countLargestGroup(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.countLargestGroup(
                n,
            )
            == output
        )

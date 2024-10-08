import pytest
from q_1663_smallestStringWithAGivenNumericValue import Solution


@pytest.mark.parametrize("n, k, output", [(3, 27, "aay"), (5, 73, "aaszz")])
class TestSolution:
    def test_getSmallestString(self, n: int, k: int, output: str):
        sc = Solution()
        assert (
            sc.getSmallestString(
                n,
                k,
            )
            == output
        )

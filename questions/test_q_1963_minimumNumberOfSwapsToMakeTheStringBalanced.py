import pytest
from q_1963_minimumNumberOfSwapsToMakeTheStringBalanced import Solution


@pytest.mark.parametrize("s, output", [("][][", 1), ("]]][[[", 2), ("[]", 0)])
class TestSolution:
    def test_minSwaps(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minSwaps(
                s,
            )
            == output
        )

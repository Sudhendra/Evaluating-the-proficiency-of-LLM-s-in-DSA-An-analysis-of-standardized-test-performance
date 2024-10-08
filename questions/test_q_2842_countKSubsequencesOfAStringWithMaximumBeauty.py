import pytest
from q_2842_countKSubsequencesOfAStringWithMaximumBeauty import Solution


@pytest.mark.parametrize("s, k, output", [("bcca", 2, 4), ("abbcd", 4, 2)])
class TestSolution:
    def test_countKSubsequencesWithMaxBeauty(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.countKSubsequencesWithMaxBeauty(
                s,
                k,
            )
            == output
        )

import pytest
from q_2514_countAnagrams import Solution


@pytest.mark.parametrize("s, output", [("too hot", 18), ("aa", 1)])
class TestSolution:
    def test_countAnagrams(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countAnagrams(
                s,
            )
            == output
        )

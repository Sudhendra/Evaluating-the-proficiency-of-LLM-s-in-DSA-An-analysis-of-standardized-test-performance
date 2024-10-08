import pytest
from q_1309_decryptStringFromAlphabetToIntegerMapping import Solution


@pytest.mark.parametrize("s, output", [("10#11#12", "jkab"), ("1326#", "acz")])
class TestSolution:
    def test_freqAlphabets(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.freqAlphabets(
                s,
            )
            == output
        )

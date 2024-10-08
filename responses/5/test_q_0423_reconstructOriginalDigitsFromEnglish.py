import pytest
from q_0423_reconstructOriginalDigitsFromEnglish import Solution


@pytest.mark.parametrize("s, output", [("owoztneoer", "012"), ("fviefuro", "45")])
class TestSolution:
    def test_originalDigits(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.originalDigits(
                s,
            )
            == output
        )

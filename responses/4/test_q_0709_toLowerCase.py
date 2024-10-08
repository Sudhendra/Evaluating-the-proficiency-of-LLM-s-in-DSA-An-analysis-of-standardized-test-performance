import pytest
from q_0709_toLowerCase import Solution


@pytest.mark.parametrize(
    "s, output", [("Hello", "hello"), ("here", "here"), ("LOVELY", "lovely")]
)
class TestSolution:
    def test_toLowerCase(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.toLowerCase(
                s,
            )
            == output
        )

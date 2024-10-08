import pytest
from q_0820_shortEncodingOfWords import Solution


@pytest.mark.parametrize("words, output", [(["time", "me", "bell"], 10), (["t"], 2)])
class TestSolution:
    def test_minimumLengthEncoding(self, words: List[str], output: int):
        sc = Solution()
        assert (
            sc.minimumLengthEncoding(
                words,
            )
            == output
        )

import pytest
from q_2423_removeLetterToEqualizeFrequency import Solution


@pytest.mark.parametrize("word, output", [("abcc", True), ("aazz", False)])
class TestSolution:
    def test_equalFrequency(self, word: str, output: bool):
        sc = Solution()
        assert (
            sc.equalFrequency(
                word,
            )
            == output
        )

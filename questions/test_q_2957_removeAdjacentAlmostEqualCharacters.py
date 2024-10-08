import pytest
from q_2957_removeAdjacentAlmostEqualCharacters import Solution


@pytest.mark.parametrize("word, output", [("aaaaa", 2), ("abddez", 2), ("zyxyxyz", 3)])
class TestSolution:
    def test_removeAlmostEqualCharacters(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.removeAlmostEqualCharacters(
                word,
            )
            == output
        )

import pytest
from q_3016_minimumNumberOfPushesToTypeWordIi import Solution


@pytest.mark.parametrize(
    "word, output", [("abcde", 5), ("xyzxyzxyzxyz", 12), ("aabbccddeeffgghhiiiiii", 24)]
)
class TestSolution:
    def test_minimumPushes(self, word: str, output: int):
        sc = Solution()
        assert (
            sc.minimumPushes(
                word,
            )
            == output
        )

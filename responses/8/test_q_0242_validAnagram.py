import pytest
from q_0242_validAnagram import Solution


@pytest.mark.parametrize(
    "s, t, output", [("anagram", "nagaram", True), ("rat", "car", False)]
)
class TestSolution:
    def test_isAnagram(self, s: str, t: str, output: bool):
        sc = Solution()
        assert (
            sc.isAnagram(
                s,
                t,
            )
            == output
        )

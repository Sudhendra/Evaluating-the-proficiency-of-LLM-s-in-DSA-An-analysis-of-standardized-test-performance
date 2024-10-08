import pytest
from q_2516_takeKOfEachCharacterFromLeftAndRight import Solution


@pytest.mark.parametrize("s, k, output", [("aabaaaacaabc", 2, 8), ("a", 1, -1)])
class TestSolution:
    def test_takeCharacters(self, s: str, k: int, output: int):
        sc = Solution()
        assert (
            sc.takeCharacters(
                s,
                k,
            )
            == output
        )

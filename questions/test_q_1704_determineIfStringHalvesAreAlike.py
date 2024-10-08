import pytest
from q_1704_determineIfStringHalvesAreAlike import Solution


@pytest.mark.parametrize("s, output", [("book", True), ("textbook", False)])
class TestSolution:
    def test_halvesAreAlike(self, s: str, output: bool):
        sc = Solution()
        assert (
            sc.halvesAreAlike(
                s,
            )
            == output
        )

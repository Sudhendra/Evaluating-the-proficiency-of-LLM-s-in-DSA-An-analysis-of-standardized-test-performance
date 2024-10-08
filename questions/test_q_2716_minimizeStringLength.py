import pytest
from q_2716_minimizeStringLength import Solution


@pytest.mark.parametrize("s, output", [("aaabc", 3), ("cbbd", 3), ("dddaaa", 2)])
class TestSolution:
    def test_minimizedStringLength(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minimizedStringLength(
                s,
            )
            == output
        )

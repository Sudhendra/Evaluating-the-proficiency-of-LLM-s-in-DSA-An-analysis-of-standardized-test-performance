import pytest
from q_2266_countNumberOfTexts import Solution


@pytest.mark.parametrize(
    "pressedKeys, output",
    [("22233", 8), ("222222222222222222222222222222222222", 82876089)],
)
class TestSolution:
    def test_countTexts(self, pressedKeys: str, output: int):
        sc = Solution()
        assert (
            sc.countTexts(
                pressedKeys,
            )
            == output
        )

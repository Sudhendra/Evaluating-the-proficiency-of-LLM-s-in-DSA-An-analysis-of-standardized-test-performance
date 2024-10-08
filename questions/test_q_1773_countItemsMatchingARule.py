import pytest
from q_1773_countItemsMatchingARule import Solution


@pytest.mark.parametrize(
    "items, ruleKey, ruleValue, output",
    [
        (
            [
                ["phone", "blue", "pixel"],
                ["computer", "silver", "lenovo"],
                ["phone", "gold", "iphone"],
            ],
            "color",
            "silver",
            1,
        ),
        (
            [
                ["phone", "blue", "pixel"],
                ["computer", "silver", "phone"],
                ["phone", "gold", "iphone"],
            ],
            "type",
            "phone",
            2,
        ),
    ],
)
class TestSolution:
    def test_countMatches(
        self, items: List[List[str]], ruleKey: str, ruleValue: str, output: int
    ):
        sc = Solution()
        assert (
            sc.countMatches(
                items,
                ruleKey,
                ruleValue,
            )
            == output
        )

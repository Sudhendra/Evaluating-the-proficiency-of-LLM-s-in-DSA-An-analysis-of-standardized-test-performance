import pytest
from q_1268_searchSuggestionsSystem import Solution


@pytest.mark.parametrize(
    "products, searchWord, output",
    [
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse",
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            ["havana"],
            "havana",
            [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        ),
    ],
)
class TestSolution:
    def test_suggestedProducts(
        self, products: List[str], searchWord: str, output: List[List[str]]
    ):
        sc = Solution()
        assert (
            sc.suggestedProducts(
                products,
                searchWord,
            )
            == output
        )

import pytest
from q_2456_mostPopularVideoCreator import Solution


@pytest.mark.parametrize(
    "creators, ids, views, output",
    [
        (
            ["alice", "bob", "alice", "chris"],
            ["one", "two", "three", "four"],
            [5, 10, 5, 4],
            [["alice", "one"], ["bob", "two"]],
        ),
        (["alice", "alice", "alice"], ["a", "b", "c"], [1, 2, 2], [["alice", "b"]]),
    ],
)
class TestSolution:
    def test_mostPopularCreator(
        self,
        creators: List[str],
        ids: List[str],
        views: List[int],
        output: List[List[str]],
    ):
        sc = Solution()
        assert (
            sc.mostPopularCreator(
                creators,
                ids,
                views,
            )
            == output
        )

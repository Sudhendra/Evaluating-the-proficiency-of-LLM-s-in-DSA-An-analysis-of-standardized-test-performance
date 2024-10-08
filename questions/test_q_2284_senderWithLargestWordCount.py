import pytest
from q_2284_senderWithLargestWordCount import Solution


@pytest.mark.parametrize(
    "messages, senders, output",
    [
        (
            [
                "Hello userTwooo",
                "Hi userThree",
                "Wonderful day Alice",
                "Nice day userThree",
            ],
            ["Alice", "userTwo", "userThree", "Alice"],
            "Alice",
        ),
        (
            ["How is leetcode for everyone", "Leetcode is useful for practice"],
            ["Bob", "Charlie"],
            "Charlie",
        ),
    ],
)
class TestSolution:
    def test_largestWordCount(
        self, messages: List[str], senders: List[str], output: str
    ):
        sc = Solution()
        assert (
            sc.largestWordCount(
                messages,
                senders,
            )
            == output
        )

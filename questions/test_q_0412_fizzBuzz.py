import pytest
from q_0412_fizzBuzz import Solution


@pytest.mark.parametrize(
    "n, output",
    [
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
class TestSolution:
    def test_fizzBuzz(self, n: int, output: List[str]):
        sc = Solution()
        assert (
            sc.fizzBuzz(
                n,
            )
            == output
        )

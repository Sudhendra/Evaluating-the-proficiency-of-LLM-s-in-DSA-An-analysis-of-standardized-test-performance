import pytest
from q_2719_countOfIntegers import Solution


@pytest.mark.parametrize(
    "num1, num2, min_sum, max_sum, output", [("1", "12", 1, 8, 11), ("1", "5", 1, 5, 5)]
)
class TestSolution:
    def test_count(self, num1: str, num2: str, min_sum: int, max_sum: int, output: int):
        sc = Solution()
        assert (
            sc.count(
                num1,
                num2,
                min_sum,
                max_sum,
            )
            == output
        )

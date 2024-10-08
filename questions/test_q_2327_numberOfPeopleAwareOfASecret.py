import pytest
from q_2327_numberOfPeopleAwareOfASecret import Solution


@pytest.mark.parametrize("n, delay, forget, output", [(6, 2, 4, 5), (4, 1, 3, 6)])
class TestSolution:
    def test_peopleAwareOfSecret(self, n: int, delay: int, forget: int, output: int):
        sc = Solution()
        assert (
            sc.peopleAwareOfSecret(
                n,
                delay,
                forget,
            )
            == output
        )

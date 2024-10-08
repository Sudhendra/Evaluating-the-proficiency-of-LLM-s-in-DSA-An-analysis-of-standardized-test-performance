import pytest
from q_2305_fairDistributionOfCookies import Solution


@pytest.mark.parametrize(
    "cookies, k, output",
    [([8, 15, 10, 20, 8], 2, 31), ([6, 1, 3, 2, 2, 4, 1, 2], 3, 7)],
)
class TestSolution:
    def test_distributeCookies(self, cookies: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.distributeCookies(
                cookies,
                k,
            )
            == output
        )

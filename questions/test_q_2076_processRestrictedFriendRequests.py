import pytest
from q_2076_processRestrictedFriendRequests import Solution


@pytest.mark.parametrize(
    "n, restrictions, requests, output",
    [
        (3, [[0, 1]], [[0, 2], [2, 1]], [True, False]),
        (3, [[0, 1]], [[1, 2], [0, 2]], [True, False]),
        (
            5,
            [[0, 1], [1, 2], [2, 3]],
            [[0, 4], [1, 2], [3, 1], [3, 4]],
            [True, False, True, False],
        ),
    ],
)
class TestSolution:
    def test_friendRequests(
        self,
        n: int,
        restrictions: List[List[int]],
        requests: List[List[int]],
        output: List[bool],
    ):
        sc = Solution()
        assert (
            sc.friendRequests(
                n,
                restrictions,
                requests,
            )
            == output
        )

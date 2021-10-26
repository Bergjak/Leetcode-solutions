from math import sqrt


class Solution:
    def minimumBoxes(self, n: int) -> int:
        # If we put mid in our function and mid is not a triangular number, then we will
        # have an imperfect pyramid. This will cause us to have to deposit a diagonal line of boxes
        # on the floor. Say that diagonal line placed on the floor is of length x. Then on the next
        # level of the pyramid, we can place an extra x-1 blocks, then x-2, x-3, ... x-k on the k'th level
        # where the 0th level is the floor.

        # We place the extra blocks as a diagonal because it allows for optimal packing. Here is an illustration:
        # Say we have the base    ....                     ....
        #                          ...    add Diagonal     ,...
        #                           ..    ============>     ,..
        #                            .                       ,.
        #                                                     ,

        def isPossible(base):
            arg = int(sqrt(1 / 4 + 2 * base) - 1 / 2)
            perfect_base = arg * (arg + 1) // 2

            diagonal_on_floor = base - perfect_base
            extra_blocks_of_pyramid_from_diagonal = diagonal_on_floor * (diagonal_on_floor - 1) // 2
            pyramid_on_top_of_base = (arg - 1) * arg * (arg + 1) // 6  # This is the sum of the first arg-1 triangular numbers

            # So, base is the base, pyramid_on_top_of_base is the perfect pyramid on top of the base, and extra_blocks_of_pyramid_from_diagonal is
            # all the extra blocks we get on the pyramid_on_top_of_base from having that diagonal be an addition to the base.
            # Notice that base actually contains the extra diagonal on the floor, hence we have diagonal_on_floor = base - perfect_base.

            return base + pyramid_on_top_of_base + extra_blocks_of_pyramid_from_diagonal >= n

        left, right = 0, n
        while left + 1 < right:
            mid = (right + left) // 2

            if isPossible(mid):
                right = mid
            else:
                left = mid

        return left + 1
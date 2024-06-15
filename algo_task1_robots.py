"""Вычисление необходимого числа платформ для перевозки роботов. 114868176."""


def platforms_count(robot_weights: list[int], platform_limit: int) -> int:
    """Вычисление необходимого числа платформ."""
    robots_sorted: list[int] = sorted(robot_weights)
    platforms_required: int = 0

    lightest_pos: int = 0
    heaviest_pos: int = len(robots_sorted) - 1

    while lightest_pos <= heaviest_pos:
        total_weight = (
            robots_sorted[lightest_pos] + robots_sorted[heaviest_pos]
        )

        if total_weight <= platform_limit:
            lightest_pos += 1

        platforms_required += 1
        heaviest_pos -= 1

    return platforms_required


if __name__ == '__main__':
    robot_weights = [int(robot) for robot in input().split()]
    platform_limit = input()
    print(platforms_count(robot_weights, platform_limit))

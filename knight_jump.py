# -*- coding: utf-8 -*-
"""
knight_jump.py

跳马问题：给定棋盘起点和终点，判断中国象棋马能否跳到终点，并输出所有可行路径。

用法示例：
    python knight_jump.py

作者：GitHub Copilot
日期：2025-06-25
"""
from typing import List, Tuple


def knight_jumps(
    start: Tuple[int, int], target: Tuple[int, int], board_size: int = 8
) -> List[List[Tuple[int, int]]]:
    """
    递归查找所有从 start 跳到 target 的路径。
    :param start: 起点坐标 (x, y)
    :param target: 终点坐标 (x, y)
    :param board_size: 棋盘大小，默认为8（8x8国际象棋棋盘）
    :return: 所有可行路径，每条路径是坐标元组的列表
    """
    moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    paths = []
    visited = set()

    def dfs(x, y, path):
        if (x, y) == target:
            paths.append(path[:])
            return
        visited.add((x, y))
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < board_size
                and 0 <= ny < board_size
                and (nx, ny) not in visited
            ):
                path.append((nx, ny))
                dfs(nx, ny, path)
                path.pop()
        visited.remove((x, y))

    dfs(start[0], start[1], [start])
    return paths


def main():
    """
    主函数：输入起点和终点，输出所有可行路径。
    """
    # 示例：从 (0, 0) 跳到 (2, 1)
    start = (0, 0)
    target = (2, 1)
    board_size = 8
    print(f"起点: {start}, 终点: {target}, 棋盘大小: {board_size}x{board_size}")
    paths = knight_jumps(start, target, board_size)
    if not paths:
        print("无法跳到终点！")
    else:
        print(f"共找到 {len(paths)} 条路径：")
        for idx, path in enumerate(paths, 1):
            print(f"路径{idx}: {path}")


if __name__ == "__main__":
    main()

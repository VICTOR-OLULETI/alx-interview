#!/usr/bin/python3
"""
    0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
        This function determines if all the boxes can
        be opened
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]
    while queue:
        box = queue[0]
        queue.remove(box)
        for key in boxes[box]:
            try:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
            except IndexError:
                continue
    return all(visited)

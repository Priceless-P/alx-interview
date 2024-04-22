#!/usr/bin/python3

"""Lockboxes"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    opened = [False] * len(boxes)
    # first box is already open
    opened[0] = True
    # keep track of box that needs to be checked
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if not opened[key]:
                opened[key] = True
                stack.append(key)
    return all(opened)

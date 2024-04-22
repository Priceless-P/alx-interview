#!/usr/bin/python3

"""Lockboxes"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    opened_boxes = set()

    # first box is already open
    opened_boxes.add(0)

    # keep track of box that needs to be checked
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)
    return len(opened_boxes) == len(boxes)

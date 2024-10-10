#!/usr/bin/python3
"""N number of locked boxes"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    openedBoxes = set()
    # for dfs
    stack = [0]

    while stack:
        # the current box to explore
        currentBox = stack.pop()

        if currentBox not in openedBoxes:
            openedBoxes.add(currentBox)
            # get the keys from the current box
            keys = boxes[currentBox]
            # add all keys to the stack to explore their corresponding boxes
            for key in keys:
                if key < len(boxes) and key not in openedBoxes:
                    stack.append(key)

    return len(openedBoxes) == len(boxes)

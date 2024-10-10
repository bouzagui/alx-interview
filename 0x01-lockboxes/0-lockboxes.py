#!/usr/bin/python3
""" model """


def canUnlockAll(boxes):
    """ lock boxes """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)

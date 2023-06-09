#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if (length == 0):
        sam = (length, None)
    else:
        sam = (length, sentence[0])

    return (sam)

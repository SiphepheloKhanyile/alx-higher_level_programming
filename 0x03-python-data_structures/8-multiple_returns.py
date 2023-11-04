#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None, )
    else:
        return_t = (len(sentence), sentence[0])
        return return_t

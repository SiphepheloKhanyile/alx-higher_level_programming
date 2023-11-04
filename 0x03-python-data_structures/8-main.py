#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

s2 = ""
ln2,first1 = multiple_returns(s2)
print("Length: {:} - First character: {}".format(ln2, first1))

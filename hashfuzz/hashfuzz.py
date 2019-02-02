import hashlib
import math 
import re

def mean(l):
    n = float(len(l))
    return sum(l) / n

def hash(s1, s2, skip_len=True):
    a = ''
    x = fuzzstr(s1, s2)
    if skip_len is False:
        if len(s1) > len(s2):
            a = s1[len(s2):]
        elif len(s2) > len(s1):
            a = s2[len(s1):]

    s = hashlib.sha256()
    s.update(x+a)
    return s.hexdigest()

def _ratio(s1, s2):
    sameness = fuzzstr(s1, s2)
    ratio = (len(sameness)*2) / float(len(s1) + len(s2))
    f = (math.floor(ratio*10000)/10000) * 100
    if f == 100.0:
        if s1 != s2:
            f = 99.99
    return f

def ratio(s1, s2):
    if len(s1) > len(s2):
        x1 = s2
        x2 = s1
    else:
        x1 = s1
        x2 = s2
    diff = len(x2) - len(x1)
    marks = []
    if diff > 2:
        for i in range(0, diff):
            a = _ratio(x1, x2[i:])
            marks.append(a)
    else:
        marks.append(_ratio(x1, x2))
    return round(mean(marks), 4)

def fuzzstr(s1, s2):
    same = ''
    i = 0
    while i < len(s1) and i < len(s2):
        x1 = s1[i]
        x2 = s2[i]
        if x1 == x2:
            same += x1
        else:
            found = False
            if i+1 < len(s2):
                x1 = s1[i]
                x2 = s2[i+1]
                if x1 == x2:
                    same += x1
                    #i += 1
                    found = True
            if not found and i+1 < len(s1):
                x1 = s1[i+1]
                x2 = s2[i]
                if x1 == x2:
                    same += x1
                    #i += 1
                    found = True
            if not found and i > 0:
                x1 = s1[i-1]
                x2 = s2[i]
                if x1 == x2:
                    same += x1
                    #i += 1
                    found = True
            if not found and i > 0:
                x1 = s1[i]
                x2 = s2[i-1]
                if x1 == x2:
                    same += x1
                    #i += 1
                    found = True
            if not found and i > 0 and i+1 < len(s2):
                x1 = s1[i-1]
                x2 = s2[i+1]
                if x1 == x2:
                    same += x1
                    #i += 1
                    found = True
            if not found and i > 0 and i+1 < len(s1):
                x1 = s1[i+1]
                x2 = s2[i-1]
                if x1 == x2:
                    same += x1
                    #i += 1
                    found = True
        i += 1
    return same




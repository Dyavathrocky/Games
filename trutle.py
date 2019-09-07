# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:49:31 2019

@author: dyrakesh
"""

import turtle


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(10)
    if abs(pos()) < 1:
        break
end_fill()
done()

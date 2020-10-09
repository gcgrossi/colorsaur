# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:52:33 2020

@author: giulio cornelio grossi
"""

import math

###############################################################################
class Gradient_2c:
  def __init__(self, c1_hex, c2_hex):
    
    # init hex colors
    self.c1_hex = c1_hex
    self.c2_hex = c2_hex
    
    # convert hex -> rgb
    h=c1_hex.lstrip('#')
    self.c1_rgb=tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    h=c2_hex.lstrip('#')
    self.c2_rgb=tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    # create the director vector in rgb space
    self.cd_rgb=tuple(map(lambda i, j: i - j, self.c1_rgb, self.c2_rgb))
  

  def pick_color(self, idx):
    
    # use the director vector to pick a particular color in the gradient
    pc=tuple(map(lambda i, j: round((i + idx*j)/255,2), self.c1_rgb, self.cd_rgb))
    self.picked_color=tuple(map(lambda x: x if x<1 else 1, pc))
    self.picked_color=tuple(map(lambda x: x if x>0 else 0, self.picked_color))

    return self.picked_color
  
  
  def get_gradient(self, depht):
    
    grad=[]

    for i in range(0,depht):
      grad.append(self.pick_color(-i/depht))
    
    return grad




###############################################################################
class Gradient_3c:
  def __init__(self, c1_hex, c2_hex, c3_hex):
    
    # init hex colors
    self.c1_hex = c1_hex
    self.c2_hex = c2_hex
    self.c3_hex = c3_hex
    
    # convert hex -> rgb
    h=c1_hex.lstrip('#')
    self.c1_rgb=tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    h=c2_hex.lstrip('#')
    self.c2_rgb=tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    h=c3_hex.lstrip('#')
    self.c3_rgb=tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    # create the director vectors in rgb space
    self.cd1_rgb=tuple(map(lambda i, j: i - j, self.c1_rgb, self.c2_rgb))
    self.cd2_rgb=tuple(map(lambda i, j: i - j, self.c2_rgb, self.c3_rgb))

  def pick_color(self, idx):
    
    pc = []
    index = math.trunc(idx)
    idx = idx-index

    # use the director vector to pick a particular color in the gradient
    pc.append(tuple(map(lambda i, j: round((i + idx*j)/255,2),   self.c1_rgb, self.cd1_rgb)))
    pc.append(tuple(map(lambda i, j: round((i + idx*j)/255,2),   self.c2_rgb, self.cd2_rgb)))
    
    self.picked_color = pc[abs(index)]

    return self.picked_color
  
  
  def get_gradient(self, depht):
    
    grad=[]

    for i in range(0,2*depht):
      grad.append(self.pick_color(-i/depht))
    
    return grad[::2]




#############################################################################
class Gradient_Nc:
  def __init__(self, c_hex):
    
    self.c_hex  = []
    self.c_rgb  = []
    self.cd_rgb = []
    
    for c in c_hex: 
      
      # init hex colors
      self.c_hex.append(c)

      # convert hex -> rgb colors
      h   = c.lstrip('#')
      rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
      self.c_rgb.append(rgb)

    # create the director vectors in rgb space
    for c in range(1,len(c_hex)): 
      rgb=tuple(map(lambda i, j: i - j, self.c_rgb[c-1], self.c_rgb[c]))
      self.cd_rgb.append(rgb)


  def pick_color(self, idx):
    
    pc = []
    index = math.trunc(idx)
    idx = idx-index

    for c in range(0,len(self.cd_rgb)):
      # use the director vector to pick a particular color in the gradient
      pc.append(tuple(map(lambda i, j: round((i + idx*j)/255,2), self.c_rgb[c], self.cd_rgb[c])))
    
    self.picked_color = pc[abs(index)]

    return self.picked_color
  

  def get_gradient(self, depht):
    
    grad=[]
    len_depht = len(self.cd_rgb)

    for i in range(0,len_depht*depht):
      grad.append(self.pick_color(-i/depht))
    
    return grad[::len_depht]


# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:20:54 2020

@author: Charya
"""
nums1 = [11,22,33]
nums2 = [44,55,66]
nums3 = [77,88,99]
print("original list: ")
print(nums1)
print(nums2)
print(nums3)
result = map(lambda x, y, z: x + y +z,nums1,nums2,nums3)
print("\n New list after adding above three lists:")
print(list(result))
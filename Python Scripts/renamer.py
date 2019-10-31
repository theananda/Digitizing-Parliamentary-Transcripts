#!/usr/bin/env python
# coding: utf-8

import os
from glob import glob
import pathlib
import collections
import re

#Path to pdf or text files
abs_path = '' #Update path here
path = pathlib.Path(abs_path)

file_extension = '.pdf' #Update extension here pdf, txt or whatever
first = '02' #update the term here 0 or 1

mid_pattern = re.compile(r'-\d\d?-')
last_pattern = re.compile(r'-\d\d?$')
for p in path.rglob(f'*{file_extension}'):
    if re.search('[a-zA-Z()]', p.stem) == None:
        old_name = str(p.stem)
        mid = mid_pattern.search(old_name).group(0).strip('-')
        if len(mid) == 1:
            mid = '0'+mid
        else:
            pass
        last = last_pattern.search(old_name).group(0).strip('-')
        if len(last) == 1:
            last = '0'+last
        else:
            pass
        new_name = first+'-'+mid+'-'+last+file_extension
        new_path = p.parent / new_name
        p.rename(new_path)
    else:
        print(f'Edit {p.name}')




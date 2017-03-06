#!/usr/bin/env python
# encoding: utf-8

import os

fold_list = ["第八章","第二章","第九章","第六章","第七章","第三章","第十二章","第十六章","第十三章","第十四章","第十五章","第十一章","第十章","第四章","第五章","第一章"]
new_name_list = ["8","2","9","6","7","3","12","16","13","14","15","11","10","4","5","1"]


for i in range(0, len(fold_list)):
    os.system("mv %s test_%s" % (new_name_list[i], new_name_list[i]))
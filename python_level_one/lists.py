# list1 = ['a','b','c','d','e']
# list2 = ['x','y','z']
# # extend method
# list1.extend(list2)
# print(list1)
#
# #removing elements
# # .pop()
# # .remove()
#
# #REVERSING ELEMENTS INSIDE THE LIST
# # reverse()
#
# #sorting method
# # .sort()
#
# #LIST COMPREHENSION
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# first_col = [row[0] for row in matrix]
# print(first_col)
# # result: [1,4,7]

from my_main_package import some_main_script as main
from my_main_package.sub_package import sub_report as sub

main.report_main()
sub.sub_report()

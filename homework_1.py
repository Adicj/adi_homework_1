my_list = [7,8,9,2,3,1,4,10,5,6]
print("My list is: ", my_list)

my_list.sort()
print("My ascending list is:: ", my_list)

my_list.sort(reverse=True)
print("My descending list is: ", my_list)

my_sorted_list = sorted(my_list)

my_sliced_list_even = my_sorted_list[1::2]
print("My even list is: ", my_sliced_list_even)

my_sliced_list_odd = my_sorted_list[0::2]
print("My odd list is: ", my_sliced_list_odd)

my_sliced_list_multiples = my_sorted_list[2::3]
print("My list with multiple of the number 3 is: ", my_sliced_list_multiples)








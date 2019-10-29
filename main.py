def min_max_difference(num_list):
    num_list.sort()
    int small = num_list[0]
    int large = num_list[len(num_list)-1]
    return large - small
    
   
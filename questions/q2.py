def find_the_smallest_missing_element(a: list, start: int=None, end: int=None) -> int:
  if start == None or end == None:
    start = 0
    end = len(a)
  
  mid = int((end + start) / 2)

  if end - start == 1:
    return mid if a[mid] != mid else mid + 1
  if a[mid] == mid:
    start = mid
  else:
    end = mid
  return find_the_smallest_missing_element(a, start, end)


#B = [0, 1, 2, 6, 9, 11, 15] # test case correct
#A =[1, 2, 3, 4, 6, 9, 11, 15] # test case correct
C = [0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20] # test case correct
#arr = [int(k) for k in input().split()]
print(find_the_smallest_missing_element(C))
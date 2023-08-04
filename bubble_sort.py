def bubble_sort(arr:list) -> str:
  counter=0
  loop=0

  for i in arr:
    sorted=True
    for j in range(len(arr)-1, 0, -1):
      if (arr[j]<arr[j-1]):
        arr[j], arr[j-1]=arr[j-1], arr[j]
        counter+=1
        sorted=False
    loop+=1
    if (sorted):
      return f"The list was sorted in {loop} loop(s) and {counter} swap(s), and the length of the list was {len(arr)}"

nums= [i for i in range(9,-1,-1)]
nums2=[2,9,3,1,6,5,7,8,0,4]
print(nums,nums2)
print(bubble_sort(nums))
print(bubble_sort(nums2))
print(nums, nums2)

#after the little experiment it looks like the number of loops needed to sort a list depends on 
#where the smallest and biggest number are placed
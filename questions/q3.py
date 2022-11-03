def find_the_ceiling_and_floor_of_a_number(a: list, k: int) -> dict:
  mid = int(len(a) / 2)
  
  if a[mid] == k:
    return {"ceiling": a[mid], "floor": a[mid]}
  elif len(a) == 1:
    if a[0] < k:
      return {"ceiling": -1, "floor": a[0]}
    else:
      return {"ceiling": a[0], "floor": -1}
  elif a[mid] < k and len(a) > mid + 1:
    if a[mid + 1] > k:
      return {"ceiling": a[mid + 1], "floor": a[mid]}
  elif a[mid - 1] < k and a[mid] > k:
    return {"ceiling": a[mid], "floor": a[mid - 1]}
  a = a[:mid] if a[mid] > k else a[mid:]
  return find_the_ceiling_and_floor_of_a_number(a, k)


a = [1, 4, 6, 8, 9]
for i in range(11):
  response = find_the_ceiling_and_floor_of_a_number(a, i)
  print(f"k = {i} --> teto = {response['ceiling']}, piso = {response['floor']}")
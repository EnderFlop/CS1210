def q1(num, denom):
  final_string = f"{num}/{denom} = "
  final_list = []
  if num == denom:
    final_string += "1"
    final_list.append(1)
    final_string += f"\n{final_list}"
    return final_string
  denom_2 = 2
  while num != 0:
    #print(f"num={num}, denom={denom}, denom_2={denom_2}")
    if num*denom_2 < denom:
      denom_2 += 1
    else:
      final_string += f"1/{denom_2} "
      final_list.append(denom_2)
      num = denom_2 * num - denom
      denom = denom * denom_2
  final_string += f"\n{final_list}"
  return final_string

print(q1(761,1000))
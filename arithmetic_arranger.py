def arithmetic_arranger(problems,answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  a_list = []
  a_len = []
  b_list = []
  b_len = []
  operator_list = []

  for p in problems:
    a,operator,b = p.split()
    
    try:
      a_int,b_int = int(a),int(b)
      if (a_int <= 9999) & (b_int <= 9999):
        a_list.append(a_int)
        b_list.append(b_int)
        a_len.append(len(a))
        b_len.append(len(b))
      else:
        return "Error: Numbers cannot be more than four digits."
    except:
      return "Error: Numbers must only contain digits."

    condition = (operator == "+") | (operator == "-")
    if not condition:
      return "Error: Operator must be '+' or '-'." 
    
    operator_list.append(operator)

    result_list = []
    for i in range(len(a_list)):
      if operator_list[i]=="+":
        result = a_list[i] + b_list[i]
      else:
        result = a_list[i] - b_list[i]  
      result_list.append(result)

  prob_len = []  
  for i in range(len(a_list)):
    prob_len.append(max(a_len[i],b_len[i])+2)
  
  l1=""
  l2=""
  l3=""
  l4=""

  for i in range(len(a_list)):
    l1 = l1+"{:>{}d}".format(a_list[i],prob_len[i])+"    "
    l2 = l2+operator_list[i]+"{:>{}d}".format(b_list[i],prob_len[i]-1)+"    "
    l3 = l3+("-"*prob_len[i])+"    "
    l4 = l4+"{:>{}d}".format(result_list[i],prob_len[i])+"    "

  l1 = l1[:-4]
  l2 = l2[:-4]
  l3 = l3[:-4]
  l4 = l4[:-4]

  if answers == False:
    arranged_problems = l1+"\n"+l2+"\n"+l3
  else:
    arranged_problems = l1+"\n"+l2+"\n"+l3+"\n"+l4


  return arranged_problems
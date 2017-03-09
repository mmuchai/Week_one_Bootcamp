def data_type(operator):
  if type (operator) == str:
    return len(operator)
  elif type(operator) == type(None):
    return 'no value'
  elif type(operator) == bool:
    return operator
  elif type(operator) == int:
    if operator < 100:
      return ('less than 100')
    elif operator > 100:
      return ('more than 100')
    elif operator == 100:
      return ('equal to 100')
  elif type(operator) == list:
    if len(operator) >= 3:
      third_item = operator [2]
      return third_item
    else:
      return None
      
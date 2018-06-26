# alogirthm to urlify a string


def urlify(string, length):
  string_list = list(string)
  total_str_len = len(string)
  
  for i in reversed(range(length)):
    if string_list[i] == ' ':
      string_list[total_str_len-3 : total_str_len] = '%20'
      total_str_len -= 3
    else:
      string_list[total_str_len-1] = string_list[i]
      total_str_len -= 1
      
  return ''.join(string_list)
  
  
if __name__ == '__main__':
  print urlify('data about the nothing      ', 22)

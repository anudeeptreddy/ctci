# Algorithm to determine if a string has all unique characters

def is_unique_ch_string(string):
  characters = {}
  for ch in string:
    if ch in characters.keys():
      return False
    characters[ch] = True
  return True


if __name__ == '__main__':
  string = 'abcde'
  print 'NO DUPLICATES' if is_unique_ch_string(string) else 'DUPLICATES'

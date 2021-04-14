import requests
import sys , os

try:
  filename = sys.argv[1]
  with open(filename, 'r') as file:
    search = file.readlines()
    for url in search:
        try:
          response = requests.get(url)
          text1 = "Automated Promotion Platform for Your Business"
          data = response.text
          if data.find(text1)>0:
              print('Found :' + ' >> ' + url)
              save = open("success.txt", "a")
              save.write(url)
              save.close()
        except:
          pass
except:
  print('Example: ./'+ sys.argv[0] + ' input.txt')
  pass


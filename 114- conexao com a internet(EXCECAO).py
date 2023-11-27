import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")

except urllib.error.URLError:
    print("O site pudim não esta acessivel")

else:
    print('conseguir acessar o site pudim')
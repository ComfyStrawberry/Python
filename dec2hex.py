PK
     ��cQ�m�       main.pydef dec2hex(dec):
  hexValue = hex(dec)
  hexS = str(hex(dec))
  h = hexS.replace('0x' , '')
  return h 
def main():
  print("DECIMAL TO HEXADECIMAL CONVERSION")
  hexString = dec2hex(10)
  print(10,hexString)
  hexString = dec2hex(245)
  print(245,hexString)
  
main()PK 
     ��cQ�m�                     main.pyPK      5   2    
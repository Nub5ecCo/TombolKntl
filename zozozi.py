import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Tombol Tambahan Termux ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  By:   KANG RECODE')
print('\t Wa : Nothing')
print('\t Facebook :-)
print('\t Github : https://github.com/Nub5ecCo')
print(a+'+'*40)
print('\nBentar....')
sleep(1)
print(b+'\n[!] Ngambil file Bawaan Bambank :v')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Sukses !')
sleep(1)
print(b+'\n[!] Nambahin Tombol Bentar')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Lagi proses  !')
sleep(1)
print(b+'\n[!] Sabar zeyeng :v')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Dah selesai Boejank !! ^^'+c+'\n\nhubungi : saya lewat Whatsapp atau  Facebook*\n\n')
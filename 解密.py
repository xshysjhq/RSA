import datetime

import tkinter as tk
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

file_in = open(r"C:\Users\18805\Desktop\申请注册.txt", "rb")
cipher_data = file_in.read()
file_in.close()
#字节转换为字符串
cipher_data = cipher_data.decode('ANSI')
#data每位字符减去5
cipher_text= ''.join(chr(ord(x)-5) for x in cipher_data)

d, n = (3606353, 7500523)
plain_text =''
cipher_text_list = cipher_text.split(',')
for namelist in cipher_text_list:
    cipher_text_i = int(namelist)
    m = chr(pow(cipher_text_i, d, n))
    plain_text += m
print(plain_text)
decrpyt_data_list = plain_text.split('/')
now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
address = decrpyt_data_list[1]


def encrypt_file(time, address):
    salt = "社会治安生态感知系统writeby谢爽解密"
    data = salt+'/'+time +'/'+ address
    e, n = (65537, 7500523)
    list = []
    for char in data:
        m = ord(char)
        cipher_text = pow(m, e, n)
        list.append(cipher_text)
    cipher = ",".join('%s' % i for i in list)
    # data每位字符加上5
    cipher_data = ''.join(chr(ord(x) + 5) for x in cipher)
    return cipher_data
with open(r"C:\Users\18805\Desktop\注册证书.txt", 'w') as f:
    encrpty_data = encrypt_file(now_time, address)
    f.seek(0)
    f.truncate()
    f.write(encrpty_data)
    f.close()


# window = tk.Tk()
# window.title("RSA加密解密")
# window.geometry("600x450+700+300")
# # 创建输入框和标签
# p_label = tk.Label(window, text="选择文件夹")
# p_label.grid(row=0, column=0)
# p_entry = tk.Entry(window)
# p_entry.grid(row=0, column=1)
#
# generate_btn=tk.Button(window, text="生成",command=generate)
#
#
# plain_text_label = tk.Label(window, text="明文:")
# plain_text_label.grid(row=2, column=0)
# plain_text_entry = tk.Entry(window)
# plain_text_entry.grid(row=2, column=1)
#
# cipher_text_label = tk.Label(window, text="密文:")
# cipher_text_label.grid(row=3, column=0)
# cipher_text_entry = tk.Entry(window)
# cipher_text_entry.grid(row=3, column=1)
#
# text_label = tk.Label(window, text="RSA加密或解密结果:")
# text_label.grid(row=10, column=1)
# text = tk.Text(window, height=10, width=30, wrap="word", state="disabled")
# text.grid(row=11, column=1)
# text.configure(state="normal")
# # 创建按钮
# generate_prime_btn=tk.Button(window, text="生成",command=generate_prime_btn_clicked)
# encrypt_btn = tk.Button(window, text="加密",command=encrypt_btn_clicked)
# decrypt_btn = tk.Button(window, text="解密",command=decrypt_btn_clicked)
# generate_prime_btn.grid(row=0, column=2)
# encrypt_btn.grid(row=5, column=0)
# decrypt_btn.grid(row=5, column=2)
#
# window.mainloop()

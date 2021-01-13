# import tkinter as tk 

# window = tk.Tk()

# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# entry.pack()

# window.mainloop()
import requests
from requests.auth import HTTPDigestAuth

url = "http://shopjozi.ir/api/user/noti" 
req = requests.get(url ,auth=HTTPDigestAuth('admin', '09356662413') )
print(req)

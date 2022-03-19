import qrcode
from tkinter import *



window = Tk()

GENpic = PhotoImage(file='QRplaceholder.PNG')


# gets the entries into variables
def click():
    content = entry.get()
    cont_path = entry_path.get()
    content_name = entry_name.get()

# generates the QRcode
    qrcode.make(content).save(cont_path + '\\' + content_name + '.png')

    Labl_upinfo['text'] = 'Created & Saved'
    Labl_upinfo['text'] = 'Make Another?'

# shows QRcode in the window
    GENpic['file'] = cont_path + '\\' + content_name + '.png'

    

    

window.title("QRcode Generator")
window.geometry('720x580')


icon = PhotoImage(file='instaded.png')
window.iconphoto(True,icon)

labl = Label(window,
text="Blade's QRcode Generator",
font=('Verdana Sans', 20),
bg='black',
fg='white',
padx=600

)

labl_instruct_path = Label(window,
text='QRcode Save Directory:',
bg='#036ffc',
fg='white',
font=('Verdana Sans', 15),

)

entry_path = Entry(window,
font=('Verdana Sans', 15),
bg='#3e90fa'
)



labl_instruct = Label(window,
text='QRcode Content:',
font=('Verdana Sans', 15),
bg='#036ffc',
fg='white',

)

entry = Entry(window,
font=('Verdana Sans', 15),
bg='#3e90fa'
)

labl_name = Label(window,
text='QRcode File Name:',
font=('Verdana Sans', 15),
bg='#036ffc',
fg='white',

)

entry_name = Entry(window,
font=('Verdana Sans', 15),
bg='#3e90fa'
)



create_button = Button(window,
font=('Verdana Sans', 15),
text='Create',
fg='black',
command=click,

)

Labl_upinfo = Label(window,
text='▼ Click Button to Create QRcode ▼',
font=('Verdana Sans', 15),
bg='#036ffc',
fg='white',

)

Labl_img = Label(window,
image=GENpic
)

labl.pack(side=TOP)

labl_instruct_path.pack()
entry_path.pack()

labl_instruct.pack()
entry.pack()

labl_name.pack()
entry_name.pack()

Labl_upinfo.pack()

Labl_img.pack()

create_button.pack()

window.configure(background='#036ffc')

window.mainloop()
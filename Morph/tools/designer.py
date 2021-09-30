from pypresence import Presence
import tkinter as tk
from tkinter import ttk
from threading import Thread

client_id = '889606355873321011'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop


class GUI:
    
    def __init__(self,server):
        self.a = "a"
        self._d_pr()
        self.server = server
        self.window = tk.Tk()
        self.center_screen(self.window)
        style = ttk.Style(self.window)
        self.window.tk.call('source', 'Morph/styles/azure dark.tcl')
        style.theme_use('azure')
        
    def center_screen(self, root):
        window_height = 530
        window_width = 800
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    
    def _d_pr(self):
        print('Started Discord rich-presence! 🐸')
        RPC.update(details="Working on Morph Project: [/Source]", state="<Morph.tools.forge.character object at 0x7f9d1b8d5e20>", large_image='morph', small_image='wr')
    
    def _gui(self):
        # Window stuff
        root = self.window
        # First frame
        frame = ttk.LabelFrame(root, text='Overview', width=200, height=200)
        frame.place(x=20, y=12)
        # Label for load
        load_txt = tk.Label(frame, text = "Load: "+str(self.server.users)).place(x=2,y=2)
        # Progress bar for load
        progress = ttk.Progressbar(frame, value=self.server.users, mode='determinate')
        progress.place(x=10, y=20)
        # Frame for requirements/rules, called rules in GUI cause shorter
        frame_r = ttk.LabelFrame(root, text='Rules:', width=200, height=200)
        frame_r.place(x=230, y=12)
        # Labels for rules
        user_rule_txt = tk.Label(frame_r, text = "Users: "+str(self.server._requirements['user_type'])).place(x=2,y=2)
        connect_rule_txt = tk.Label(frame_r, text = "Connection: "+str(self.server._requirements['connect_type'])).place(x=2,y=20)
        access_rule_txt = tk.Label(frame_r, text = "Access: "+str(self.server._requirements['access_type'])).place(x=2,y=38)
        # Frame for treeview
        treeframe = ttk.LabelFrame(root, text='Users:', width=200, height=200)
        treeframe.place(x=20, y=212)
        # Treeview for users
        treeScroll = ttk.Scrollbar(treeframe)
        treeScroll.pack(side='right', fill='y')


        treeview = ttk.Treeview(treeframe, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
        treeview.pack()
        treeScroll.config(command=treeview.yview)

        treeview.column("#0", width=120)
        treeview.column(1, anchor='w', width=100)
        treeview.column(2, anchor='w', width=100)

        treeview.heading("#0", text="User", anchor='center')
        treeview.heading(1, text="ID", anchor='center')
        treeview.heading(2, text="IP", anchor='center')

        self.window.mainloop()
    
    def _kill(self):
        self.window.destroy()

    def open_gui(self):
        self._gui()
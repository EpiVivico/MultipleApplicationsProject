import tkinter as tk
from tkinter import ttk


class MyInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.frame = tk.Frame(self.master, width=400, height=300, relief='raised')
        self.frame.pack()
        self.master = master  # root
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # -------      Set Window Title                 -------
        self.winfo_toplevel().title("Graphical User Interface")

        self.setWindow()
        self.createInputButton()
        # self.createAnagramButton()

        # -----             Making Display Zone         -------

        # self.displayAnagrams("", 0)
        '''self.textZone = tk.StringVar(value="O\t\t\t\tO")
        self.frame = ttk.Frame(self.master) # root
        self.textZoneEntry = ttk.Entry(self.frame, textvariable=self.textZone, state="readonly")
        self.textZoneScrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.textZoneEntry.xview)
        self.textZoneEntry.config(xscrollcommand=self.textZoneScrollbar.set)

        self.canvas.create_window(window=self.frame)
        '''
        # self.createQuitButton()

    def displayAnagrams(self, anagrams, initCode):
        # ------           Show Text Zone             -------
        self.textZone = tk.StringVar(value=anagrams)
        frame = ttk.Frame(self.master)  # root
        textZoneEntry = ttk.Entry(frame, textvariable=self.textZone, state="readonly")
        textZoneScrollbar = ttk.Scrollbar(frame, orient="vertical", command=textZoneEntry.xview)
        textZoneEntry.config(xscrollcommand=textZoneScrollbar.set)
        # textZoneEntry.grid(row=1, )

        if initCode == 0:
            # frame.pack()
            self.canvas.create_window(200, 190, window=frame)
            # textZoneEntry.grid(row=1, sticky='ew')
            # textZoneScrollbar.grid(row=2, sticky='ew')

    '''def setWindow(self):
        # -------           Set Canva and Window        -------
        self.canvas = tk.Canvas(self.master, width=400, height=300, relief='raised')
        self.canvas.pack()
        label = tk.Label(self.master, font=('helvetica', 15, 'bold'), text="Enter a word to be checked:")
        self.canvas.create_window(200, 100, window=label)'''

    def setWindow(self):
        # -------           Set Frame and Window        -------
        label = tk.Label(self.frame, font=('helvetica', 15, 'bold'), text="Enter a word to be checked:")
        label.place(relx=0.5, rely=0.13, anchor='center')
        # label.pack()

    def createInputButton(self):
        # -------          User Input Button            -------
        self.entry = tk.Entry(self.frame)
        self.entry.place(relx=0.5, rely=0.2, anchor='center')
        # self.entry.pack()

        # Create the application variable.
        self.contents = tk.StringVar()

        # Set it to some value.
        self.contents.set("")

        # Tell the entry widget to watch this variable.
        self.entry["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        self.entry.bind('<Key-Return>', self.print_contents)

    def createAnagramButton(self):
        # -------           Primary Button              -------
        self.anagramButton = tk.Button(text="Search for anagrams", fg="white", bg="dark green",
                                       font=('helvetica', 10, 'bold'), command=self.checkAnagramCallback)  # raw init
        self.canvas.create_window(200, 170, window=self.anagramButton)

    def createQuitButton(self):
        # -------             Quit Button                -------
        self.quit = tk.Button(text="QUIT", fg="black", bg="red", font=('helvetica', 10, 'bold'),
                              command=self.master.destroy)
        self.canvas.create_window(375, 285, window=self.quit)

    def checkAnagramCallback(self):
        # call anagram checker (back end)
        print("Checking for anagrams: " + self.contents.get())
        # self.displayAnagrams(self.contents.get()) self.displayAnagrams("OK this is the test to get anagrams as a
        # very long long long string in order to test the scrollbar and the textzone...", 1)
        self.contents.set("")

    def print_contents(self, event):
        # event gives you the pressed key and mouse positioning
        print("Hi, You typed:", self.contents.get())
        self.contents.set("")


if __name__ == "__main__":
    root = tk.Tk()
    myapp = MyInterface(root)
    myapp.mainloop()

import anagramFinder as af
import tkinter as tk
import tkinter.scrolledtext
from tkinter import ttk


class MyInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.Afinder = af.AnagramFinder()

        # -------       Desktop Application SetUP       -------
        self.frame = tk.Frame(self.master, width=400, height=100, relief='raised')
        self.frame.pack(fill=None, expand=False)
        self.master = master  # root
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # -------      Set Window Title                 -------
        self.winfo_toplevel().title("Graphical User Interface")

        self.setWindow()
        self.createInputButton()
        self.createAnagramButton()
        self.createTextZone()

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

    def createTextZone(self):
        # ------           Show Text Zone             -------
        '''self.textZone = tk.Text(self.frame, height=5, width=40)
        self.scrollBar = tk.Scrollbar(self.frame, command=self.textZone.yview())
        self.textZone["yscrollcommand"] = self.scrollBar.set'''
        self.textConsole = tkinter.scrolledtext.ScrolledText(self, width=40, height=10, font=('helvetica', 12))
        self.textConsole.pack(expand=True, fill='both', pady=10)
        self.textConsole.configure(state=tk.DISABLED)

    def setWindow(self):
        # -------           Set Frame and Window        -------
        label = tk.Label(self.frame, font=('helvetica', 15, 'bold'), text="Enter a word to be checked:")
        label.place(relx=0.5, rely=0.13, anchor='center')

    def createInputButton(self):
        # -------          User Input Button            -------
        self.entry = tk.Entry(self.frame)
        self.entry.place(relx=0.5, rely=0.4, anchor='center')

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
        self.anagramButton = tk.Button(self.frame, text="Search for anagrams", fg="white", bg="dark green",
                                       font=('helvetica', 10, 'bold'), command=self.checkAnagramCallback)  # raw init
        self.anagramButton.place(relx=0.5, rely=0.7, anchor='center')

    def createQuitButton(self):
        # -------             Quit Button                -------
        self.quit = tk.Button(text="QUIT", fg="black", bg="red", font=('helvetica', 10, 'bold'),
                              command=self.master.destroy)
        self.canvas.create_window(375, 285, window=self.quit)

    def checkAnagramCallback(self):
        # call anagram checker (back end)
        print("Checking for anagrams of: " + self.contents.get())
        self.Afinder.searchAnagram(self.contents.get())
        listOfAnagrams = self.Afinder.finalResults

        toWrite = ""
        for word in listOfAnagrams:
            toWrite += word + '\n'

        self.writeInTextZone(toWrite)
        self.contents.set("")

    def writeInTextZone(self, toWrite):
        self.textConsole.configure(state=tk.NORMAL)
        self.textConsole.insert('0.0', toWrite)
        self.textConsole.configure(state=tk.DISABLED)

    def print_contents(self, event):
        # event gives you the pressed key and mouse positioning
        print("Hi, You typed:", self.contents.get())
        self.contents.set("")


if __name__ == "__main__":
    root = tk.Tk()
    myapp = MyInterface(root)
    myapp.mainloop()

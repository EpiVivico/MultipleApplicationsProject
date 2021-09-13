import anagramFinder as af
import permutations as permute
import tkinter as tk
import tkinter.scrolledtext


class MyInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.Afinder = af.AnagramFinder()

        # -------       Desktop Application SetUP       -------
        self.frame = tk.Frame(self.master, width=400, height=150, relief='raised')
        self.frame.pack(fill=None, expand=False)

        # ------        Init of the None                --------
        self.master = master  # root
        self.anagramButton = None
        self.textConsole = None
        self.entry = None
        self.contents = None
        self.quit = None
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # -------      Set Window Title                 -------
        self.winfo_toplevel().title("Graphical User Interface")

        self.setWindow()
        self.createInputButton()
        self.createAnagramButton()
        self.createPermutationButton()
        self.createTextZone()
        self.createQuitButton()

    def createTextZone(self):
        # ------           Show Text Zone             -------
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
        self.anagramButton.place(relx=0.5, rely=0.6, anchor='center')

    def createPermutationButton(self):
        # -------           Primary Button              -------
        self.anagramButton = tk.Button(self.frame, text="List all permutations", fg="white", bg="brown",
                                       font=('helvetica', 10, 'bold'), command=self.findPermutations)  # raw init
        self.anagramButton.place(relx=0.5, rely=0.8, anchor='center')

    # Crash at 9 letters
    def findPermutations(self):
        self.textConsole.configure(state=tk.NORMAL)

        permutations = []
        permutations = permute.find_permutations(self.contents.get(), 0, permutations)

        strPermutations = ""
        for word in permutations:
            strPermutations += word + '\n'

        self.textConsole.insert('0.0', strPermutations)
        self.textConsole.configure(state=tk.DISABLED)

    def createQuitButton(self):
        # -------             Quit Button                -------
        self.quit = tk.Button(self, text="QUIT", fg="black", bg="red", font=('helvetica', 10, 'bold'),
                              command=self.master.destroy)
        self.quit.pack(side=tk.RIGHT, pady=5)

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
        print(event)
        self.contents.set("")


if __name__ == "__main__":
    root = tk.Tk()
    myapp = MyInterface(root)
    myapp.mainloop()

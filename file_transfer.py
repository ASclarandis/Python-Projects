import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
from datetime import timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        # sets title of GUI window
        self.master.title("File Transfer")
        
        # creates a button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # positions the source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # creats entry for source directory selection
        self.source_dir = Entry(width=75)
        # positions entry in GUI using tkinter grid() padx and pady are the same as
        # the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30,0))
        
        # creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # positions destination button in GUI using tkinter grid() padx and pady are the same as
        # the button to ensure they line up
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        # creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # positions entry in GUI using tkinter grid() padx and pdy are the same as
        # the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        # creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady= (0, 15))

    # creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # the .delete(0,END) will clear the content that is inserted in the entry widget
        # this allows the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        # the .insert method will insert the user selection to the source_dir entry
        self.source_dir.insert(0, selectSourceDir)
            

    # creates function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # the .delete(0, END) will clear the content that is inserted in the entry widget
        # this allows the path to be inserted into the entry widget properly
        self.destination_dir.delete(0, END)
        # the .insert method will insert the user selection to the destination_dir entry widget
        self.destination_dir.insert(0, selectDestDir)


    # creates function to transfer files from one directory to another
    def transferFiles(self):
        # gets source directory
        source = self.source_dir.get()
        # gets destination directory
        destination = self.destination_dir.get()
        # gets a list of files in the source directory
        source_files = os.listdir(source)
        
        
        # setting parameters to only transfer files that were created/modified within 24 hours
        for i in source_files:
            # gets the current time
            current_time = datetime.datetime.now()
            # gets the timestamp of when the file was last modified
            modified_time = os.path.getmtime(source + '/' + i)
            # convertimg modified_time to same data type as current_time in order to get time difference
            mod_time = datetime.datetime.fromtimestamp(modified_time)
            timeDifference = current_time - mod_time
            if timeDifference < timedelta(hours = 24):
                # moves each file from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

    # creates function to exit program
    def exit_program(self):
        # root is the main GUI window, the tkinter destroy method
        # tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

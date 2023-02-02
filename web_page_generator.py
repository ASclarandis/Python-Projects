import tkinter as tk
from tkinter import *
import webbrowser

# creating the GUI frame
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        
        # creates a label to inform user to enter text into entry box
        text_label = Label(text = 'Enter custom text or click the Default HTML page button')
        text_label.grid(row=0,column=0, padx=(25,0), pady=(10,0), sticky=W)
        
        # creates entry for custom text
        self.customText = Entry(width=100)
        self.customText.grid(row=1, column=0, columnspan=2, padx=(0, 10), pady=(0, 10))
        
        # creates a button for the default HTML page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(200, 0), pady=(10, 10))
        
        # creates a button for submitting custom text
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=1, padx=(20, 10), pady= (10, 10))


        
    # this function will create the default HTML document
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # this function will create a custom HTML document
    def customHTML(self):
        # get() will return the input of the entry field into the HTML doc
        customText = self.customText.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

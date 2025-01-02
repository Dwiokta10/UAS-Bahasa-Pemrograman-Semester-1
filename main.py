from tkinter import Tk
from data.data import Data
from view.viewGui import ViewGUI

if __name__ == "__main__":
    root = Tk()
    data = Data()
    app = ViewGUI(root, data)
    root.mainloop()

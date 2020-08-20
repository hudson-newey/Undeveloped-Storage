import tkinter as tk

# init
wordList = []

# CASUAL
# 100ms = 10 words per second
# 50ms = 20 words per second
# 30ms = 33 words per second
# 25ms = 40 words per second
# 20ms = 50 words per second
delay = 100#ms

print("File to Read,")
with open("text/" + input(),'r') as file:     
    for iline in file:
        # reading each word
        for iword in iline.split():
            wordList.append(iword)

class UpdateLabel(tk.Label):
  def __init__(self, *args, **kwargs):
    tk.Label.__init__(self, *args, **kwargs)
    self._count = 0

  def update_text(self):
    self.config(text=str(wordList[self._count]), height=40, width=40, font=("Lato", 60))
    self._count += 1
    self.after(delay, self.update_text)

root = tk.Tk()
label = UpdateLabel(root)
label.pack()
label.update_text()
root.mainloop()

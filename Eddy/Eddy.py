import wpf
from System.Windows import Application, Window
from Microsoft.Win32 import OpenFileDialog
from Text import split, combine
from Chains import Chain, ChainGroup

class Eddy(Window):

    def __init__(self):
        wpf.LoadComponent(self, 'Window.xaml')
        self.speakButton.Click += self.speak
        self.loadButton.Click += self.load
        self.chain = ChainGroup()

    def load(self, *args):
        dialog = OpenFileDialog()
        dialog.Filter = "Text|*.txt"
        if dialog.ShowDialog():
            with open(dialog.FileName, encoding="utf-8") as data:
                words = split(data.read())
                self.chain.append(Chain(words))

    def speak(self, *args):
        words, word = [], "."
        while len(words) <= 0 or word != ".":
            word = self.chain(word)
            if word == "": break
            words.append(word)
        self.textbox.Text += "Eddy : " + combine(words) + "\n"
        self.textbox.ScrollToEnd()

if __name__ == '__main__':
    Application().Run(Eddy())
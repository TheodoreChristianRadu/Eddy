import wpf
from System.Windows import Application, Window
from System.Windows.Controls import DockPanel
from Microsoft.Win32 import OpenFileDialog
from Text import split, combine
from Chains import Chain, ChainGroup

class Eddy(Window):

    def __init__(self):
        wpf.LoadComponent(self, 'Window.xaml')
        self.chain = ChainGroup()

    def load(self, *args):
        dialog = OpenFileDialog()
        dialog.Filter = "Text|*.txt"
        if dialog.ShowDialog():
            with open(dialog.FileName, encoding="utf-8") as data:
                if self.Slider(dialog.SafeFileName, self.tweak, self.sliders):
                    words = split(data.read())
                    self.chain.append(Chain(words))
    
    class Slider(DockPanel):
        limit = 15
        def __new__(cls, name, tweaked, parent):
            if len(parent.Children) >= cls.limit:
                return None
            return super().__new__(cls)
        def __init__(self, name, tweaked, parent):
            wpf.LoadComponent(self, 'Slider.xaml')
            self.name.Text = name
            self.slider.Value = 5
            self.slider.Tag = len(parent.Children)
            self.slider.ValueChanged += tweaked
            self.value.Text = "1.0"
            parent.Children.Add(self)

    def tweak(self, slider, *args):
        weight = slider.Value / (10.1 - slider.Value)
        slider.Parent.value.Text = "{:.1f}".format(weight)
        self.chain[slider.Tag].weight = weight

    def speak(self, *args):
        words, word = [], "."
        while len(words) <= 0 or word != ".":
            word = self.chain(word)
            if word == "": break
            words.append(word)
        self.textbox.Text += "\n" + "Eddy : " + combine(words) + "\n"
        self.textbox.ScrollToEnd()

if __name__ == '__main__':
    Application().Run(Eddy())
import wpf
from System.Windows import Application, Window
from System.Windows.Controls import DockPanel, Canvas
from Microsoft.Win32 import OpenFileDialog
from System.Windows.Input import Mouse, MouseButton, MouseButtonState, MouseButtonEventArgs
from Text import split, combine
from Chains import Chain, ChainGroup

class Eddy(Window):

    def __init__(self):
        wpf.LoadComponent(self, 'Window.xaml')
        self.knob.Children.Add(self.Knob())
        self.chain = ChainGroup()

    class Knob(Canvas):
        def __init__(self):
            wpf.LoadComponent(self, 'Knob.xaml')
            self.slider.ValueChanged += self.tweaked
        def hover(self, sender, event):
            if (event.LeftButton == MouseButtonState.Pressed and not event.MouseDevice.Captured):
                click = MouseButtonEventArgs(event.MouseDevice, event.Timestamp, MouseButton.Left)
                click.RoutedEvent = Mouse.MouseDownEvent
                sender.RaiseEvent(click)
        def tweaked(self, *args):
            self.gauge.CurrentValue = self.slider.Value

    def load(self, *args):
        dialog = OpenFileDialog()
        dialog.Filter = "Text|*.txt"
        if dialog.ShowDialog():
            with open(dialog.FileName, encoding="utf-8") as data:
                if self.Slider(dialog.SafeFileName, self.sliders, self.tweak):
                    words = split(data.read())
                    self.chain.append(Chain(words))
    
    class Slider(DockPanel):
        limit = 15
        def __new__(cls, name, parent, tweaked):
            if len(parent.Children) >= cls.limit: return None
            return super().__new__(cls)
        def __init__(self, name, parent, tweaked):
            wpf.LoadComponent(self, 'Slider.xaml')
            self.name.Text = name
            self.slider.Value = 5
            self.slider.Tag = len(parent.Children)
            self.slider.ValueChanged += tweaked
            self.value.Text = "  1.0"
            parent.Children.Add(self)

    def tweak(self, slider, *args):
        weight = slider.Value / (10.1 - slider.Value)
        slider.Parent.value.Text = "{:5.1f}".format(weight)
        self.chain[slider.Tag].weight = weight

    def speak(self, *args):
        words, word = [], "."
        energy = self.knob.Children[0].gauge.CurrentValue
        while len(words) <= energy or word != ".":
            word = self.chain(word)
            if word == "": break
            words.append(word)
        self.textbox.Text += "\n" + "Eddy : " + combine(words) + "\n"
        self.textbox.ScrollToEnd()

if __name__ == '__main__':
    Application().Run(Eddy())
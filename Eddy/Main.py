from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlFile, ControlSlider, ControlButton, ControlTextArea
from pyforms import start_app
from Eddy import Eddy

class Program(BaseWidget):

    def __init__(self):
        self.eddy = Eddy()
        super().__init__("Eddy")
        self.file = ControlFile("Influence")
        self.file.changed_event = self.loadFile
        self.length = ControlSlider("Length")
        self.length.max = 1000
        self.button = ControlButton("Speak")
        self.button.value = self.makeSpeech
        self.text = ControlTextArea()
        self.formset = ["", ("", "file", "length", "button", ""), "", ("", "text", ""), ""]

    def loadFile(self):
        try:
            with open(self.file.value, encoding="utf-8") as data:
                self.eddy.influence(data.read())
        except FileNotFoundError:
            pass

    def makeSpeech(self):
        self.text += "Eddy : " + self.eddy.speak(self.length.value) + "\n"

start_app(Program)
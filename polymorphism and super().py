class fifth():
    def showclass(self):
        self.name="hira"
        print(self.name)

class ninth(fifth):
    def showclass(self):
        self.name="khira"
        print(self.name)
        print("after reset")
        super().showclass()


st1=fifth()
st2=ninth()
st2.showclass()


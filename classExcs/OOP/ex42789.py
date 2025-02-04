class RecordingBell:
    def __init__(self):
        self.msg = ""

    def play(self):
        return self.msg

    def record(self, s):
        self.msg += s


o1 = RecordingBell()
print(o1.play())
assert o1.play() == ""

o2 = RecordingBell()
o2.record("one")
print(o2.play())
assert o2.play() == "one"

o1.record("yo")
print(o1.play())
assert o1.play() == "yo"

o2.record("two")
o2.record("three")
print(o2.play())
assert o2.play() == "onetwothree"

print("OK")
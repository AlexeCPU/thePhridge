import json

class Settings:
    def __init__(self, settingsFilePath):
        self.settingsFilePath = settingsFilePath
        try:
            f = open(settingsFilePath, "r")
        except FileNotFoundError:
            f = open(settingsFilePath, "w+")
            f.write("{}")
        f = open(settingsFilePath, "r")
        self.data = json.load(f)

    def setValue(self, key, value):
        self.data[key] = value
        
        # Whenever the value is set it writes the change to the file provided when creating the class
        json_object = json.dumps(self.data, indent = 4)
        with open(self.settingsFilePath, "w") as outfile:
            outfile.write(json_object)

    def getValue(self, key):
        return self.data[key]

    def clear(self):
        with open(self.settingsFilePath, "w") as outfile:
            outfile.write("{}")



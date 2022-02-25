import json

class Settings:
    def init(self, settingsFilePath):
        self.settingsFilePath = settingsFilePath
        f = open(settingsFilePath)
        self.data = json.load(f)

    def setValue(self, key, value):
        self.data[key] = value
        
        # Whenever the value is set it writes the change to the file provided when creating the class
        json_object = json.dumps(self.data, indent = 4)
        with open(self.settingsFilePath, "w") as outfile:
            outfile.write(json_object)

    def getValue(self, key):
        return self.data[key]



"""
read from xml file
convert to json
return json obj
"""

import xml.etree.ElementTree as ET


class JsonAdapter:
    def __init__(self):
        self.original = None
        self.transformed = {}

    def transform(self, filename: str) -> dict:
        data = ET.parse(filename)
        root = data.getroot()
        all_notes = root.findall("note")
        self.transformed = {root.tag: []}
        for note in all_notes:
            to = note.find("to").text
            from_guest = note.find("from").text
            heading = note.find("heading").text
            body = note.find("body").text
            self.transformed[root.tag].append(
                {"to": to, "from": from_guest, "heading": heading, "body": body}
            )
        return self.transformed

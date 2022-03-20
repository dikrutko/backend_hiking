import os
import xml.dom.minidom
import codecs

dict = {}

fileDir = f"trecks"
fileExt = r".gpx"
result = '{'
color = []
colorrgb = []
for treck in os.listdir(fileDir):
    if treck.endswith(fileExt):
        doc = xml.dom.minidom.parse(f"trecks/{treck}")
        trk = doc.getElementsByTagName("trk")[0]
        name = trk.getElementsByTagName("name")[0]
        
        if str(name.childNodes[0].nodeValue) == "Здоровья":
            color.append("Red")
            colorrgb.append("rgb(255,0,0)")
        else:
            extensions = trk.getElementsByTagName("extensions")[0]
            TrackExtension = extensions.getElementsByTagName("gpxx:TrackExtension")[0]
            DisplayColor = TrackExtension.getElementsByTagName("gpxx:DisplayColor")[0]
            color.append(str(DisplayColor.childNodes[0].nodeValue))
            i = str(DisplayColor.childNodes[0].nodeValue)
            if i == "Orange":
                colorrgb.append("rgb(255,165,0)")
            elif i == "DarkCyan":
                colorrgb.append("rgb(0,139,139)")
            elif i == 'Purple':
                colorrgb.append('rgb(128,0,128)')
            elif i == 'DarkMagenta':
                colorrgb.append('rgb(139,0,139)')
            elif i == 'Green':
                colorrgb.append('rgb(0,255,0)')
            elif i == 'DarkGreen':
                colorrgb.append('rgb(0,100,0)')
            elif i == 'DarkBlue':
                colorrgb.append('rgb(2,8,148)')
            elif i == 'Yellow':
                colorrgb.append('rgb(250,253,15)')
            elif i == 'DarkRed':
                colorrgb.append('rgb(139,0,0)')

        trkseg = trk.getElementsByTagName("trkseg")[0]
        result = result + "'" + str(name.childNodes[0].nodeValue) + "'" + ':['
        for child in trkseg.childNodes:
            if child.nodeType == child.ELEMENT_NODE:
                ele = child.getElementsByTagName("ele")[0]
                latValue = round(float(child.getAttribute("lat")),6)
                lonValue = round(float(child.getAttribute("lon")),6)
                eleValue = round(float(ele.childNodes[0].nodeValue),6)
                result += f'{lonValue},{latValue},{eleValue},'
        result = result[:-1] + '],\n'
#print(color, colorrgb)       
file1 = codecs.open("vocab_base.py", "w", "utf-8")
file1.write("vocab = " + result[:-2] + "}")
file1.close()

file2 = open("vocab_color.py", "w")
#file2.write("color = " + str(color) + "\n")
file2.write("colorrgb = " + str(colorrgb))
file2.close()

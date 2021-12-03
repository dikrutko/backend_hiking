import xml.dom.minidom


def pars_coords(name):
    doc = xml.dom.minidom.parse(f"scripts/trecks/{name}.gpx")
    trk = doc.getElementsByTagName("trk")[0]
    trkseg = trk.getElementsByTagName("trkseg")[0]
    result = ''
    for child in trkseg.childNodes:
        if child.nodeType == child.ELEMENT_NODE:
            latValue = round(float(child.getAttribute("lat")),6)
            lonValue = round(float(child.getAttribute("lon")),6)

            result += f'geoPoints.add(new GeoPoint({latValue}), ({lonValue}));<br>'
    return result

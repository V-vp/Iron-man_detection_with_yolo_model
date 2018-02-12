import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET

def write_xml(folder,img,objects,tl,br,savedir):
    if not  os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img.path)
    height,width,depth = image.shape

    annotaion = ET.Element('annotation')
    ET.SubElement(annotaion,'folder').text = folder
    ET.SubElement(annotaion,'filename').text = img.name
    ET.SubElement(annotaion,'segmented').text = '0'
    size = ET.SubElement(annotaion,'size')
    ET.SubElement(size,'width').text = str(width)
    ET.SubElement(size,'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    for obj,topl,botr in zip(objects,tl,br):
        ob = ET.SubElement(annotaion,'object')
        ET.SubElement(ob,'name').text = obj
        ET.SubElement(ob,'pose').text = 'Unsecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob,'bndbox')
        ET.SubElement(bbox,'xmin').text = str(topl[0])
        ET.SubElement(bbox,'ymin').text = str(topl[1])
        ET.SubElement(bbox,'xmax').text = str(botr[0])
        ET.SubElement(bbox,'ymax').text = str(botr[1])
    xml_str = ET.tostring(annotaion)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root,pretty_print=True)
    savepath = os.path.join(savedir,img.name.replace('jpg','xml'))
    with open(savepath,'wb') as temp_xml:
        temp_xml.write(xml_str)
    #return xml_str

if __name__ =='__main__':
    folder = 'images'
    img = [im for im in os.scandir('images') if '000001' in im.name][0]
    objects = ['ironman']
    tl = [(10,10)]
    br = [(100,100)]
    savedir = 'atton'
    write_xml(folder, img, objects, tl, br, savedir)
    #print(xml_str)

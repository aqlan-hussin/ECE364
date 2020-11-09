#! /usr/local/bin/python3.4
import numpy as np
import zlib
import base64
from imageio import *
#from scipy.misc import *
import json
from os.path import join
from collections import OrderedDict
import re
import copy

class Payload:

    def __init__(self, rawData=None, compressionLevel=-1, json=None):
        if rawData is None and json is None:
            raise ValueError("Error: Both rawData and json are not provided.")
        if compressionLevel > 9 or compressionLevel < -1:
            raise ValueError("Error: compressionLevel can only be between -1 and 9 inclusively.")
        if rawData is not None and isinstance(rawData,np.ndarray) == False:
            raise TypeError("Error: Incorrect type for rawData.")
        if json is not None and type(json) != str:
            raise TypeError("Error: Incorrect type for json.")
        if rawData is not None:
            self.rawData = rawData
            self.json = self.getJson(self.rawData,compressionLevel)
        else:
            self.json = json
            self.rawData = self.getData(self.json)
        pass

    def getJson(self, rawData, compressionLevel):
        if len(rawData.shape) == 1:
            jtype = "text"
            jsize = None
            #txt = []
            #for x in rawData:
            #    txt.append(x)
            txt = rawData.flatten()
            array1D = np.asarray(txt,dtype=np.uint8)
        elif len(rawData.shape) == 2:
            jtype = "gray"
            jsize = "{0},{1}".format(rawData.shape[0],rawData.shape[1])
            #pixels = []
            #for x in rawData:
            #    for y in x:
            #        pixels.append(y)
            pixels = rawData.flatten()
            array1D = np.asarray(pixels,dtype=np.uint8)
        else:
            jtype = "color"
            jsize = "{0},{1}".format(rawData.shape[0],rawData.shape[1])
            #r = []
            #g = []
            #b = []
            #for x in rawData:
            #    for y in x:
            #        r.append(y[0])
            #        g.append(y[1])
            #        b.append(y[2])
            #pixels = r + g + b
            pixels = rawData.flatten()
            array1D = np.asarray(pixels,dtype=np.uint8)

        jcomp = False
        if compressionLevel != -1:
            jcomp = True
            array1D = zlib.compress(array1D,compressionLevel)

        #data = ','.join(str(s) for s in array1D)
        #img_data = data.encode('utf-8')

        jdata = base64.b64encode(array1D)
        jdata = jdata.decode('utf-8')

        #{'type':jtype,'size':jsize,'isCompressed':jcomp,"content":jdata}
        dict = OrderedDict([('type',jtype),('size',jsize),('isCompressed',jcomp),("content",jdata)])

        return json.dumps(dict,separators=(',',':'))

    def parseLine(self, lines):
        dict = {}
        fields = re.findall(r'\"[^\"]+\"|true|false|null',lines)
        i = 0
        while i < len(fields):
            key = re.findall(r'[^\"]+',fields[i])[0]
            val = re.findall(r'[^\"]+',fields[i+1])[0]
            dict[key] = val
            i += 2
        return dict

    def getData(self, json):
        dict = self.parseLine(json)

        data = dict.get("content")
        data = data.encode('utf-8')
        data = base64.b64decode(data)
        #data = data.decode('utf-8')
        #data = data.split(',')
        #array1D = []
        #for items in data:
        #    array1D.append(int(items))
        #array1D = np.asarray(data,dtype='uint8')

        if dict.get("isCompressed") == "true":
            data = zlib.decompress(data)

        #array1D = np.asarray(data,dtype=np.uint8)
        array1D = list(data)

        if dict.get("type") == "color":
            shape = dict.get("size").split(',')
            shape[0] = int(shape[0])
            shape[1] = int(shape[1])
            #size = shape[0] * shape[1]
            #size = int(len(array1D)/3)
            #r = array1D[:size]
            #g = array1D[size:2*size]
            #b = array1D[2*size:]
            #pixels = []
            #for i in range(size):
            #    pixels.append(r[i])
            #    pixels.append(g[i])
            #    pixels.append(b[i])
            shape.append(3)
            array1D = np.asarray(array1D, dtype=np.uint8)
            rawData = np.resize(array1D,tuple(shape))
        elif dict.get("type") == "gray":
            shape = dict.get("size").split(',')
            shape[0] = int(shape[0])
            shape[1] = int(shape[1])
            array1D = np.asarray(array1D, dtype=np.uint8)
            rawData = np.resize(array1D,tuple(shape))
        else:
            rawData = np.asarray(array1D,dtype=np.uint8)

        return rawData

class Carrier:

    def __init__(self, img):
        if isinstance(img,np.ndarray) == False:
            raise TypeError("Error: Incorrect type for img.")
        if len(img.shape) != 3:
            raise ValueError("Error: Given img contains less than 3 dimensions.")
        self.img = img
        pass

    def payloadExists(self):
        red = (self.img[:,:,0]).flatten()[:3]
        green = self.img[:,:,1].flatten()[:3]
        blue = self.img[:,:,2].flatten()[:3]
        alpha = self.img[:,:,3].flatten()[:3]
        bitStr = '{"t'
        redbstr = list(map(lambda x:'{0:08b}'.format(x), red))
        greenbstr = list(map(lambda x:'{0:08b}'.format(x), green))
        bluebstr = list(map(lambda x:'{0:08b}'.format(x), blue))
        alphabstr = list(map(lambda x:'{0:08b}'.format(x), alpha))
        charList = []
        for i in [0,1,2]:
            charstr = alphabstr[i][-2:] + bluebstr[i][-2:] + greenbstr[i][-2:] + redbstr[i][-2:]
            charstr = chr(int(charstr,2))
            charList.append(charstr)
        bits = ''.join(charList)

        if bits == bitStr:
            return True
        else:
            return False

    def clean(self):
        new = copy.deepcopy(self.img)
        size = self.img.shape
        bitarray = ['00', '01', '10', '11']
        new_img = new.flatten()
        new_array = []
        for items in new_img:
            item = '{0:08b}'.format(items)[0:6] + bitarray[np.random.randint(0,4,1)[0]]
            new_array.append(int(item,2))
        new_array = np.asarray(new_array, dtype=np.uint8)
        new_array = np.resize(new_array, size)
        #for i in range(len(new)):
        #    for j in range(len(new[i])):
        #        for k in range(len(new[i][j])):
        #            if new[i][j][k] % 2 != 0:
        #                new[i][j][k] &= 0xFE
        #new = np.bitwise_and(new,~(np.random.randint(0,3,1)[0]))
        return new_array

    def embedPayload(self, payload, override=False):
        if isinstance(payload, Payload) == False:
            raise TypeError("Error: Incorrect type for payload.")
        if override == False and self.payloadExists():
            raise Exception("Carrier already contains a payload!")

        data = payload.json
        array = np.fromstring(data,dtype=np.uint8)
        carrier_size = self.img.shape[0] * self.img.shape[1] * 4
        #if len(payload.rawData.shape) == 1:
        #    payload_size = payload.rawData.shape[0]
        #elif len(payload.rawData.shape) == 2:
        #    payload_size = payload.rawData.shape[0] * payload.rawData.shape[1]
        #else:
        #    payload_size = payload.rawData.shape[0] * payload.rawData.shape[1] * 3
        payload_size = len(array) * 4

        if payload_size > carrier_size:
            raise ValueError("Error: Payload size is larger than what the carrier can hold.")

        red = (self.img[:,:,0]).flatten()
        green = (self.img[:,:,1]).flatten()
        blue = (self.img[:,:,2]).flatten()
        alpha = (self.img[:,:,3]).flatten()
        #count = 0
        #bits =  list(map(lambda x:'{0:08b}'.format(x), data))

        for i in range(len(array)):
            bitstr = '{0:08b}'.format(array[i])
            falpha = '{0:08b}'.format(alpha[i])
            alpha[i] = int(falpha[0:6]+bitstr[0:2],2)
            fblue = '{0:08b}'.format(blue[i])
            blue[i] = int(fblue[0:6]+bitstr[2:4],2)
            fgreen = '{0:08b}'.format(green[i])
            green[i] = int(fgreen[0:6]+bitstr[4:6],2)
            fred = '{0:08b}'.format(red[i])
            red[i] = int(fred[0:6]+bitstr[6:8],2)

        new_carrier = []

        for i in range(len(alpha)):
            new_carrier.append(red[i])
            new_carrier.append(green[i])
            new_carrier.append(blue[i])
            new_carrier.append(alpha[i])

        new_carrier = np.asarray(new_carrier)
        new_img = np.resize(new_carrier, (self.img.shape[0], self.img.shape[1], 4))

        return new_img

    def extractPayload(self):
        red = (self.img[:,:,0]).flatten()
        green = (self.img[:,:,1]).flatten()
        blue = (self.img[:,:,2]).flatten()
        alpha = (self.img[:,:,3]).flatten()
        json = ""
        for i in range(len(red)):
            falpha = '{0:08b}'.format(alpha[i])
            fblue = '{0:08b}'.format(blue[i])
            fgreen = '{0:08b}'.format(green[i])
            fred = '{0:08b}'.format(red[i])
            new_byte = falpha[6:8] + fblue[6:8] + fgreen[6:8] + fred[6:8]
            new_char = chr(int(new_byte,2))
            json += new_char
            if new_char == '}':
                break

        return Payload(json=json)


if __name__ == "__main__":
    img = imread(join("data", "payload1.png"))
    #gray = imread(join("data", "payload2.png"))
    #txt = np.fromstring(join("data", "payload3.txt"), dtype=np.uint8)
    p1 = Payload(rawData=img, compressionLevel=-1)
    #with open("test.json", 'w') as file1:
    #    file1.write(p1.json)
    #p2 = Payload(json=p1.json)
    #print(type(p1.json))
    #print(isinstance(p2.rawData,np.ndarray))
    #no_payload = imread(join("data", "carrier.png"))
    #with_payload = imread(join("data", "embedded3_5.png"))
    #check = Carrier(no_payload)
    #print(check.payloadExists())
    #new = check.embedPayload(p1)
    embedded = imread(join("data", "embedded1_-1.png"))
    new_carrier = Carrier(embedded)
    extracted = new_carrier.extractPayload()
    print(extracted.rawData == p1.rawData)
    #new_carrier = Carrier(new)
    #print(new_carrier.payloadExists())
    #clean = check.clean()
    #clean = Carrier(clean)
    #print(clean.payloadExists())

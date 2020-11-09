import numpy as np
import zlib
import base64
import copy
from scipy.misc import *
from os.path import join
import re
import random

class Payload:

    def __init__(self, img=None, compressionLevel=-1, content=None):

        self.img = None
        self.content = None
        self.xml = ''

        if img is None and content is None:
            raise ValueError("Error: Both img and content are not provided.")

        if img is not None and content is not None:
            raise ValueError("Error: Only one between img and content should be provided.")

        if compressionLevel > 9 or compressionLevel < -1:
            raise ValueError("Error: compressionLevel is greater than 9 or less than -1.")

        if img is not None and type(img) != np.ndarray:
            raise TypeError("Error: Incorrrect type for img.")

        if content is not None and type(content) != np.ndarray:
            raise TypeError("Error: Incorrect type for content.")

        if content is not None:
            self.content = content
            self.img = self.getImg(self.content, compressionLevel)
        else:
            self.img = img
            self.content = self.getContent(self.img, compressionLevel)


    def getContent(self, img, compressionLevel):

        table = {}
        table['A']=0;table['B']=1;table['C']=2
        table['D']=3;table['E']=4;table['F']=5
        table['G']=6;table['H']=7;table['I']=8
        table['J']=9;table['K']=10;table['L']=11
        table['M']=12;table['N']=13;table['O']=14
        table['P']=15;table['Q']=16;table['R']=17
        table['S']=18;table['T']=19;table['U']=20
        table['V']=21;table['W']=22;table['X']=23
        table['Y']=24;table['Z']=25;table['a']=26
        table['b']=27;table['c']=28;table['d']=29
        table['e']=30;table['f']=31;table['g']=32
        table['h']=33;table['i']=34;table['j']=35
        table['k']=36;table['l']=37;table['m']=38
        table['n']=39;table['o']=40;table['p']=41
        table['q']=42;table['r']=43;table['s']=44
        table['t']=45;table['u']=46;table['v']=47
        table['w']=48;table['x']=49;table['y']=50
        table['z']=51;table['0']=52;table['1']=53
        table['2']=54;table['3']=55;table['4']=56
        table['5']=57;table['6']=58;table['7']=59
        table['8']=60;table['9']=61;table['+']=62
        table['/']=63

        r = []
        g = []
        b = []

        for x in img:
            for y in x:
                r.append(y[0])
                g.append(y[1])
                b.append(y[2])
        pixels = r + g + b
        pixels = np.asarray(pixels,dtype='uint8')

        size = img.shape
        size = str(size[0]) + "," + str(size[1])
        compressed = '"False"'

        if compressionLevel != -1:
            pixels = zlib.compress(pixels,compressionLevel)
            compressed = '"True"'

        data = ','.join(str(s) for s in pixels)


        xml = '<?xml version="1.0" encoding="UTF-8"?>' + '<payload type="Color" size="' + size + '" compressed=' + compressed + '>' + data + '</payload>'
        self.size = len(data)
        img_data = xml.encode('utf-8')
        new_data = base64.b64encode(img_data)
        padding = len(new_data) % 4
        if padding != 0:
            new_data += b'=' * (4 - padding)
        new_data = str(new_data).split("'")[1]
        mydata = list(new_data)

        myList = []

        for items in mydata:
            for k,v in table.items():
                if items == k:
                    myList.append(v)

        #encoded = ','.join(str(s) for s in myList)

        content = np.asarray(myList,dtype='uint8')

        return content


    def getImg(self, content, compressionLevel):

        table = {}
        table[0]='A';table[1]='B';table[2]='C'
        table[3]='D';table[4]='E';table[5]='F'
        table[6]='G';table[7]='H';table[8]='I'
        table[9]='J';table[10]='K';table[11]='L'
        table[12]='M';table[13]='N';table[14]='O'
        table[15]='P';table[16]='Q';table[17]='R'
        table[18]='S';table[19]='T';table[20]='U'
        table[21]='V';table[22]='W';table[23]='X'
        table[24]='Y';table[25]='Z';table[26]='a'
        table[27]='b';table[28]='c';table[29]='d'
        table[30]='e';table[31]='f';table[32]='g'
        table[33]='h';table[34]='i';table[35]='j'
        table[36]='k';table[37]='l';table[38]='m'
        table[39]='n';table[40]='o';table[41]='p'
        table[42]='q';table[43]='r';table[44]='s'
        table[45]='t';table[46]='u';table[47]='v'
        table[48]='w';table[49]='x';table[50]='y'
        table[51]='z';table[52]='0';table[53]='1'
        table[54]='2';table[55]='3';table[56]='4'
        table[57]='5';table[58]='6';table[59]='7'
        table[60]='8';table[61]='9';table[62]='+'
        table[63]='/'


        cList = content.tolist()
        myList = []
        for items in cList:
            for k,v in table.items():
                if items == k:
                    myList.append(v)

        mydata = ''.join(str(s) for s in myList)
        img_data = mydata.encode('utf-8')
        padding = len(img_data) % 4
        if padding == 3:
            img_data += '='.encode('utf-8')
        if padding == 2:
            img_data += '='.encode('utf-8') + '='.encode('utf-8')
        pixels = base64.b64decode(img_data)
        xml = pixels.decode('utf-8')
        self.xml = xml
        #with open("test2.txt",'w') as file1:
        #    file1.write(str(xml))
        comp = xml.split('"')[9]
        data = xml.split('>')[2]
        data = data.split('<')[0]
        data = data.split(',')


        dataList = []
        for items in data:
            dataList.append(int(items))

        dataList = bytearray(dataList)
        if comp == "True":
            data2 = zlib.decompress(dataList)
            data2List = [int(x) for x in data2]
        else:
            data2List = dataList

        #pixels2 = pixels.decode('utf-8')

        #data2 = pixels2.split('>')[2]
        #data2 = data2.split('<')[0]
        #data2 = data2.split(',')


        #for items in data2:
        #    data2List.append(int(items))

        #with open("test2.txt",'w') as file1:
        #    file1.write(str(pixels2))

        size = xml.split('"')[7]
        size = size.split(',')
        shape = [int(x) for x in size]
        #for items in size:
        #    shape.append(int(items))
        #print(len(data2List))

        r = data2List[:shape[0]*shape[1]]
        g = data2List[shape[0]*shape[1]:2*shape[0]*shape[1]]
        b = data2List[2*shape[0]*shape[1]:3*shape[0]*shape[1]]
        image = []
        for i in range(shape[0]*shape[1]):
            image.append(r[i])
            image.append(g[i])
            image.append(b[i])

        shape.append(3)

        imgList = np.reshape(image,tuple(shape))

        return np.array(imgList, dtype='uint8')


class Carrier:

    def __init__(self,img):

        if type(img) != np.ndarray:
            raise TypeError("Error: Incorrect type for img")
        self.img = img


    def payloadExists(self):
        table = {}
        table[0]='A';table[1]='B';table[2]='C'
        table[3]='D';table[4]='E';table[5]='F'
        table[6]='G';table[7]='H';table[8]='I'
        table[9]='J';table[10]='K';table[11]='L'
        table[12]='M';table[13]='N';table[14]='O'
        table[15]='P';table[16]='Q';table[17]='R'
        table[18]='S';table[19]='T';table[20]='U'
        table[21]='V';table[22]='W';table[23]='X'
        table[24]='Y';table[25]='Z';table[26]='a'
        table[27]='b';table[28]='c';table[29]='d'
        table[30]='e';table[31]='f';table[32]='g'
        table[33]='h';table[34]='i';table[35]='j'
        table[36]='k';table[37]='l';table[38]='m'
        table[39]='n';table[40]='o';table[41]='p'
        table[42]='q';table[43]='r';table[44]='s'
        table[45]='t';table[46]='u';table[47]='v'
        table[48]='w';table[49]='x';table[50]='y'
        table[51]='z';table[52]='0';table[53]='1'
        table[54]='2';table[55]='3';table[56]='4'
        table[57]='5';table[58]='6';table[59]='7'
        table[60]='8';table[61]='9';table[62]='+'
        table[63]='/'

        pixels = self.img.flatten()
        pixels = pixels[0:12]
        myList = []

        binlist = list(map(lambda x: format(x % 4, '02b'), pixels))
        binlist = np.array(binlist)
        binlist = np.reshape(binlist, (4,3))
        binstr = list(map(lambda x: x[2] + x[1] + x[0], binlist))
        binstr = list(map(lambda x: '0b' + x, binstr))
        cList = list(map(lambda x: int(x,2), binstr))
        for items in cList:
            for k,v in table.items():
                if items == k:
                    myList.append(v)

        xml = ''.join(myList)

        return (xml.encode('utf-8') == base64.b64encode('<?x'.encode('utf-8')))

    def clean(self):

        randomList = [0xFF,0xFE,0xFD,0xFC]
        new_img = copy.deepcopy(self.img)
        for i in range(len(new_img)):
            for j in range(len(new_img[i])):
                for k in range(len(new_img[i][j])):
                    new_img[i][j][k] &= random.choice(randomList)
        return new_img


    def embedPayload(self, payload, override=False):

        if type(payload) != Payload:
            raise TypeError('Error: Incorrect type for payload')
        if override == False and self.payloadExists() == True:
            raise Exception('Carrier already contains a payload')

        new_img = copy.deepcopy(self.img)
        content = payload.content

        if len(content)*3 > len(new_img.flatten()):
            raise ValueError('Error: Carrier size should be larger than payload size')

        r = []
        g = []
        b = []
        for x in self.img:
            for y in x:
                r.append(y[0])
                g.append(y[1])
                b.append(y[2])

        cList = content.tolist()
        binred = list(map(lambda x,y: format(x, '08b')[:6] + format(y, '06b')[4:6],r,cList))
        bingreen = list(map(lambda x,y: format(x, '08b')[:6] + format(y, '06b')[2:4],g,cList))
        binblue = list(map(lambda x,y: format(x, '08b')[:6] + format(y, '06b')[:2],b,cList))

        for i in range(len(binred)):
            binred[i] = int(binred[i],2)
            bingreen[i] = int(bingreen[i],2)
            binblue[i] = int(binblue[i],2)

        binred += r[len(cList):len(new_img.flatten())]
        bingreen += g[len(cList):len(new_img.flatten())]
        binblue += b[len(cList):len(new_img.flatten())]

        myList = []
        for i in range(len(binred)):
            myList.append([binred[i],bingreen[i],binblue[i]])

        new = np.reshape(myList, self.img.shape)

        return np.array(new,dtype='uint8')


    def extractPayload(self):

        if self.payloadExists() == False:
            raise Exception('Carrier does not contain any payload')

        table = {}
        table[0]='A';table[1]='B';table[2]='C'
        table[3]='D';table[4]='E';table[5]='F'
        table[6]='G';table[7]='H';table[8]='I'
        table[9]='J';table[10]='K';table[11]='L'
        table[12]='M';table[13]='N';table[14]='O'
        table[15]='P';table[16]='Q';table[17]='R'
        table[18]='S';table[19]='T';table[20]='U'
        table[21]='V';table[22]='W';table[23]='X'
        table[24]='Y';table[25]='Z';table[26]='a'
        table[27]='b';table[28]='c';table[29]='d'
        table[30]='e';table[31]='f';table[32]='g'
        table[33]='h';table[34]='i';table[35]='j'
        table[36]='k';table[37]='l';table[38]='m'
        table[39]='n';table[40]='o';table[41]='p'
        table[42]='q';table[43]='r';table[44]='s'
        table[45]='t';table[46]='u';table[47]='v'
        table[48]='w';table[49]='x';table[50]='y'
        table[51]='z';table[52]='0';table[53]='1'
        table[54]='2';table[55]='3';table[56]='4'
        table[57]='5';table[58]='6';table[59]='7'
        table[60]='8';table[61]='9';table[62]='+'
        table[63]='/'

        r = []
        g = []
        b = []
        for x in self.img:
            for y in x:
                r.append(y[0])
                g.append(y[1])
                b.append(y[2])

        #binred = list(map(lambda x: format(x % 4, '02b'), r))
        #bingreen = list(map(lambda x: format(x % 4, '02b'), g))
        #binblue = list(map(lambda x: format(x % 4, '02b'), b))
        cList = []
        for i in range(len(r)):
            binred = format(r[i] % 4, '02b')
            bingreen = format(g[i] % 4, '02b')
            binblue = format(b[i] % 4, '02b')
            binlist = binblue + bingreen + binred
            cList.append(binlist)
        aList = []
        for items in cList:
            aList.append(int(items,2))

        #binlist = list(map(lambda x,y,z: '0b' + x + y + z, binblue, bingreen, binred))
        #cList = list(map(lambda x: int(x,2), binlist))
        myList = []
        for items in aList:
            myList.append(table.get(items))
        xmlstr = ''.join(myList)
        xmlstr = xmlstr.encode('utf-8')

        padding = len(xmlstr) % 4
        if padding == 3:
            xmlstr += '='.encode('utf-8')
        if padding == 2:
            xmlstr += '='.encode('utf-8') + '='.encode('utf-8')

        xmlstr = base64.b64decode(xmlstr)
        xmlstr = ''.join(list(map(chr, xmlstr)))
        #with open("test2.txt",'w') as file1:
        #    file1.write(str(xmlstr))

        regex = r'(.+)</payload>'
        m = re.search(regex,xmlstr)
        if m:
            xmlstr = m.group(1) + '</payload>'

        xmlstr = xmlstr.encode('utf-8')
        content = base64.b64encode(xmlstr)

        padding = len(content) % 3
        if padding == 2:
            content = content[0:-2]
        if padding == 1:
            content = content[0:-1]

        table = {}
        table['A']=0;table['B']=1;table['C']=2
        table['D']=3;table['E']=4;table['F']=5
        table['G']=6;table['H']=7;table['I']=8
        table['J']=9;table['K']=10;table['L']=11
        table['M']=12;table['N']=13;table['O']=14
        table['P']=15;table['Q']=16;table['R']=17
        table['S']=18;table['T']=19;table['U']=20
        table['V']=21;table['W']=22;table['X']=23
        table['Y']=24;table['Z']=25;table['a']=26
        table['b']=27;table['c']=28;table['d']=29
        table['e']=30;table['f']=31;table['g']=32
        table['h']=33;table['i']=34;table['j']=35
        table['k']=36;table['l']=37;table['m']=38
        table['n']=39;table['o']=40;table['p']=41
        table['q']=42;table['r']=43;table['s']=44
        table['t']=45;table['u']=46;table['v']=47
        table['w']=48;table['x']=49;table['y']=50
        table['z']=51;table['0']=52;table['1']=53
        table['2']=54;table['3']=55;table['4']=56
        table['5']=57;table['6']=58;table['7']=59
        table['8']=60;table['9']=61;table['+']=62
        table['/']=63

        myList = []
        for items in list(content):
            myList.append(table.get(chr(items)))

        numarr = np.array(myList,dtype='uint8')

        payload = Payload(content=numarr)

        return payload

if __name__ == '__main__':
    img1 = imread(join("data", "payload1.png"))
    img2 = np.array([[[1, 2, 3], [4,5,6]], [[7,8,9], [10,11,12]]])

    #P = Payload(img=img2)
    #p2 = Payload(content=P.content)
    #referenceArrays = np.load(join("data", "arrays.npz"))
    #content1_6 = referenceArrays["content1_6"]
    #P = Payload(content=content1_6)
    #(Carrier(img=imread('data/result1_6.png')).extractPayload())

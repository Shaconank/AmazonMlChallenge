from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt
from PIL import Image
from constants import entity_unit_map
from units import unit_variations
import re
ocr = PaddleOCR(use_angle_cls=True, lang='en')


img_path = './61QsBSE7jgL.jpg'


result = ocr.ocr(img_path, cls=True)

import re

def find_all_indexes(s, substring):
    # Compile the regex pattern for the substring
    pattern = re.compile(re.escape(substring))
    # Find all the starting indexes of the substring
    matches = pattern.finditer(s)
    return [match.start() for match in matches]

output=set()

for line in result[0]:
    for unit in entity_unit_map['item_weight']:
            for representation in unit_variations[unit]:
                text = line[1][0]
                print(text)
                inds = find_all_indexes(text.lower(),representation.lower())
                print(inds)
                for ind in inds:
                    if ind == 0:
                         continue
                    printer = 0
                    stringnew = text[:ind]

                    if stringnew[ind -1].isspace():
                        stringnew = stringnew.strip()
                        stringnew = stringnew.replace(' ','')
                    ind = len(stringnew) -1
                    i = ind
                    print(i,representation,stringnew)
                    while stringnew[i].isdigit() and i>=0:
                        printer = 1
                        i -=1
                        print(i,representation,stringnew)
                    if printer:
                            output.add(stringnew[i+1:]+' '+unit)
                        
print(output)

                    
                    
                     
                     

image = Image.open(img_path).convert('RGB')
boxes = [item[0] for item in result[0]]
texts = [item[1][0] for item in result[0]]
scores = [item[1][1] for item in result[0]]


im_show = draw_ocr(image, boxes, texts, scores, font_path=r'D:\Programming\Rainforest\Code\PaddleOCR\doc\fonts\latin.ttf')
im_show = Image.fromarray(im_show)

plt.imshow(im_show)
plt.axis('off')
plt.show()

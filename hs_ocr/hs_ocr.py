import ddddocr

ocr = ddddocr.DdddOcr()

with open("test2.png", 'rb') as f:
    image = f.read()

res = ocr.classification(image)

print(res)

with open('example.txt', 'w') as f:
    f.write(res)

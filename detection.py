import cv2
import pandas as pd

img = cv2.imread("img-test/img1.jpg")
imgWidth = img.shape[1] - 40

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
csv = pd.read_csv("colors.csv", header = None, names = index)

r = g = b = x_pos = y_pos = 0
def getRGBvalue(event, x, y, flags, param):
    global r, g, b, x_pos, y_pos
    event, flags, param
    x_pos, y_pos = x, y
    b, g, r = img[y, x]
    b, g, r = int(b), int(g), int(r)
    
    
def getNameColor(R, G, B):
    minimum = 10 ** 3
    for i in range(len(csv)):
        dist = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if (dist <= minimum):
            minimum = dist
            color_name = csv.loc[i, "color_name"]
    return color_name

def getRGBtext(R, G, B):
    R, G, B = str(R) + ' ' * (4 - len(str(R))), str(B) + ' ' * (4 - len(str(B))), str(G) + ' ' * (4 - len(str(G)))
    return 'R = ' + R + '  G = ' + G + '  B = ' + B

def colorDetection(): 
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", getRGBvalue)
                
    while True:
        cv2.imshow("Image", img)
        cv2.rectangle(img, (10, 10), (imgWidth + 30, 40), (b, g, r), -1)

        scalar = (255, 255, 255) if r + g + b < 600 else (0, 0, 0)
        cv2.putText(img, getNameColor(r, g, b), (30, 32), 1, 1.2, scalar, 1, cv2.LINE_AA)    
        cv2.putText(img, getRGBtext(r, g, b), (imgWidth - 280, 32), 1, 1.2, scalar, 1, cv2.LINE_AA)    

        if cv2.waitKey(20) & 0xFF == 27:
            break
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    colorDetection()

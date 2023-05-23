import cv2
import sys
import matplotlib.pyplot as plt

DEFAULT_FILE = "input.txt"
DEFAULT_THRESHOLD = 128

# TODO fix this mess
def settingsFromArgs(args):
    filename = DEFAULT_FILE
    threshold = DEFAULT_THRESHOLD
    i = 1
    while i < len(args):
        if args[i] == '-f':
            filename = args[(i := i + 1)]
        elif args[i] == '-t':
            threshold = int(args[(i := i + 1)])
        i += 1
    return (filename, threshold)

# TODO error handling
def getGreyscale(filename, threshold):
    img = cv2.imread(filename = filename, flags=cv2.IMREAD_GRAYSCALE)
    grey = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return grey

def displayImage(img):
    plt.imshow(img,'gray',vmin=0,vmax=255)
    plt.title("result")
    plt.xticks([]),plt.yticks([])
    plt.show()

def main():
    if not len(sys.argv) % 2:
        print("usage: imageAnalysis\n\t-f [filename]\n\t-t [threshold]")
        raise RuntimeError("invalid args")
    (filename, threshold) = settingsFromArgs(sys.argv)

    img = cv2.imread(filename = filename, flags=cv2.IMREAD_GRAYSCALE)
    ret, grey = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    displayImage(grey)

if __name__ == '__main__':
    main()
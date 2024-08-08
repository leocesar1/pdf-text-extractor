import os

# lib to create a progress bar --------
from tqdm import tqdm 

from PIL import Image
import pytesseract
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# append info in result file   --------
import csv
def addContentToFile(content, fileName): #"result.csv"
    try:
        hasHeader = True if os.stat("file").st_size > 0 else False
    except:
        hasHeader = False
    print(hasHeader)

    with open(fileName, "a+", newline="") as myfile:
        w = csv.DictWriter(myfile, content.keys())
        if not hasHeader:
            w.writeheader()
        w.writerow(content)

# import pdf file
import pypdfium2 as pdfium
def importPdfFile(path):
    pdf = pdfium.PdfDocument(path)
    nPages = len(pdf)
    return ( pdf, nPages ) 

def makeNewFileName(path, file): 
    originalFileName = file
    print("Original File Name: ", originalFileName)
    newImageFileName = path+"\\images\\"+originalFileName.replace(".pdf","")
    return newImageFileName

def convertPdfToImg(pdfFile,pageNumber,rootName):
    page = pdfFile.get_page(pageNumber)
    pil_image = page.render(
        scale=3,
        rotation=0,
        crop=(0, 0, 0, 0)
    )
    resultName = rootName+str(pageNumber)+".png"
    pil_image = pil_image.to_pil()
    pil_image.save(resultName)
    return resultName

def findTextInImgFile(imgPath,paramsList):
    text = extract_text_from_image(imgPath)
    resultConditions = {}
    for item in paramsList:
        resultConditions[f"param '{str(item)}'"] = item in text
    
    generalResult = True in list(resultConditions.values())
    return {
        "hasTextInThisFile": generalResult, 
        "details": resultConditions
    }

paramsList = [ "param1", "param2", "param3", "param4"]

thisdir = os.getcwd()
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".pdf"):
            newImageFileName = makeNewFileName(r,file)
            pdfFilePath = os.path.join(r, file)
            pdfFile, numberOfPages = importPdfFile(pdfFilePath)

            print("---------- getting pages ----------------")
            imgFileNameList = []
            for pageNumber in tqdm(range(numberOfPages)):
                imgFileName = convertPdfToImg(pdfFile,pageNumber,newImageFileName)
                imgFileNameList.append(imgFileName)
            
            print("Total pages: ", len(imgFileNameList))
            print("---------- verifying pages ----------------")
            for pageNumber in tqdm(range(len(imgFileNameList))):
                imgPath = imgFileNameList[pageNumber]
                verifyResult = findTextInImgFile(imgPath,paramsList)

                pageNumber = pageNumber + 1
                if verifyResult["hasTextInThisFile"]:
                    verifyResult["details"]["file"] = file
                    verifyResult["details"]["page"] = pageNumber
                    
                    addContentToFile(verifyResult["details"],"result.csv")
                    
            print("---------- cleaning aux files  ----------------")
            for i in tqdm(range(len(imgFileNameList))):
                item = imgFileNameList[i]
                os.remove(item)
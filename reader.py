# Uses PyPDF2
# Uses textract
# Uses nltk
# uses punkt
# uses python's built-in CSV

import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json


#write a for-loop to open many files
filename = 'my-test.pdf'

#open allows you to read the file
pdfFileObj = open(filename,'rb')

#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#discerning the number of pages will allow us to parse through all the pages
num_pages = pdfReader.numPages
count = 0
text = ""

#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()

# This if statement exists to check if the above library returned words.
# It's done because PyPDF2 cannot read scanned files.

if text != "":
   text = text

# If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

else:
   text = textract.process(fileurl, method='tesseract', language='eng')

# The word_tokenize function will break our text phrases into individual words.
tokens = word_tokenize(text)

#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',']

#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords

stop_words = stopwords.words('english')

#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
my_list = []

# convert keywords to utf-8
for word in keywords:
  word = str(word)
  my_list.append(word)

with open("my_data.json", 'w') as outfile:
  json.dump(my_list, outfile)
# # Write to CSV
# with open("output.csv", "w") as csvFile:
#   writer = csv.writer(csvFile, delimiter=",", quotechar="'")
#   writer.writerows(my_list)

print(my_list)
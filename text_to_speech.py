import  pyttsx3,PyPDF3 


pdfreader = PyPDF3.PdfFileReader(open("book-35.pdf", "rb"))
engine = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_txt = text.strip().replace('\n',' ')
    print(clean_txt)

engine.save_to_file(clean_txt, "art-of-living-35.mp3")
engine.runAndWait()

engine.stop()
# import PyPDF2
# import pyttsx3
# import pdfplumber

# file = "book.pdf"

# book = open(file, 'rb')
# pdf_Reader = PyPDF2.PdfReader(book)
# pages = pdf_Reader.pages
# finalText = ''
# print(pages)

# for num in range(0, pages):
#     page = pdf_Reader.getPage[num]
#     text = page.extract_text()
#     player = pyttsx3.init()
#     player.say(text)
#     player.runAndWait()

# # engine = pyttsx3.init()
# # engine.save_to_file(finalText, 'art_of_living.mp3')
# # engine.runAndWait()

# # book.close()
import pyttsx3
import PyPDF2

hikaye=open("metin.pdf","rb")
pdfokuyucu= PyPDF2.PdfFileReader(hikaye)

engine=pyttsx3.init()
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id) 

for sayfano in range(0,pdfokuyucu.numPages):
    sayfa=pdfokuyucu.getPage(sayfano)
    yazi=sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()

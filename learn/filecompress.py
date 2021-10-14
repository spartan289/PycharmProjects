import site
site.addsitedir("...pathToPDFTron\PDFNetWrappersWin32\PDFNetC\Lib")
from PDFNetPython3.PDFNetPython import PDFNet,PDFDoc,Optimizer, SDFDoc
PDFNet.Initialize('demo:1631960088233:78ca97a5030000000045aae80a06716738822d52a66f7799dbb253da5d')
pdf = PDFDoc('evs.pdf')
pdf.InitSecurityHandler()

# Optimize the document
Optimizer.Optimize(pdf)
pdf.Save('evscomp.pdf', SDFDoc.e_linearized)
pdf.Close()

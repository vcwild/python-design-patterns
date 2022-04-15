from template import CSVMiner, PDFMiner


csv = CSVMiner()
pdf = PDFMiner()

csv.algorithm("morganna.csv")
print("\n")
pdf.algorithm("morganna.pdf")

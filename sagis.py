import tabula
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
# readinf the PDF file that contain Table Data
# you can find find the pdf file with complete code in below
# read_pdf will save the pdf table into Pandas Dataframe
df = tabula.read_pdf("SWB20191010.pdf",multiple_tables=True)
tabula.convert_into("SWB20191010.pdf","SWB20191010.xlsx", output_format="xlsx",pages=2)
# in order to print first 5 lines of Table
tabula.read_pdf("/home/abdo/Documents/GrainRSA/SWB20191010.pdf", area=(197,633,273,633), pages=0)

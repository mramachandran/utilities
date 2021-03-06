from sqlalchemy import create_engine
import urllib
import os
import pandas as pd
from datetime import datetime
import calendar
import numpy as np
import shutil
## Change Path, update userid and password before running

corePath = 'C://projects//datamodel//datamodelexport'

params = 'DRIVER={ODBC Driver 13 for SQL Server};' \
         'SERVER=*****;' \
         'PORT=1433;' \
         'DATABASE=ReportingDataModel;' \
         'UID=******;'\
         'PWD=******;'
            
# params = urllib.parse.quote_plus(params)
# engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params)

def moveFiles(source,fname,destination):
    shutil.copy(source+"\\"+fname,destination)

sqldirectory = 'C://projects//datamodel//datamodelexport' #change path here

for fname in os.listdir(sqldirectory):
    fullname = os.path.join(sqldirectory, fname) 

    filenamewithoutextension = os.path.splitext(fname)[0] 
    outputfilename = filenamewithoutextension + ".csv"
    print(fullname)
    
    df = pd.read_csv(fullname, sep=',')
    df.to_sql(filenamewithoutextension, engine, index=False)

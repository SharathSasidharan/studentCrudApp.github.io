import pymysql
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib import colors
pdf=SimpleDocTemplate("MyDocc.pdf")
flow_obj=[]
td=[["ROLLNO","NAME","EMAIL","GENDER","CONTACT","DATEOFBIRTH","ADDRESS"]]
con=pymysql.connect(host="localhost",user="root",password="",database="stm")
cur=con.cursor()
cur.execute("select * from students")
data_row=cur.fetchall()      
for row in data_row:
        data=[row[0],row[1],row[2],row[3],row[4],row[5],row[6]]
        td.append(data)
      #   print(td)   
table=Table(td) 
ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.red),
                ("BACKGROUND",(0,0),(-1,0),colors.yellow)])
table.setStyle(ts)
flow_obj.append(table)
pdf.build(flow_obj)
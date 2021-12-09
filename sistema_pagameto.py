from tkinter import*   
import random
import time
import datetime

payroll = Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Sistema Folha de Pagamento")


def EXIT():
    payroll.destroy()
    
def RESET():
    
    EMPREGADO.set() 
    ENDERECO.set("") 
    PONTO.set("")
    VENDA.set("") 
    EMPREGO.set("") 
    HEXTRA.set("") 
    SALARIO.set("")  
    COMISSAO.set("")  
    TAXA.set("") 
    IMPOSTOS.set("") 
    PAYDAY.set("")
    SINDICATO.set("") 
    TRIBUTO.set("")
    FISCAL.set("")  
    TAXASINDICATO.set("") 
    ULTIMOPAGAMENTO.set("") 
        
def REFE():
    
    PAYDAY.set(time.strftime("%d/%m/%y"))
    #PAYDAY.set(time.strftime("%x"")) 
    
    REFEPONTO = random.randint(1400, 2965)
    REFEPO= ("CARTÃO " + str(REFEPONTO))
    PONTO.set(REFEPO)
    
  
    SINDICATOREFEN= ("FORA BOSO")
    SINDICATO.set(SINDICATOREFEN)
    

        
def DIAPAGAMENTO():
    
    i = datetime.datetime.now()
    TAXA.set(i.month)  
    

def SALARIOMENSAL():
    SM = float (SALARIO.get())
    SALARIOMENSAL.set(SALARIO)
    
def SALARIOCOMISSAO():
    
    SC = float(TAXA.get() * VENDA.get())
    PISO = 3000
    SALARIOCOM = "R$", str('%.2f'% (SC + PISO))
    COMISSAO.set(SALARIOCOM)
    
def SALARIOHORA():

    SH = float(TAXA.get() * HEXTRA.get())
    PISO = 3000
    SALARIOHORISTA = "R$", str('%.2f'% (SH + PISO))
    VENDA.set(SALARIOHORISTA)
    
#horista = 3000 + comissao por hora = TAXA * hora extra
#assalariado  = piso 3000
#comissionado = piso 3000 + comissao por venda = TAXA * RESULTADO DA VENDA
    
PISO = StringVar()
EMPREGADO = StringVar()
ENDERECO = StringVar() 
PONTO = StringVar() 
VENDA = StringVar()
EMPREGO= StringVar()
HEXTRA = StringVar() #HORAEXTRA
SALARIO = StringVar() #SALARIO(ASSALARIADO)
COMISSAO = StringVar()
TAXA = StringVar()
IMPOSTOS = StringVar()
PAYDAY = StringVar()
SINDICATO = StringVar()
TRIBUTO = StringVar()
FISCAL = StringVar() 
TAXASINDICATO = StringVar()
ULTIMOPAGAMENTO = StringVar()
FORMAPAGAMENTO = StringVar()

Tops= Frame(payroll, width= 1350, height=50)
Tops.pack(side= TOP)
LF= Frame(payroll, width= 700, height=650)
LF.pack(side=LEFT)
RF= Frame(payroll, width= 600, height=650)
RF.pack(side=RIGHT)

lblInfo = Label (Tops, font= ('arial', 50 ,'bold'), text = "Sistema Folha de Pagamento", fg="steel blue", bd=8, relief="raise")
lblInfo.grid(row=0,column=0)

#--------------------------------LADO ESQUERDO---------------------------------------------

LeftInsideLF= Frame(LF, width= 600, height= 200, bd=8, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF= Frame(LF, width= 600, height= 200, bd=8, relief="raise")
LeftInsideLFLF.pack(side=LEFT)

#--------------------------------LADO ESQUERDO/TOP------------------------------------------

lblEMPREGADO = Label (LeftInsideLF, font= ('arial', 12 ,'bold'), text = "NOME DO EMPREGADO", 
                      fg="steel blue", bd=1, anchor ='w')
lblEMPREGADO.grid(row=0,column=0)
txtEMPREGADO = Entry (LeftInsideLF, font= ('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable= EMPREGADO)
txtEMPREGADO.grid(row=0, column=1)

lblENDERECO = Label (LeftInsideLF, font= ('arial', 12 ,'bold'), text = "ENDEREÇO", 
                      fg="steel blue", bd=1, anchor ='w')
lblENDERECO.grid(row=1,column=0)
txtENDERECO = Entry (LeftInsideLF, font= ('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable= ENDERECO)
txtENDERECO.grid(row=1, column=1)

lblEMPREGO= Label (LeftInsideLF, font= ('arial', 12 ,'bold'), text = "TIPO DE EMPREGO", 
                      fg="steel blue", bd=1, anchor ='w')
lblEMPREGO.grid(row=2,column=0)
txtEMPREGO = Entry (LeftInsideLF, font= ('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable= EMPREGO) #tipodetrabalhador
txtEMPREGO.grid(row=2, column=1)

#--------------------------------LADO ESQUERDO/ESQUERDO-----------------------------------

lblVENDA = Label (LeftInsideLFLF, font= ('arial', 12 ,'bold'), text = "RESULTADO DE VENDA", 
                      fg="steel blue", bd=1, anchor ='w')
lblVENDA.grid(row=2,column=0)
txtVENDA= Entry (LeftInsideLFLF, font =('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable=VENDA)
txtVENDA.grid(row=2, column=1)

lblHEXTRA = Label (LeftInsideLFLF, font= ('arial', 12 ,'bold'), text = "HORA EXTRA", 
                      fg="steel blue", bd=1, anchor ='w')
lblHEXTRA.grid(row=3,column=0)
txtHEXTRA = Entry (LeftInsideLFLF, font= ('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable = HEXTRA)
txtHEXTRA.grid(row=3, column=1)

lblTAXA = Label (LeftInsideLFLF, font= ('arial', 12 ,'bold'), text = "TAXA", 
                      fg="steel blue", bd=1, anchor ='w')
lblTAXA.grid(row=4,column=0)
txtTAXA = Entry (LeftInsideLFLF, font= ('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable= TAXA)
txtTAXA.grid(row=4, column=1)

lblCOMISSAO = Label (LeftInsideLFLF, font= ('arial', 12 ,'bold'), text = "COMISSÃO", 
                      fg="steel blue", bd=1, anchor ='w')
lblCOMISSAO.grid(row=5,column=0)
txtCOMISSAO = Entry (LeftInsideLFLF, font= ('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable = COMISSAO)
txtCOMISSAO.grid(row=5, column=1)



#--------------------------------LADO DIREITO---------------------------------------------

RightInsideLF=Frame(RF, width= 600, height= 200, bd=8, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF= Frame(RF, width= 300, height= 200, bd=8, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF= Frame(RF, width= 300, height= 200, bd=8, relief="raise")
RightInsideRFRF.pack(side=RIGHT)

#--------------------------------LADO DIREITO/TOP------------------------------------------

lblSALARIO = Label (RightInsideLF, font= ('arial', 12 ,'bold'), text = "SALARIO", 
                      fg="steel blue", bd=1, anchor ='w')
lblSALARIO.grid(row=0,column=0)
txtSALARIO = Entry (RightInsideLF, font= ('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable = SALARIO)
txtSALARIO.grid(row=0, column=1)

lblPONTO = Label (RightInsideLF, font= ('arial', 12 ,'bold'), text = "CARTÃO DE PONTO", 
                      fg="steel blue", bd=1, anchor ='w')
lblPONTO.grid(row=1,column=0)
txtPONTO =  Entry (RightInsideLF, font =('arial', 12 ,'bold'), bd = 20, width= 40, 
                      bg="steel blue", justify = 'right', textvariable=PONTO)
txtPONTO.grid(row=1, column=1)

#--------------------------------LADO DIREITO/ESQUERDO---------------------------------------------

lblULTIMOPAGAMENTO= Label (RightInsideLFLF, font= ('arial', 12 ,'bold'), text = "ULTIMO PAGAMENTO", 
                      fg="steel blue", bd=1, anchor ='w')
lblULTIMOPAGAMENTO.grid(row=0,column=0)
txTULTIMOPAGAMENTO = Entry (RightInsideLFLF, font= ('arial', 12 ,'bold'), bd = 20, width= 20, 
                      bg="steel blue", justify = 'right', textvariable = ULTIMOPAGAMENTO)
txTULTIMOPAGAMENTO.grid(row=0, column=1)

lblPAYDAY = Label (RightInsideLFLF, font= ('arial', 12 ,'bold'), text = "ATUAL PAGAMENTO", 
                      fg="steel blue", bd=1, anchor ='w')
lblPAYDAY.grid(row=1,column=0)
txtPAYDAY = Entry (RightInsideLFLF, font= ('arial', 12 ,'bold'), bd = 20, width= 20, 
                      bg="steel blue", justify = 'left', textvariable=PAYDAY)
txtPAYDAY.grid(row=1, column=1)

lblFORMAPAGAMENTO = Label (RightInsideLFLF, font= ('arial', 12 ,'bold'), text = "FORMA DE PAGAMENTO", 
                      fg="steel blue", bd=1, anchor ='w')
lblFORMAPAGAMENTO.grid(row=2,column=0)
txtFORMAPAGAMENTO = Entry (RightInsideLFLF, font= ('arial', 12 ,'bold'), bd = 20, width= 20, 
                      bg="steel blue", justify = 'left', textvariable=FORMAPAGAMENTO)
txtFORMAPAGAMENTO.grid(row=2, column=1)

lblSINDICATO = Label (RightInsideLFLF, font= ('arial', 12 ,'bold'), text = "SINDICATO", 
                      fg="steel blue", bd=1, anchor ='w')
lblSINDICATO.grid(row=3,column=0)
txtSINDICATO = Entry (RightInsideLFLF, font= ('arial', 12 ,'bold'), bd = 20, width= 20, 
                      bg="steel blue", justify = 'left', textvariable=SINDICATO)
txtSINDICATO.grid(row=3, column=1)

lblTAXASINDICATO = Label (RightInsideLFLF, font= ('arial', 12 ,'bold'), text = "TAXA SINDICATO", 
                      fg="steel blue", bd=1, anchor ='w')
lblTAXASINDICATO.grid(row=4,column=0)
txtTAXASINDICATO = Entry (RightInsideLFLF, font= ('arial', 12 ,'bold'), bd = 20, width= 20, 
                      bg="steel blue", justify = 'left', textvariable=TAXASINDICATO)
txtTAXASINDICATO.grid(row=4, column=1)

#------------------------------------BOTTOMS------------------------------------------------------------------

btnwagepaymnet= Button(RightInsideRFRF, padx = 8, bd= 8, fg = "black", font= ('arial', 20 ,'bold'),
                       width=14,text = "PAGAMENTO", bg= "sky blue", command = SALARIOMENSAL).grid(row=0,column=0)

btnREFE= Button(RightInsideRFRF, padx = 8, bd= 8, fg = "black", font= ('arial', 20 ,'bold'),
                       width=14,text = "REFERÊNCIA", bg= "sky blue", command = REFE).grid(row=1,column=0)

btnCOMISSAO= Button(RightInsideRFRF, padx = 8, bd= 8, fg = "black", font= ('arial', 20 ,'bold'),
                       width=14,text = "COMISSÃO", bg= "sky blue", command = SALARIOCOMISSAO).grid(row=2,column=0)

btnPROCURAR= Button(RightInsideRFRF, padx = 8, bd= 8, fg = "black", font= ('arial', 20 ,'bold'),
                       width=14,text = "PROCURAR", bg= "sky blue").grid(row=3,column=0)

btnRESET= Button(RightInsideRFRF, padx = 8, bd= 8, fg = "black", font= ('arial', 20 ,'bold'),
                       width=14,text = "RESETE", bg= "sky blue", command= RESET).grid(row=4,column=0)

btnSAIR= Button(RightInsideRFRF, padx = 8, bd= 8, fg = "black", font= ('arial', 20 ,'bold'),
                       width=14,text = "SAIR", bg= "sky blue", command = EXIT).grid(row=5,column=0)











payroll.mainloop()
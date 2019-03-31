import csv

singleCheat = 0
singleNoCheat = 0

marriedCheat = 0
marriedNoCheat = 0

divorcedCheat = 0
divorcedNoCheat = 0

jmlSingle = 0
jmlMarried = 0
jmlDivorced = 0

jmlRule = 0
list_data = []
def printRule(status):
    global jmlRule
    jmlRule += 1
    print('Rule', jmlRule, ': if marital status ==', status, 'then diizinkan')
    return;

def lastStep(list_data, maritalStatus):
    vTaxNoCheat = 0
    vTaxCheat = []
    vNoCheat = 0
    vCheat = 0
    for row in list_data:
        if(row['marital status'] == maritalStatus and row['refund'] == 'no'):
             if(row['Cheat'] == 'no'):
                 vTaxNoCheat = row['Taxable Income']
             else:
                 vTaxCheat.append(row['Taxable Income'])
    hasilSorting=sorted([vTaxCheat])
    listSorting = hasilSorting[0]
    if(vTaxNoCheat < listSorting[0]):
        global jmlRule
        jmlRule += 1
        print('Rule', jmlRule, ': if marital status ==', maritalStatus, 'and refund == no and Taxable Income Kurang dari ',
              listSorting[0], 'and Taxable Income Lebih dari ',vTaxNoCheat,'then diizinkan')
             
    
        
        
def nextStep(list_data, maritalStatus):
    vRefundNoCheat = 0
    vRefundCheat = 0
    vNoCheat = 0
    vCheat = 0
    for row in list_data:
        if(row['marital status'] == maritalStatus and row['refund'] == 'yes'):
            if(row['Cheat'] == 'no'):
                vRefundNoCheat += 1
            else:
                vRefundCheat += 1  
        if(row['marital status'] == maritalStatus and row['refund'] == 'no'):
            if(row['Cheat'] == 'no'):
                vNoCheat += 1
            else:
                vCheat += 1
    
    if(vRefundCheat == 0 and vNoCheat == 0 ):
                   global jmlRule
                   jmlRule += 1
                   print('Rule', jmlRule, ': if marital status ==', maritalStatus, 'and refund == yes then diizinkan')

    else:
        lastStep(list_data, maritalStatus)

def checkRule(jmlSingle, jmlMarried, jmlDivorced, singleNoCheat, marriedNoCheat, divorcedNoCheat, list_data):
                if(jmlSingle == singleNoCheat):
                   printRule('Single')
                if(jmlDivorced == divorcedNoCheat):
                    printRule('Divorced')
                if(jmlMarried == marriedNoCheat):
                    printRule('Married')
                if(jmlSingle != singleNoCheat):
                    nextStep(list_data,'single')
                if(jmlDivorced != divorcedNoCheat):
                    nextStep(list_data,'divorced')
                if(jmlMarried != marriedNoCheat):
                    nextStep(list_data, 'married')
                


with open('classification.csv') as f:
    reader = csv.DictReader(f, delimiter=',')

    for row in reader:
        list_data.append(row)
        if((row['marital status']) == 'married'):
            if(row['Cheat'] == 'yes'):
                marriedCheat += 1
            else:
                marriedNoCheat += 1
        elif((row['marital status']) == 'single'):
            if(row['Cheat'] == 'yes'):
                singleCheat += 1
            else:
                singleNoCheat += 1
        else:
            if(row['Cheat'] == 'yes'):
                divorcedCheat += 1
            else:
                divorcedNoCheat += 1

    jmlSingle = singleNoCheat - singleCheat
    jmlMarried = marriedNoCheat -  marriedCheat 
    jmlDivorced =  divorcedNoCheat - divorcedCheat 


    checkRule(jmlSingle, jmlMarried, jmlDivorced, singleNoCheat, marriedNoCheat, divorcedNoCheat, list_data)



    

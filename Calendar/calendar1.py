import calendar
from re import search
from function import *
import csv
y=2023
m2=12
mm=''
year=''
dd=''
minutes=''
hour=''
jam=0
id=0      #id event
l2=[]
m=month(y,m2)
print('\n_________________________________________________\n')
print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:\n')
#while version != '' and version != 'q' and version != 'single':
#    version=str(input ('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:'))
print('    "-" για πλοήγηση στον προηγούμενο μήνα\n')
print('    "+" για διαχείριση των γεγονότων του ημερολογίου\n')
print('    "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα\n')
move1=str(input("    ->"))
print('\n----------------------------------------------------\n')
while move1!='q':
    if move1=='-':
        n=int(m2)-1
        m2=n
        if (n<=0):
            print ('Δεν υπάρχει προηγούμενος μήνας για το ετος', y)
        else:
            m=month(int(y),m2)
    if move1=='+':
        print('Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:\n')
        print('    1 Καταγραφή νέου γεγονότος\n')
        print('    2 Διαγραφή γεγονότος\n')
        print('    3 Ενημέρωση γεγονότος\n')
        print('    0 Επιστροφή στο κυρίως μενού\n')
        move2=int(input("    ->"))
        if move2==1:
            datetime=(str(input('Ημερομηνία γεγονότος, σε μορφή ΥΥΥΥ-ΜΜ-DD')))
            year=''
            mm=''
            dd=''
            for i in range(0,4):
                year=year+datetime[i]
            for j in range(5,7):
                mm=mm+datetime[j]
            for n in range(8,10):
                dd=dd+datetime[n]
            while (int(year)<2022 or int(mm)<1 or int(mm)>12 or int(dd)<1 or int(dd)>31):
                datetime=(str(input('Ημερομηνία γεγονότος, σε μορφή ΥΥΥΥ-ΜΜ-DD')))
                year=''
                mm=''
                dd=''
                for i in range(0,4):
                    year=year+datetime[i]
                for j in range(5,7):
                    mm=mm+datetime[j]
                for n in range(8,10):
                    dd=dd+datetime[n]
            y=year    #gia ektyposh mhna
            m2=mm     #gia ektyposh mhna
            time=(str(input('Ώρα γεγονότος, σε μορφή HH:MM ')))
            minutes=''
            hour=''
            for i in range(0,2):
                hour=hour+time[i]
            for i in range(3,5):
                minutes=minutes+time[i]
            while (int(hour)<=0 or int(hour)>=24) or (int(minutes)<=0 or int(minutes)>=60):
                time=(str(input('Ώρα γεγονότος, σε μορφή HH:MM ')))
                minutes=''
                hour=''
                for i in range(0,2):
                    hour=hour+time[i]
                for i in range(3,5):
                    minutes=minutes+time[i]
            duration=(int(input('Διάρκεια γεγονότος')))
            while duration<0 and duration!=int:
                duration=(int(input('Διάρκεια γεγονότος')))
            
            title=(str(input('Τίτλος γεγονότος')))
            while "," in title:
                title=(str(input('Τίτλος γεγονότος')))
            if jam==0:
                d=date(datetime,time,duration,title)
            else:
                  a=add(datetime,time,duration,title)
            print("\nΤο γεγονός καταγράφηκε")
            st=''
            st=str(id)+". "+ "["+title+"]"+ " -> Date: "+ datetime +", Time : "+time+ ", Duration : "+str(duration)
            lista.append([st])
            id+=1
            #p=printing()
            e=event_list(lista)
            for i in range(len(lista)):
                print(e[i][0])
            jam+=1
            m3=month(int(y),int(m2))
        elif move2==2:#diagrafh event
            ye=str(input('Εισάγεται έτος: '))
            mon=str(input('Εισάγεται μήνα: '))
            y=ye     #gia ektyposh mhna
            m2=mon    #gia ektyposh mhna
            #e=event_list(lista)
            f=find_list(ye,mon,l2)
            e=event_list(l2)
            for i in range(len(l2)):
                print(e[i][0])
            de=str(input('Δώσε τίτλο γεγονότος προς διαγραφή: '))
            d=delete(de)
            for i in range(0,len(lista)):
                if (search(de,lista[i][0])):
                    lista[i].remove(lista[i][0])
            print("Το γεγενός διαγράφθηκε ")
            m3=month(int(y),int(m2))
        elif move2==3:#enhmervsh
            p=0   #gia na dw an allaxe kati vste na diafraftei
            print("==== Αναζήτηση γεγονότων ====")
            e=str(input('Εισάγεται έτος: '))
            mh=str(input('Εισάγεται μήνα: '))
            y=e     #gia ektyposh mhna
            m2=mh    #gia ektyposh mhna
            f=find_list(e,mh,l2)
            e=event_list(l2)
            for i in range(len(l2)):
                print(e[i][0])
            pick=int(input("Επιλέξτε γεγονός προς ενημέρωση: "))
            dap=input("Ημερομηνία γεγονότος: ")
            if (dap!=''):
                r=remaked(pick,dap)
                lista.remove(lista[pick])
            hp=input("Ώρα γεγονότος: ")
            if (hp!=''):
                r=remakeh(pick,hp)
                p+=1
            dp=input("Διάρκεια γεγονότος: ")
            if (dp!=''):
                r=remakedp(pick,dp)
                p+=1
            tp=input("Τίτλος γεγονότος: ")
            if (tp!=''):
                remaketp(pick,tp)
                p+=1
            print("Το γεγονός ενημερώθηκε ")
            df = pd.read_csv("event.csv")
            print(df)
            m4=month(int(y),int(m2))
            
        elif move2==0:
            m=month(int(y),int(m2))
        
    elif move1=="*":
        y=str(input('Εισάγεται έτος: '))
        mo=str(input('Εισάγεται μήνα: '))
        f=find_list(y,mo,l2)
        e=event_list(l2)
        for i in range(len(l2)):
            print(e[i][0])
        t=str(input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:"))
    #m=month(int(y),int(mm))
    print('_________________________________________________\n')
    print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:\n')
    print('    "-" για πλοήγηση στον προηγούμενο μήνα\n')
    print('    "+" για διαχείριση των γεγονότων του ημερολογίου\n')
    print('    "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα\n')
    move1=str(input("    ->"))
    print('\n----------------------------------------------------\n')


 

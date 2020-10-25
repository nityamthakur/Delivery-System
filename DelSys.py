import mysql.connector

import matplotlib.pyplot as plt; plt.rcdefaults()

import numpy as np

import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    
  host="localhost",
  
  user="root",
  
  passwd="root",
  
  database="school"
  
)

mycursor = mydb.cursor()

while True:
    
    print('Welcome')
    
    print('1.Show existing records')
    
    print('2.Add new records')
    
    print('3.View deadlines')
    
    print('4.Show statistics')
    
    print('5.Exit')
    
    choicemain=input('Enter your choice: ')
    
    if choicemain=='1':
        
        #To show records that already exist
        
        mycursor.execute("SELECT * from delivery")
        
        myresult = mycursor.fetchall()
        
        for x in myresult:
            
            print(x)
            
        print('Order By: ')
        
        print('1.Date of Order')
        
        print('2.Date of Delivery')
        
        print('3.City of Delivery')
        
        print('4.Name of Reciever')
        
        print('5.Size of Item')
        
        print('6.Exit')
        
        choice1=input('Enter your choice: ')
        
        if choice1=='1':
            
            #To order by the date of order
            
            mycursor = mydb.cursor()
            
            sql = "SELECT * FROM delivery ORDER BY Date_Ordered"
            
            mycursor.execute(sql)
            
            myresult = mycursor.fetchall()
            
            for x in myresult:
                
                print(x)
                
        if choice1=='2':
            
            #To order by date of delivery
            
            mycursor = mydb.cursor()
            
            sql = "SELECT * FROM delivery ORDER BY Date_of_Delivery"
            
            mycursor.execute(sql)
            
            myresult = mycursor.fetchall()
            
            for x in myresult:
                
                print(x)
                
        if choice1=='3':
            
            #To order by city of delivery
            
            mycursor = mydb.cursor()
            
            sql = "SELECT * FROM delivery ORDER BY City_of_Delivery"
            
            mycursor.execute(sql)
            
            myresult = mycursor.fetchall()
            
            for x in myresult:
                
                print(x)
                
        if choice1=='4':
            
            #To order by Name of Reciever
            
            mycursor = mydb.cursor()
            
            sql = "SELECT * FROM delivery ORDER BY Name_of_Reciever"
            
            mycursor.execute(sql)
            
            myresult = mycursor.fetchall()
            
            for x in myresult:
                
                print(x)
                
        if choice1=='5':
            
            #To order by Size of Item
            
            mycursor = mydb.cursor()
            
            sql = "SELECT * FROM delivery ORDER BY Size_of_Item"
            
            mycursor.execute(sql)
            
            myresult = mycursor.fetchall()

            for x in myresult:
                
                print(x)
                
        if choice1=='6':
            
              break
            
    if choicemain=='2':
        
        print('Launch MySQL to add new records in the database')

    if choicemain=='3':
        
        #To see deadline according to month
        
        mon=input('Enter the month: ')
        
        if mon=='august':
            
            #For August

            print('The following items need to be delivered by the end of August: ')

            mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=8")
            
            myresult = mycursor.fetchall()
            
            for x in myresult:
                
                print(x)
                
        if mon=='september':

            #For September
            
            print('The following items need to be delivered by the end of September: ')
            
            mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=9")
            
            myresult = mycursor.fetchall()
            
            for x in myresult:
                
                print(x)
                
        if mon=='october':
            
            #For October
            
            print('The following items need to be delivered by the end of October: ')
            
            mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=10")
            
            myresult = mycursor.fetchall()
            
            for x in myresult:
                
                print(x)
                
        if mon=='november':
            
            #For November
            
            print('The following items need to be delivered by the end of November: ')
            
            mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=11")
            
            myresult = mycursor.fetchall()
            
            for x in myresult:
                
                print(x)
                
    if choicemain=='4':
        
        #To show statistics
        
        print('What would you like to see: ')
        
        print('1.Bar graph according to Delivery Date')
        
        print('2.Pie chart')
        
        print('3.Exit')
        
        choice2=input('Enter your choice: ')
        
        if choice2=='1':
            
            #To show bar graphs
            
            print('How would you like to view your graph: ')
            
            print('1.Vertical Bar graph')
            
            print('2.Horizontal Bar graph')
            
            print('3.Exit')
            
            choice3=input('Enter your choice number: ')
            
            if choice3=='1':
                
                #To show vertical bar graph
                
                mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=8")
                
                myresult = mycursor.fetchall()
                
                count1=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=9")
                
                myresult = mycursor.fetchall()
                
                count2=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=10")
                
                myresult = mycursor.fetchall()
                
                count3=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=11")
                
                myresult = mycursor.fetchall()
                
                count4=mycursor.rowcount
                
                objects = ('August', 'September', 'October', 'November')
                
                y_pos = np.arange(len(objects))
                
                performance = [count1,count2,count3,count4,]
                
                plt.bar(y_pos, performance, align='center', alpha=0.5)
                
                plt.xticks(y_pos, objects)
                
                plt.ylabel('Number of Deliveries')
                
                plt.xlabel('Month')
                
                plt.title('Deliveries')
                
                plt.show()
                
            if choice3=='2':
                
                #To show horizontal bar graph
                
                mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=8")
                
                myresult = mycursor.fetchall()
                
                count1=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=9")
                
                myresult = mycursor.fetchall()
                
                count2=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=10")
                
                myresult = mycursor.fetchall()
                
                count3=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE month(Date_of_Delivery)=11")
                
                myresult = mycursor.fetchall()
                
                count4=mycursor.rowcount
                
                objects = ('August', 'September', 'October', 'November')
                
                y_pos = np.arange(len(objects))
                
                performance = [count1,count2,count3,count4]
                
                plt.barh(y_pos, performance, align='center', alpha=0.5)
                
                plt.yticks(y_pos, objects)
                
                plt.xlabel('Number of Deliveries')
                
                plt.ylabel('Month')
                
                plt.title('Deliveries')
                
                plt.show()
                
            if choice3=='3':
                
                break
            
        if choice2=='2':
            
            #To show Pie chart
            
            print('What would you like to see in your Pie chart: ')
            
            print('1.Pie chart according to City of Delivery')
            
            print('2.Pie chart according to Size of Item')
            
            print('3.Exit')
            
            choice4=input('Enter your choice number: ')
            
            if choice4=='1':
                
                #To show Pie chart according to city
                
                fig = plt.figure()
                
                ax = fig.add_axes([0,0,1,1])
                
                ax.axis('equal')
                
                mycursor.execute("SELECT * FROM delivery WHERE City_of_Delivery='Delhi'")
                
                myresult = mycursor.fetchall()
                
                count1=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE City_of_Delivery='Mumbai'")
                
                myresult = mycursor.fetchall()
                
                count2=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE City_of_Delivery='Banglore'")
                
                myresult = mycursor.fetchall()
                
                count3=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE City_of_Delivery='Kolkata'")
                
                myresult = mycursor.fetchall()
                
                count4=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE City_of_Delivery='Chennai'")
                
                myresult = mycursor.fetchall()

                count5=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE City_of_Delivery='Pune'")
                
                myresult = mycursor.fetchall()
                
                count6=mycursor.rowcount
                
                Cities = ['Delhi', 'Mumbai', 'Banglore', 'Kolkata', 'Chennai','Pune']
                
                Deliveries = [count1,count2,count3,count4,count5,count6]
                
                ax.pie(Deliveries, labels = Cities,autopct='%1.2f%%')
                
                plt.show()
                
            if choice4=='2':
                
                #To show Pie chart according to size
                
                fig = plt.figure()
                
                ax = fig.add_axes([0,0,1,1])
                
                ax.axis('equal')
                
                mycursor.execute("SELECT * FROM delivery WHERE Size_of_Item='Large'")
                
                myresult = mycursor.fetchall()
                
                count1=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE Size_of_Item='Medium'")
                
                myresult = mycursor.fetchall()
                
                count2=mycursor.rowcount
                
                mycursor.execute("SELECT * FROM delivery WHERE Size_of_Item='Small'")
                
                myresult = mycursor.fetchall()
                
                count3=mycursor.rowcount
                
                Sizes = ['Large', 'Medium', 'Small']
                
                Deliveries = [count1,count2,count3]
                
                ax.pie(Deliveries, labels = Sizes,autopct='%1.2f%%')
                
                plt.show()
                
            if choice4=='3':
                
                break
            
    if choicemain=='5':
        
        #To exit
        
        break

        
                        
        
            






























































































































































































































































































































































































































from bs4 import BeautifulSoup as bs
import urllib3 as ul

http = ul.PoolManager()
from csv import writer

with open("p14.csv",'w',newline='',encoding='utf-8') as csv_file:
    csv_writer=writer(csv_file)
    headers=["Company_Name","Address","Contact Person","Contact Person Designation","Phone_Number_1","Phone_Number_2","Email_id_1","Email_id_2","Email_id_3"]
    csv_writer.writerow(headers)

    url='https://www.aaaindia.org/membership/list-of-membersagencies/'
    response = http.request('GET',url)
    website=bs(response.data, 'lxml')
    cards=website.findAll("div",{"class":"grey_container"})
    # print(cards)
    for i in range(len(cards)):
        print(i)
        company_name=cards[i].find("h3")
        company_name1=company_name.text #Name of the company
        print(company_name1)
        url2=cards[i].find("a")
        details_ulr=url2['href']
        # print(details_ulr)
        detail_res= http.request('GET',details_ulr)
        website2=bs(detail_res.data, 'lxml')
        # print(website2)
        addr=website2.find("div",{"class":"grey_container"})
        ps=addr.find_all("p")
        address=ps[1].text.strip().replace("\n",'').replace("–",' ').replace("’",'').replace("‘",'') #Address of a company
        print(address)
        c_person=ps[2]
        c1 = str(c_person).split("<br/>")
        c2=c1[0].replace("<p>",'').replace('\n','').replace("              ",'')
        if i==19:
            per_name = c2.split("-")
            con_name = per_name[0] #Name of contact person
            con_design = per_name[1].replace("&amp;",'&') #Designation of a person
        elif (i==34) or (i==36) or (i==50) or (i==72) or (i==94):
            con_name=c2
            con_design=''
        elif i==113:
            per_name=c2.split("(")
            con_name=per_name[0]
            con_design=per_name[1].replace(")",'').replace("–",'')
        else:
            per_name = c2.split("–")
            con_name = per_name[0] #Name of contact person
            con_design = per_name[1].replace("&amp;",'&') #Designation of a person
        print(con_name)
        print(con_design)
        ph = c1[1].replace('<i class="fa fa-phone"></i>','').replace("\n",'')
        ph1 = ph.split("/")
        phone2=''
        for j in range(len(ph1)):
            if j==0:
                phone1 =ph1[0].replace(" – ",' ').replace("+",'') #phone number 1
                print(phone1)
            if j==1:
                phone2 = ph1[1] #phone number 2
                print(phone2)
        em3=''
        for i in range(2,len(c1)):
            if i==2:
                em1 = c1[2].replace('<i class="fa fa-envelope"></i>','').replace("\n",'') #Email 1
                print(em1)
            if i==3:
                em = c1[3].replace('<i class="fa fa-envelope"></i>','').replace("</p>",'').replace("\n",'') #Email 2
                emn=em.split("/")
                for k in range(len(emn)):
                    if k==0:
                        em2=emn[0]
                        print(em2)
                    if k==1:
                        em3=emn[1]
                        print(em3)
                # print(em2)      
        print("-------------------------------------------")

        csv_writer.writerow([company_name1,address,con_name,con_design,phone1,phone2,em1,em2,em3])

                
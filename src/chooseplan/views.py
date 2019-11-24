from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from .forms import chooseplanform
from .models import questions

# python local setting
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import psycopg2
import re
import pprint 
from itertools import chain

engine = create_engine("postgres+psycopg2://postgres:12221992@localhost:5432")
connection = engine.connect()
metadata = MetaData()
HCT = Table('Healthcare_Categories', metadata, autoload=True, autoload_with=engine)

Health_Care_Plans  =    [
                        {'Sharp_Silver_70_HMO': {"Specialist": '3S', 'Preventive_Care': "1PC", "Diagnostic_Test": "3DT", "Generic_Drugs": "4GD",
"Outpatien_Surgery":'3OS', 'Immediate_Medical_Attention': '3IMA', 'Outpatient_Services/Inpatient_Services': '1OSIS', 'Pregnant': "2P", 'Home_Health_Care': '3HHC',
'Rehabilitation_Services': '3RS', 'Skilled_Nursing_Care': '3SNC'}},
                        {'Kaiser_Covered_California_Silver_87_HMO' : {"Specialist": '1S', 'Preventive_Care': "2PC", "Diagnostic_Test": "2DT", "Generic_Drugs": "2GD",
"Outpatien_Surgery":'1OS', 'Immediate_Medical_Attention': '2IMA', 'Outpatient_Services/Inpatient_Services': '3OSIS', 'Pregnant': "4P", 'Home_Health_Care': '2HHC',
'Rehabilitation_Services': '1RS', 'Skilled_Nursing_Care': '2SNC'}},
                        {'LA_Coverd_Silver_70_HMO' : {"Specialist": '4S', 'Preventive_Care': "3PC", "Diagnostic_Test": "1DT", "Generic_Drugs": "3GD",
"Outpatien_Surgery":'4OS', 'Immediate_Medical_Attention': '4IMA', 'Outpatient_Services/Inpatient_Services': '4OSIS', 'Pregnant': "3P", 'Home_Health_Care': '4HHC',
'Rehabilitation_Services': '4RS', 'Skilled_Nursing_Care': '4SNC'}},
                        {'Blue_Shield_87_PPO_Silver' : {"Specialist": '2S', 'Preventive_Care': "4PC", "Diagnostic_Test": "1DT", "Generic_Drugs": "1GD",
"Outpatien_Surgery":'2OS', 'Immediate_Medical_Attention': '1IMA', 'Outpatient_Services/Inpatient_Services': '2OSIS', 'Pregnant': "1P", 'Home_Health_Care': '1HHC',
'Rehabilitation_Services': '2RS', 'Skilled_Nursing_Care': '1SNC'}}
]



# def chooseplan(request):
#     return render(request, 'chooseplan/chooseplan.html')

def chooseplan(request):
    if request.method == 'POST':
        form = chooseplanform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_chooseplan")
    else:
        form = chooseplanform()
    return render(request, 'chooseplan/chooseplan.html', {'form': form})


def show_chooseplan(request):
    plan_lists=''
    plan_lists += '<center><img src="http://jipadev.wpengine.com/wp-content/uploads/2013/07/Payor-Header.jpg" width="1600" height="400"</center>'
    plan_lists += '<center><h2>Here are the best plans for you condition</h2></center><br>'
    try:
        test_result = match_code1(ret_code1(get_data1("self")))
        if test_result == []:
            test_result = "No or not enough answers checked"
        # details = {'Here are the best plans for you condition': (test_result)}
        if 'Sharp_Silver_70_HMO' in test_result:
            plan_lists += '<center><h2>Sharp Silver 70HMO - For Sharp Silver Plan click:</h2></center><br>' 
            plan_lists += '<center><a href="https://www.sharphealthplan.com/docs/default-source/group-plans/2019/sg-sbc-on-exchange/20360_sbc_ccsb-sharp-premier-silver-70-hmo-2000-45-child-dental.pdf"><img src="https://www.healthforcalifornia.com/bundles/website/img/carrier-logos/sharp.png" style="width:200x;height:200px;border:0;"></a></center><br>'
        if 'Kaiser_Covered_California_Silver_87_HMO' in test_result:
            plan_lists += '<center><h2>Kaiser Covered California Silver 87 HMO - For Kaiser Covered California Silver Plan click:</h2></center><br>'
            plan_lists += '<center><a href="http://info.kaiserpermanente.org/healthplans/california/individual/pdfs/2019-ON-Exchange/Silver_87_HMO.pdf"><img src="https://1000logos.net/wp-content/uploads/2019/05/Kaiser-Permanente-Logo.png" style="width:400px;height:300px;border:0;"></a></center><br>'
        if 'LA_Coverd_Silver_70_HMO' in test_result:
            plan_lists += '<center><h2>LA Coverd Silver 70 HMO - For LA Coverd Silver plan click:</h2></center><br>'
            plan_lists += '<center><a href="https://www.lacare.org/sites/default/files/LA0922b_2019_LACC_SBC_Silver_70_1018.pdf"><img src="https://hitconsultant.net/wp-content/uploads/2019/09/Blue-Shield-of-CA-Announces-New-146-Million-Collaboration-Aimed-at-Keeping-Healthcare-Loca.png" style="width:400px;height:300px;border:0;"></a></center><br>'
        if 'Blue_Shield_87_PPO_Silver' in test_result:
            plan_lists += '<center><h2>Blue Shield 87 PPO Silver - For Blue Shield Silver plan click:</h2></center><br>'
            plan_lists += '<center><a href="https://www.blueshieldca.com/bsca/bsc/public/broker/PortalComponents/StreamDocumentServlet?fileName=Silver_87_PPO_1-18_SOB.pdf"><img src="https://mma.prnewswire.com/media/810201/blue_jpg_Logo.jpg?p=facebook" style="width:450px;height:300px;border:0;"></a></center><br>'
        plan_lists += '<br>'
        plan_lists += '<img src="http://digitalhealthage.com/wp-content/uploads/2015/09/Event-Integrated-health.jpg" width="1600" height="400">'
    except:
        test_result = "No or not enough answers checked"
    return HttpResponse(plan_lists)
    


def ret_code(provider_list):
    healthlist = [ ]
    for i in provider_list:
        ilist = list(i)
        for b in range (len(ilist)):
            if '32S' and '20S' in ilist:
                healthlist.append("1S")
            if '12PC' and '14PC' in ilist:
                healthlist.append("1PC")
            if '10DT' and '42DT' in ilist:
                healthlist.append("1DT")
            if '8GD' and '18GD' in ilist:
                healthlist.append("1GD")
            if '44OS' and '26OSSNC' in ilist:
                healthlist.append("1OS")
            if '36IMA' and '24IMARS' in ilist:
                healthlist.append("1IMA")
            if '34OSIS' and '40OSIS' in ilist:
                healthlist.append("1OSIS")
            if '16P' and '30P' in ilist:
                healthlist.append("1P")
            if '48HHC' and '46HHC' in ilist:
                healthlist.append("1HHC")
            if '38RS' and '24IMARS' in ilist:
                healthlist.append("1RS")
            if '28SNC' and '26OSSNC' in ilist:
                healthlist.append("1SNC")
            return healthlist

def match_code(hcp):
    final_outcome = [ ]
    final_outcome_improved = [ ]
    for mc in hcp:
        for hp in Health_Care_Plans:
            for plans in hp.values():
                for plans_attributes in plans.values():
                    if mc in plans_attributes:
                        final_outcome.append(list(hp.keys()))
                        for f in final_outcome:
                            if f not in final_outcome_improved:
                                final_outcome_improved.append(f)
                                finalized = list(chain(*final_outcome_improved))
    return (finalized)

# =================================

def get_data1(self):
    stmt = 'Select * From public."chooseplan_questions" Order By id DESC LIMIT 1'
    result_proxy = connection.execute(stmt)
    results = result_proxy.fetchall()
    return results



def ret_code1(provider_list):
    healthlist = [ ] 
    for i in provider_list:
        ilist = list(i)
        for b in range (len(ilist)):
            if '32S' and '20S' in ilist:
                healthlist.append("1S")
            if '12PC' and '14PC' in ilist:
                healthlist.append("1PC")
            if '10DT' and '42DT' in ilist:
                healthlist.append("1DT")
            if '8GD' and '18GD' in ilist:
                healthlist.append("1GD")
            if '44OS' and '26OSSNC' in ilist:
                healthlist.append("1OS")
            if '36IMA' and '24IMARS' in ilist:
                healthlist.append("1IMA")
            if '34OSIS' and '40OSIS' in ilist:
                healthlist.append("1OSIS")
            if '16P' and '30P' in ilist:
                healthlist.append("1P")
            if '48HHC' and '46HHC' in ilist:
                healthlist.append("1HHC")
            if '38RS' and '24IMARS' in ilist:
                healthlist.append("1RS")
            if '28SNC' and '26OSSNC' in ilist:
                healthlist.append("1SNC")
            return healthlist

def match_code1(hcp):
    final_outcome = [ ]
    final_outcome_improved = [ ]
    finalized = []
    for mc in hcp:
        for hp in Health_Care_Plans:
            for plans in hp.values():
                for plans_attributes in plans.values():
                    if mc in plans_attributes:
                        final_outcome.append(list(hp.keys()))
                        for f in final_outcome:
                            if f not in final_outcome_improved:
                                final_outcome_improved.append(f)
                                finalized = list(chain(*final_outcome_improved))
    return (finalized)


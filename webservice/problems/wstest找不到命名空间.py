# -*- coding: utf-8 -*-
import sys
sys.stdout.encoding
from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor

import json

from suds.xsd.doctor import Import, ImportDoctor
from suds.client import Client
#
# def ts():
#
#     # fix broken wsdl
#     # add <s:import namespace="http://www.w3.org/2001/XMLSchema"/> to the wsdl
#     imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
#     imp.filter.add('http://adm.entity.hsgy.com')
#     wsdl_url = 'http://122.225.12.166:88/services/HSGY_ADM001Service?wsdl'
#     client = Client(wsdl_url, doctor=ImportDoctor(imp))
#
#     # make request
#     arrayofstring = client.factory.create('HSGY_ADM001')
#     arrayofstring.string = [1, 2,1,2]
#
#     rs = client.service.HSGY_ADM001Service(1073757, arrayofstring, 99).string

def say_hello_test():
    wsdl_url = "http://122.225.12.166:88/services/HSGY_ADM001Service?wsdl"
    # wsdl_url = "http://127.0.0.1:8080/ws_py/service/cxfService?wsdl"

    #client = Client(wsdl_url)

    args = {
    "frepair_person_num":"0105010101",
    "frepair_person_name":"张先生",
    "frepair_number":"WX202009250004",
    "frepair_person_company":"030af0ca-dbd4-4bb3-b2ae-69c800d8bda2",
    "frepair_project":"空调维修",
    "frepair_person_dept":"030af0ca-dbd4-4bb3-b2ae-69c800d8bda2"
    }

    # args = {
    #     "id": 1,
    #     "goods": {"name":"hahah"}
    # }
    #
    #
    # args={
    #     "frepairNumber":{"frepair_number":"20200520231402"},
    #     "frepairPersonCompany":{"frepair_person_company":"嘉兴地区"},
    #     "frepairPersonDept":{"frepair_person_dept":"030af0ca-dbd4-4bb3-b2ae-69c800d8bda2"},
    #     "frepairPersonName":{"frepair_person_name","张先生"},
    #     "frepairPersonNum":{"frepair_person_num":"0105010101"},
    #     "frepairProject":{"frepair_project":"空调维修"}
    # }

    # args = {
    #     "frepairNumber": {"name":
    #           {"namespaceURI":"http://adm.entity.hsgy.com","localPart":"frepair_number"},"declaredType":"".__class__,
    #           "value":"20200520231402"},
    #
    #     "frepairPersonCompany": {"name":
    #           {"namespaceURI":"http://adm.entity.hsgy.com","localPart":"frepair_person_company"},"declaredType":"".__class__,
    #           "value":"嘉兴地区"},
    #
    #     "frepairPersonDept": {"name":
    #           {"namespaceURI":"http://adm.entity.hsgy.com","localPart":"frepair_person_dept"},"declaredType":"".__class__,
    #           "value":"030af0ca-dbd4-4bb3-b2ae-69c800d8bda2"},
    #     "frepairPersonName": {"name":
    #           {"namespaceURI":"http://adm.entity.hsgy.com","localPart":"frepair_person_name"},"declaredType":"".__class__,
    #           "value":"张先生"},
    #     "frepairPersonNum": {"name":
    #           {"namespaceURI":"http://adm.entity.hsgy.com","localPart":"frepair_person_num"},"declaredType":"".__class__,
    #           "value":"0105010101"},
    #     "frepairProject": {"name":
    #           {"namespaceURI":"http://adm.entity.hsgy.com","localPart":"frepair_project"},"declaredType":"".__class__,
    #           "value":"空调维修"}
    # }




    # # Import和DoctorImport是提供wsdl中缺少的import标签的
    # imp = Import("http://www.w3.org/2001/XMLSchema", location="http://www.w3.org/2001/XMLSchema.xsd")
    # imp.filter.add("http://adm.entity.hsgy.com")
    # imp.filter.add("webservices.services.weaver.com.cn")
    #
    # doctor = ImportDoctor(imp)
    # client = Client(wsdl_url, doctor=doctor)
    # rs = client.service.HSGY_ADM001(args)


    # python 连接java 解决命名空间找不到问题autoblend = True
    client = Client(wsdl_url, autoblend = True)
    rs = client.service.create001service(args)
    print(rs)


say_hello_test()
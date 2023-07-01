# Script hack to convert a vcf file to json
#

import sys
import json

import re
import json

'''
def ParseVcf(VcfPath):
    contacts = []
    with open(VcfPath, 'r') as vcf_file:
        vcf_data = vcf_file.read()
    
    vcf_entries = re.split(r'(?<=END:VCARD)\n', vcf_data)
    
    for entry in vcf_entries:
        contact = {}
        
        # Extract contact information using regular expressions
        name_match = re.search(r'FN:(.*)', entry)
        if name_match:
            contact['Name'] = name_match.group(1)
        
        email_match = re.search(r'EMAIL;.*?:([^;\n]+)', entry)
        if email_match:
            contact['Email'] = email_match.group(1)
        
        phone_match = re.findall(r'TEL;.*?:([^;\n]+)', entry)
        if phone_match:
            #contact['Phone'] = phone_match.group(1)
            print(f'   {phone_match}')
        
        if contact:
            contacts.append(contact)
    
    return contacts
'''

def ParseVcf(VcfPath):
    contacts = []
    with open(VcfPath, 'r') as vcf_file:
        vcf_data = vcf_file.read()
    
    vcf_entries = re.split(r'(?<=END:VCARD)\n', vcf_data)
    
    for entry in vcf_entries:
        lines = entry.splitlines()
        for line in lines:
            index = line.find(':')
            key = line[:index]
            value = line[index+1:]
            print(f'{key} = {value}')
        print()
    
    return contacts

def VcfToJason(VcfPath, JsonPath):
    contacts = ParseVcf(VcfPath)
    for contact in contacts:
        print(contact)
        print()
    
    #with open(JsonPath, 'w') as json_file:
    #    json.dump(contacts, json_file, indent=4)
    
    #print("Conversion completed. JSON file saved.")

def Main(argv):
    if (len(argv) < 2):
        print(f"Usage: {argv[1]} filename")

    VcfPath = argv[1]
    JsonPath = argv[1] + '.json'
    VcfToJason(VcfPath, JsonPath)

Main(sys.argv)

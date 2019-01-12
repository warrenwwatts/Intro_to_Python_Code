# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:57:30 2018
Program to create a readable mail digest from a mailbox
using RegEx.
@author: warren watts
"""




def file_to_list(file_name):
    """
    function: file_to_list, creates an array of text lines from a 
    file for processing.
              
    input: file_name - str with name of the file to be read.
    return: list of str, the lines of the file
    """
    
    from os.path import isfile
    text_list =[]
    if isfile(file_name):
        with open(file_name,'r') as file:
            for line in file:
                text_list.append(line)
    else:
        print(file_name + ' does not exist')
    return text_list

def list_to_file(text_list, file_name):
    """
    function: list_to_file, creates a file if no file exists with 
    file_name with each line of the file as a str in text_list.
    
    input: text_list - list of strings, assumed end with 
                       newline characters (\n)
           file_name - str with name of the file to be read.
    return: bool true if successful, false if file already exists
    """
    
    from os.path import isfile
    no_file  = not isfile(file_name)
    
    if no_file:
        with open(file_name,'w') as file:
            for line in text_list:
                file.write(line)
    else:
        print(file_name + ' already exists')
    return no_file


def mail_extract(text_list):
    """
    function: mail_extract, extracts From, Time, To, Subject and body of email
    
    input: text_list - raw mail box in list of lines form
    return: list of str, formatted email
    """
    import re
    # variables to find body of email and other fields
    body = False
    sender = ''
    dest = ''
    time = ''
    text_out = []
    
    for line in text_list:
        if re.search('^From\s\S+@\S+', line):
            # find end of message body
            body = False
            text_out.append('\n') # add blank line at end of message body
           
        elif re.search('^Date:\s[A-Z]', line):
            # extract time without GMT adjustment
            time = re.findall('(^Date:\s.+:[0-9]+:[0-9]+)', line)[0] + '\n'
        elif re.search('^From:\s\S+@\S+', line):
            # get real From: line
            sender = line
        elif re.search('^To:\s\S+@\S+', line):
            # get To: line
            dest = line
            
        elif re.search('^Subject:\s', line):
            # identify Subject line
            # add message header
            text_out.append(sender)
            text_out.append(dest)
            text_out.append(time)
            text_out.append(line) # subject line
        
        if body:
            text_out.append(line)
        
        if re.search('^X-DSPAM-Probability:', line):
            # find beginning of message body
            body = True
        
    return text_out
        
    
    
# read in mailbox from mbox3.txt
mail_box = file_to_list('mbox3.txt')
# extract mail digest
mail_digest = mail_extract(mail_box)
# write mail digest to digest.txt
list_to_file(mail_digest, 'digest.txt')



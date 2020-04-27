# Simon Ebelhar
# 10/05/2019
# SDEV300 

from flask import Flask
from datetime import datetime

app = Flask(__name__, static_url_path='/static')

# app file route to use after local IP:port to display product of code
@app.route('/Lab7', methods=['GET','POST'])

# Function to build HTML website in Python, via Flask, using other functions listed below
def mtb_website():
    mtb_website_run = heading_start();
    mtb_website_run += header1('Mountain Biking is Fun!')
    mtb_website_run += header3('Just get out there and DO IT')
    mtb_website_run += paragraph("Mountain biking is a great activity. It combines nature with speed and fun. It's faster than hiking, so you can cover more beautiful scenery, but not so fast as a motor vehicle so you don't just zoom past the scenery. It's a great workout too, but without even noticing the work because it's so much fun. And the best part is it's very accessible for most people! You don't have to be in great shape. Just get out there on some dirt and have some fun!")
    mtb_website_run += header2('Types of Mountain Bikes')
    mtb_website_run += unorderedList()
    mtb_website_run += "<A HREF='https://www.evo.com/guides/how-to-choose-mountain-bike'>Link to Details on Types of Mountain Bikes</A>"
    mtb_website_run += header2('UCI Downhill Men Elite Rankings')
    mtb_website_run += orderedList()
    mtb_website_run += "<A HREF='https://www.uci.org/mountain-bike/rankings'>Link to Full Standings</A>"
    mtb_website_run += header2('Photo of My Favorite Trail Area')
    mtb_website_run += "<A HREF='https://www.trailforks.com/photo/13539279/'>Link to User Photo of Trails I Ride</A>"
    mtb_website_run += pic1()
    mtb_website_run += pic2()
    mtb_website_run += pic3()
    mtb_website_run += pic4()
    mtb_website_run += bikeTable()
    mtb_website_run += form()
    mtb_website_run += time()
    mtb_website_run += heading_close()
    return mtb_website_run

def pic1():
    myPic = """<div><img src="/static/dannymac.jpg"></div>"""
    return myPic

def pic2():
    myPic = """<div><img src="/static/santa-cruz-instagram-02.jpg"></div>"""
    return myPic

def pic3():
    myPic = """<div><img src="/static/santa-cruz-instagram-09.jpg"></div>"""
    return myPic

def pic4():
    myPic = """<div><img src="/static/Santa_Cruz_Bronson.jpg"></div>"""
    return myPic

# Function to return the date and time
def time():
    now = datetime.now()
    newString = now.strftime('<br><br>%m/%d/%Y, %H:%M:%S')
    return newString
    
# Function to define title, open HTML, and open body of HTML webpage
def heading_start():
    heading_start_html = '<!-- Opening of HTML webpage until opening of body -->'
    heading_start_html = '<!DOCTYPE html> '
    heading_start_html +='<head> '
    heading_start_html +='<title>SDEV300 - Lab7</title>'
    heading_start_html += '<style>' + getStyle() + '</style>'
    heading_start_html +='</head>'
    heading_start_html +='<body>'
    return heading_start_html

# Function to format a 1st level HTML heading, passing argument as the heading text   
def header1(myString):
    newString = '<h1>' + myString + '</h1>'
    return newString

# Function to format a 2nd level HTML heading, passing argument as the heading text   
def header2(myString):
    newString = '<h2>' + myString + '</h2>'
    return newString

# Function to format a 3rd level HTML heading, passing argument as the heading text 
def header3(myString):
    newString = '<h3>' + myString + '</h3>'
    return newString
 
# Function to format a HTML paragraph, passing argument as the paragraph text 
def paragraph(myParagraph):
    newString = '<p>' + myParagraph + '<p>'
    return newString

# Function to return unordered list of types of mountain bikes
def unorderedList():
    listdata = '<ul>'
    listdata += '<li> Cross Country (XC) </li>'
    listdata += '<li> Trail </li>'
    listdata += '<li> All Mountain (Enduro) </li>'
    listdata += '<li> Downhill (DH) </li>'
    listdata += '</ul>'
    return listdata

@app.route('/Lab7/static', methods=['GET','POST'])
def form():
    formhtml = """<form action="/static/formdata.php" method='post'>"""
    formhtml += "<div>"
    with open('accounts.txt', mode='w')   as accounts:
        accounts.write('100 Jones   24.98\n')
    formhtml += "<label for='firstname'>First Name:</label>"
    formhtml += "<input type='text' name='firstname' id='firstname'>"
    formhtml += "</div>"
    formhtml += "<div>"
    formhtml += "<label for='lastname'>Last Name:</label>"
    formhtml += "<input type='text' name='lastname' id='lastname'>"
    formhtml += "</div>"
    formhtml += "<div>"
    formhtml += "<datalist id='dropper'>"
    formhtml += "<option value='V10'>"
    formhtml += "<option value='Nomad'>"
    formhtml += "<option value='Megatower'>"
    formhtml += "<option value='Hightower'>"
    formhtml += "<option value='Bronson'>"
    formhtml += "<option value='5010'>"
    formhtml += "</datalist>"
    formhtml += "<label>"
    formhtml += "Select Bike:"
    formhtml += "<input id='move' list='dropper'>"
    formhtml += "</label>"
    formhtml += "</div>"
    formhtml += "<div>"
    formhtml += "<label for='bikelove' style='display: block;'> Tell us why you love bikes! </label>"
    formhtml += """<textarea name='bikelove' rows=6 cols=50 placeholder="Spill your beans here (...fill in your answer)" id='bikelove'></textarea>"""
    formhtml += "</div>"
    formhtml += "<div>"
    formhtml += "<input type='submit' value='Submit'>"
    formhtml += "<input type='reset' value='Reset'>"
    formhtml += "</div>"
    formhtml += "</form>"
    return formhtml
    
# Funtion to return ordered list of UCI downhill mountain bike rankings   
def orderedList():
    listdata = '<ol>'
    listdata += '<li> Loic Bruni </li>'
    listdata += '<li> Amaury Pierron </li>'
    listdata += '<li> Troy Brosnan </li>'
    listdata += '<li> Danny Hart </li>'
    listdata += '<li> Greg Minnaar </li>'
    listdata += '</ol>'
    return listdata

def getStyle():
    myStyle = 'table,td {'
    myStyle += 'border: 1px  solid #999;'
    myStyle += '}'
    return myStyle

def bikeTable():
    bikedata = '<table> <thead>'
    bikedata += '<tr><th>Bike</th><th>Front Travel</th><th>Rear Travel</th></tr></thead>'
    bikedata += '<tbody><tr><td>V10</td> <td> 203mm </td> <td> 215mm </td></tr>'
    bikedata += '<tr><td>Nomad</td> <td> 170mm </td> <td> 170mm </td></tr>'
    bikedata += '<tr><td>Megatower</td> <td> 160mm </td> <td> 160mm </td></tr>'
    bikedata += '<tr><td>Hightower</td> <td> 150mm </td> <td> 140mm </td></tr>'
    bikedata += '<tr><td>Bronson</td> <td> 160mm </td> <td> 150mm </td></tr>'
    bikedata += '<tr><td>5010</td> <td> 130mm </td> <td> 130mm </td></tr>'
    bikedata += '</tbody></table>'
    return bikedata

# Function to close body and html close
def heading_close():
    heading_close_html = '<!-- Closing of HTML webpage from closing of body -->'
    heading_close_html = '</body>'
    heading_close_html += '</html>'
    return heading_close_html
    
app.run(host='0.0.0.0', port= 8080)
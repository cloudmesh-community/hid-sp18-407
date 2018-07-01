#! /usr/bin/env python
import subprocess
import sys
import os
import os.path
import yaml
import textwrap
import io
from contextlib import redirect_stdout

def lprint(l):
    print ('\n'.join(l))
    
def SECTION(name, msg="", c="="):
    output = []
    output.append("\n")
    output.append(80* c)
    output.append(name + " " + msg)
    output.append(80* c)
    return output

def SUBSECTION(name, msg):
    r = SECTION(name, msg, c='-')
    return r
    
def readme(filename):
    try:
        with open(filename, 'r') as f:
            content = yaml.load(f)
    except Exception as e:
        print (e)
        content = None
    return content
        
def execute(command):
    output=subprocess.check_output(command, stderr=sys.stdout, shell=True).decode("utf-8").splitlines()
    return output


def shell(command):
    try:
        output = subprocess.check_output(
            "{command}; exit 0".format(command=command),
            stderr=subprocess.STDOUT,
            shell=True)
        #output = subprocess.check_output(command, shell=True, stderr=sys.stdout)
        lines = output.decode("utf-8").splitlines()
    except Exception as e:
        lines = str(e)

    return lines

# print (execute("ls | fgrep Makefile"))

def banner(msg=""):
    name = sys._getframe(1).f_code.co_name
    r = SUBSECTION(name.strip(), msg)
    return r

def wordcount(content, owner):
    lprint(banner())

    wc = [0,0,0]
    try:
        wc[0] = execute('wc -w ' + content)[0].strip().split()[0]
    except:
        pass
    try:
        wc[1] = execute('ps2ascii report.pdf | wc -w')[0].strip()
    except:
        pass
    try:
        wc[2] = execute('wc -w report.bib')[0].strip().split()[0]
    except:
        pass


    try:
        r = execute("mdls -name kMDItemNumberOfPages report.pdf")
        pages = r[0].split("=")[1].strip()
    except Exception as e:
        print (e)
        pages = 0

    print ('wc', owner['hid'], owner['kind'], pages, wc[0], content)
    print ('wc', owner['hid'], owner['kind'], pages, wc[1], 'report.pdf')
    print ('wc', owner['hid'], owner['kind'], pages, wc[2], 'report.bib')
    print ()

def print_numbered_line(counter, line):
    prefix = str(counter) +": "     
    wrapper = textwrap.TextWrapper(initial_indent=prefix, width=70,
                                    subsequent_indent=' '*len(prefix))
    print(wrapper.fill(line.strip()))

def numbered_line(counter, line):
    prefix = str(counter) +": "     
    wrapper = textwrap.TextWrapper(initial_indent=prefix, width=70,
                                    subsequent_indent=' '*len(prefix))
    t = wrapper.fill(line.strip())

    return t
    
def print_numbered_line_nostrip(counter, line):
    prefix = str(counter) +": "     
    wrapper = textwrap.TextWrapper(initial_indent=prefix, width=70,
                                    subsequent_indent=' '*len(prefix))
    print (wrapper.fill(line))

    

    
def find(filename, c, erroron=True, tip=None):
    output = banner(c)

    if tip is not None:
        output.append("\n")
        output.append(tip)
        output.append("\n")
        
    counter = 1
    found = False
    try:
        with open(filename, "r") as f:
            for line in f:
                counter += 1
                if c in line:
                    found = True
                    prefix = str(counter) +": " 
                    wrapper = textwrap.TextWrapper(initial_indent=prefix, width=70,
                                subsequent_indent=' '*len(prefix))
                    output.append(wrapper.fill(line.strip()))
    except:
        print ("ERROR reading", filename)
        return found, None
    output.append("passed: " + str(erroron != found))
    return found, output

def floats(filename):
    lprint(banner())
            
    counter = {
        'begin{figure}' : 0,
        'begin{table}' : 0,
        'includegraphics' : 0,
        'label{' : 0,
        'ref{' : 0,
    }
    
    linecounter = 1
    found = False
    with open(filename, 'r') as f:
        content = f.readlines()
        
    for line in content:
        linecounter += 1
        for c in counter:
                
            if c in line:
                counter[c] += 1
                #print (linecounter, ": ", line.strip("\n"), sep="")
                print_numbered_line(linecounter, line)

    # rename
    found = {
        'figures' : counter['begin{figure}'],
        'tables' : counter['begin{table}'],
        'includegraphics' : counter['includegraphics'],
        'labels' : counter['label{'],
        'refs': counter['ref{']
    }
    found['floats']=found['figures'] + found['tables']

    print()
    for entry in found:
        print (entry, found[entry])
    print()
    
    print (found['figures'] + found['tables'] >= found['refs'], ': ref check passed: (refs >= figures + tables)')
    print (found['figures'] + found['tables'] >= found['labels'], ': label check passed: (refs >= figures + tables)')
    print (found['figures'] >= found['includegraphics'], ': include graphics passed: (figures >= includegraphics)')
    print (found['refs'] >= found['labels'], ': check if all figures are refered to: (refs >= labels)')

    print()
    print('Label/ref check')
    linecounter = 0
    top = max(found['figures'],found['tables'], found['includegraphics'])
    passing = True
    for line in content:
        linecounter += 1
        for i in range(1,top+1):
            if "igure {i}".format(i=i) in line:
                print_numbered_line(linecounter, line)
                # print (linecounter, ": ", line, sep='')
                passing = False
            if "able {i}".format(i=i) in line:
                print_numbered_line(linecounter, line)                
                # print (linecounter, ": ", line, sep='')
                passing = False
    if passing:
            msg = ''
    else:
        msg = '-> labels or refs used wrong'
    print('passed:', passing, msg)

    print()
    print("When using figures use columnwidth")
    print("[width=1.0\columnwidth]")
    print("do not cahnge the number to a smaller fraction")
    print()
    
    find(filename, 'textwidth')
    
def below_check(filename):

    failed = False
    
    b = banner()

    def emphasize(word):
        return "**" + word + "**"
    
    def test(word1, word2, line, linecounter, failed):
        output = []

        if word1 in line and word2 in line.lower():
            failed = True
            output.append("WARNING: {word1} and {word2} may be used improperly".format(word1=word1, word2=word2))

            #output = str(line)
            #output.replace(word1, word1)
            #output.replace(word2, word2)

            l = numbered_line(linecounter, line)
            output.append(l)
        return output
    
    linecounter = 1

    with open(filename, 'r') as f:
        content = f.readlines()

    output = [] 
    for line in content:
        linecounter += 1
        
        output += test("table", "below", line, linecounter, failed)
        output += test("table", "above", line, linecounter, failed)
        output += test("figure", "below", line, linecounter, failed)
        output += test("figure", "above", line, linecounter, failed)
        output += test("code", "below", line, linecounter, failed)
        output += test("code", "above", line, linecounter, failed)
        output += test("algorithm", "below", line, linecounter, failed)
        output += test("algorithm", "above", line, linecounter, failed)

    #if failed:
    if len(output) >=1:
        lprint (b)
        lprint(output)

        
#ok    
def yamlcheck(filename):
    r = shell('yamllint ../README.yml')
    if len(r) >=1:
        lprint(banner())
        lprint (r)

def bibtex(filename):
    lprint(banner())
    print()
    print ('label errors')
    print()
    try:
        with open("{filename}.bib".format(filename=filename), 'r') as f:
            content = f.readlines()
    except:
        print ("ERROR reading report.bib")
        return
    counter = 0
    for line in content:
        counter += 1
        if line.strip().startswith("@"):
            if '@String' in line or '@Comment' in line:
                continue
            if not ',' in line:
                print (counter, ": you forgot the , after a bibtex label ")
                return
            label = line.split("{")[1].strip()[:-1]
            if '_' in label:
                print (counter, ": ", label, ": do not use underscore in labels:", sep = '')
            if ' ' in label:
                print (counter, ": ", label, ": do not use ' ' (spaces) in labels:", sep='')
    print()
    print('bibtex errors')
    print()
    output = shell('bibtex {filename}'.format(filename=filename))
    #print (output)
    print ('\n'.join(output))

# ok
def bibtex_empty_fields(filename):
    b = banner()
    failed, output = find(filename + ".bib", '""',
                         tip='entries in general should not be empty in bibtex')
    if failed:
        print(banner)
        lprint (output)

#ok
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# ok
def ascii(filename):
    output = banner()
    with open("{filename}".format(filename=filename), 'r') as f:
        content = f.readlines()
    # print (ord('"'))
    counter = 0
    failed = False
    for line in content:
        counter += 1
        for c in line:
            if not is_ascii(c):
                failed = True
                output.append("non ascii found {c}".format(ord(c)))
    if failed:
        lprint (output)

if os.path.isfile('content.tex'):
    filename = 'content.tex'
else:
    filename = 'report.tex'

data = readme('../README.yml')
kind = os.path.basename(os.getcwd())
    
data['owner']['kind'] = kind


r = SECTION('Compliance Report')
lprint (r)
print()
print('name:', data['owner']['name'])
print('hid: ', data['owner']['hid'])

try:
    print('paper1:', data['paper1']['status'])
except:
    pass

try:
    print('paper2:', data['paper2']['status'])
except:
    pass

try:
    print('project:', data['project']['status'])
except:
    pass


yamlcheck('../README.yml')    

wordcount(filename, data['owner'])
find(filename, '"')
find(filename, 'footnote')
find("report.tex", "input{format/i523}", erroron=False)
floats(filename)
below_check(filename)
bibtex('report')
bibtex_empty_fields('report')                
ascii(filename)

# SECTION("The following tests are optional")


with io.StringIO() as buf, redirect_stdout(buf):
    if not find(filename, 'newline', tip="Tip: newlines can often be replaced just by an empty line"):
        output = buf.getvalue()
        print (output)

with io.StringIO() as buf, redirect_stdout(buf):

    if not find(filename, 'cite {', tip="cites should have a space before \cite{} but not before the {"):
        output = buf.getvalue()
        print (output)
        
    

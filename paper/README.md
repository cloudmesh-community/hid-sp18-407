Report format
=============

This directory contains a template that will be used for writing
reports. It is important that you do not modify the template so all
students have the same format template.

To make it simple we split the content and the format into two
different files.

The content is in 

    content.tex 
    
which you may edit, The template is in

    report.tex

which you are not allowed to edit.

Make sure you run 

    make check
    
which provides a conveneient way to check your latex code. Naturally you 
need to have the full version of LaTeX whcih includes chktex which 
make check calls.

Compiling the report
--------------------

We included a simple Makefile in the directory and if you have LaTeX
properly installed you can use it from commandline to create the
report.pdf:

    make

Please remember that you MUST NOT commit the report.pdf file to the
reporsitory. If we detect thsi we will remove it and do not review
your paper. This is to avoid that students submit papers that actually
do not compile in LaTeX. Make sure you paper always compiles.

This will also generate a simple check on some common issues. The 
log file is located in 

    report-latex.log
    
After the compilation is over.

    
Adding your own packages
------------------------

If you need to add additional usepackages, you need to ask for
approval first. You may not modify the color of hyperlinks or place
the figures in the text. But otherwise there will most likely be no
conflicts. To avoid any issue, check it first and ask for final
approval.



.PHONY: book images

FILE=abstract
#FLAGS=-interaction nonstopmode -halt-on-error -file-line-error
#FLAGS=-interaction nonstopmode  -file-line-error
FLAGS=-shell-escape
CLOUD=cloud
FLAGS=-shell-escape -output-directory=dest -aux-directory=dest


DEFAULT=$(CLOUD)

LATEX=pdflatex

#LATEX=pdfflatex
#LATEX=pydflatex -k




pdflatex:
	pdflatex abstract
	biber abstract
	pdflatex abstract
	pdflatex abstract

all: dest
	latexmk -jobname=$(FILE) $(FLAGS) -pvc -view=pdf $(FILE)

clean:
	rm -f	*.pdf *.bbl *.log *.blg *.aux *.out *.idx *.run.xml *.bcf *.toc
	rm -rf dest

dest:
	mkdir dest

view:
	open abstract.pdf

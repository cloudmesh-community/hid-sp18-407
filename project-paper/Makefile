FILE=report
FLAGS=-interaction nonstopmode -halt-on-error -file-line-error 
REVIEW=review
DEFAULT=$(FILE)
LATEX=pdflatex
BIBTEX=bibtex

SAMPLE=../../hid-sample

UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
OPEN=open
endif
ifeq ($(UNAME), Linux)
OPEN=xdg-open
endif


#make -f Makefile bibtex > report-latex.log 2>&1 || true
#	@echo  >> report-latex.log 2>&1
#	@echo "latex report" >> report-latex.log 2>&1
#	@echo "===========================================" >> report-latex.log 2>&1
#	@echo >> report-latex.log 2>&1
#>> report-latex.log 2>&1
#	make -f Makefile check >> report-latex.log 2>&1


all: prepare
	make -f Makefile generate

generate: clean iureport check
	$(LATEX) ${FLAGS} ${FILE}
	$(BIBTEX) ${FILE}
	$(LATEX) ${FLAGS} ${FILE}
	$(LATEX) ${FLAGS} ${FILE}

prepare:
	cd ../../hid-sample; git pull
	cp ../../hid-sample/paper/Makefile .

iureport:
	cp $(SAMPLE)/tex/format/iureport.cls .
	cp $(SAMPLE)/tex/format/ACM-Reference-Format.bst .

check: prepare
	@$(SAMPLE)/bin/check-quotes.py content.tex
	@chktex -q -n 13 -n 8 content.tex

check-ta:
	@python $(SAMPLE)/paper/check.py 

bibtex:
	@echo 
	@echo "bibtext report" 
	@echo "===========================================" 
	@echo 
	@bibtex $(FILE)
	@echo 
	@echo "bibtext _ label error" 
	@echo "===========================================" 
	@echo 
	@grep -nr "@" report.bib |fgrep _ | awk -F',' '{print $1}' |  sort -u 
	@echo
	@echo "bibtext space label error"
	@echo "===========================================" 
	@echo
	@grep -nr "@" report.bib |fgrep " " | awk -F',' '{print $1}' | fgrep -v "url" | fgrep -v "@String" | fgrep -v "@Comment"|  sort -u
	@echo
	@echo "bibtext comma label error"
	@echo "===========================================" 
	@echo
	@grep -nr "@" report.bib | fgrep -v "@String" | fgrep -v "@Comment"| fgrep -v ',' | sort -u 

footnote-error:	
	@echo ""
	@echo "footnote error"
	@echo "====================="
	@echo ""
	@grep  -nr 'footnote' report.tex |sort -u || true

wordcount-report:
	@echo ""
	@echo "wordcount report"
	@echo "====================="
	@echo ""
	@wc -w report.tex || true
	@echo '   ' $(shell ps2ascii report.pdf | wc -w) 'report.pdf'
	@wc -w report.bib || true

quote-error:
	@echo ""
	@echo "latex quote error"
	@echo "====================="
	@echo ""
	@grep  -nr '"' report.tex |sort -u || true

yaml-error:
	@echo
	@echo "yaml error"
	@echo "====================="
	@echo
	@yamllint ../README.yml || true

format-check:
	@echo 
	@echo "format check"
	@echo "===========================================" 
	@echo
	@echo "if input/i523 is found it is correct (1=ok 0=wrong):"
	@grep -nr "format/i523" report.tex |wc -l || true

figure-check:
	@echo 
	@echo "figure check"
	@echo "===========================================" 
	@echo 
	@echo "Number of figures:"
	@grep -nr "begin{figure" report.tex  |wc -l
	@echo "Number of Tables:"
	@grep -nr "begin{table" report.tex  |wc -l
	@echo "Number of label:"
	@grep -nr "label{" report.tex  |wc -l
	@echo "Number of ref:"
	@grep -nr "ref{" report.tex  |wc -l
	@grep -nr "igure 1" report.tex || true
	@grep -nr "igure 2" report.tex || true
	@fgrep -nr  "igure 3" report.tex || true 
	@grep -nr "igure 4" report.tex  ||true
	@grep -nr "able 1" report.tex ||true
	@grep -nr "able 2" report.tex ||true
	@grep -nr "able 3" report.tex ||true
	@grep -nr "able 4" report.tex ||true

none-ascii:
	@echo 
	@echo "non ascii check report.tex"
	@echo "===========================================" 
	@echo ""
	@echo "this check is not perfect"
	@echo ""
	@perl -ane '{ if(m/[[:^ascii:]]/) { print  } }' report.tex || true
	@echo 
	@echo "non ascii check report.bib"
	@echo "===========================================" 
	@echo ""
	@echo "this check is not perfect"
	@echo ""
	@perl -ane '{ if(m/[[:^ascii:]]/) { print  } }' report.bib || true

# @grep -n -P "[^|a-zA-Z\{\}\s%\./\-:;,0-9@=\\\\\"'\(\)_~\$\!&\`\?+#\^<>\[\]\*]" report.tex || true
# @grep -n -P "[^|a-zA-Z\{\}\s%\./\-:;,0-9@=\\\\\"'\(\)_~\$\!&\`\?+#\^<>\[\]\*]" report.bib || true

#@echo
#./check-yaml.py

#review-create:
#	cp -i report.tex review.tex
#	make -f Makefile review-fetch


insert:
	rm  -f bibtex-error.tex
	@echo '\\section{Bibtex Issues}' > bibtex-error.tex
	bibtex -terse ${REVIEW} | sed -e 's/^/\\todo[inline]{/'  | sed -e 's/.*/&}/'  >> bibtex-error.tex
	sed 's/^\\end{document}/\\input{bibtex-error}\\input{issues}\\end{document}/g' < ${REVIEW}.tex > tmp.tex
	mv tmp.tex ${REVIEW}.tex
	tail ${REVIEW}.tex

#review-fetch:
#	wget -q https://raw.githubusercontent.com/bigdata-i523/sample-hid000/master/paper1/issues.tex

review:
	rm -rf ~/tmp-review
	mkdir -p ~/tmp-review
	cp -r * ~/tmp-review
	cp report.tex ~/tmp-review/review.tex
	cd ~/tmp-review; make -f Makefile insert
	cd ~/tmp-review; make -f Makefile review-pdf
	cp ~/tmp-review/review.pdf review-local.pdf
	open ${REVIEW}-local.pdf
	rm -rf ~/tmp-review

review-pdf:
	$(PDFLATEX) ${FLAGS} ${REVIEW}
	bibtex ${REVIEW}
	make -f Makefile insert
	$(PDFLATEX) ${FLAGS} ${REVIEW}
	bibtex ${REVIEW}
	$(PDFLATEX) ${FLAGS} ${REVIEW}
	$(PDFLATEX) ${FLAGS} ${REVIEW}
	bibtex -terse ${REVIEW} | sed -e 's/^/\* [ ] /' 

pack:
	rm -rf ${FILE}
	mkdir ${FILE}
	mkdir ${FILE}/tex
	mkdir ${FILE}/images
	cp ${FILE}.tex ${FILE}
	cp ${FILE}.bib ${FILE}
	cp ${FILE}.pdf ${FILE}
	cp tex/sig-alternate-2013.cls ${FILE}/tex
	cp -r images/*.pdf ${FILE}/images
	tar cvf ${FILE}.tar ${FILE}

clean:
	rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.pdf *.toc *.fdb_latexmk *.fls *.fff *.lof *.lot *.ttt *.cut
	rm -rf _region_.*
	rm -f iureport.cls
	rm -f ACM-Reference-Format.bst


view:
	$(OPEN) ${FILE}.pdf

# all dependce tracking taking care of by Latexmk
fast:
	latexmk -pdf ${FILE}

watch:
	latexmk -pvc -view=pdf ${FILE}

.PHONY: all clean view fast watch

pull:
	git pull

up:
	git commit -a
	git push

#publish:
#	@echo "==============================================================="
#	@echo "publish ${FILE}.pdf -> http://cyberaide.github.io/papers/${FILE}.pdf" 
#	@echo "==============================================================="
#	cp ${FILE}.pdf /tmp
#	cd ..; git checkout gh-pages
#	cp /tmp/${FILE}.pdf .
#	git add ${FILE}.pdf
#	git commit -m "adding new version of ${FILE}.pdf" ${FILE}.pdf
#	git push
#	cd bigdata
#	git checkout master


bib-extract:
	echo "EXTRACTING ALL USED CITATIONS INTO A BIB FILE"
	bibtool -x ${FILE}.aux -o ${FILE}.bib

skim:
	echo $(DEFAULT)
	open -a /Applications/skim.app $(DEFAULT).pdf

doc:
	make
	mv report.pdf ../paper-instructions.pdf

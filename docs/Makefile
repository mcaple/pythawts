# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

#.PHONY: gh
gh:
	make html
	@echo 'We will create html in the gh-pages branch'
	git checkout gh-pages
	cd ..;	pwd; cp -a ./docs/build/html/. ./docs/html/.
	cd ..; git commit -a -m "Updated html gh-pages"
	git push origin
	git checkout main


#.PHONY: github
#.ONESHELL:
#github:
#	rm -rf /tmp/gh-pages
#	cp -r $(BUILDDIR)/html /tmp/gh-pages
#	git checkout gh-pages
#	cd .. && rm -rf * && cp -r /tmp/gh-pages/* ./ && rm -rf /tmp/gh-pages && git add . && git commit -m "Updated gh-pages" && git push && git checkout master

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

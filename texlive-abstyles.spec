# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/abstyles
# catalog-date 2008-11-26 23:58:56 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-abstyles
Version:	20081126
Release:	2
Summary:	Adaptable BibTeX styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/abstyles
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstyles.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstyles.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A family of modifications of the standard BibTeX styles whose
behaviour may be changed by changing the user document, without
change to the styles themselves. The package is largely used
nowadays in its adaptation for working with Babel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/abstyles/acompat.bib
%{_texmfdistdir}/bibtex/bib/abstyles/jourabbr.bib
%{_texmfdistdir}/bibtex/bib/abstyles/jourfull.bib
%{_texmfdistdir}/bibtex/bst/abstyles/aabbrv.bst
%{_texmfdistdir}/bibtex/bst/abstyles/aalpha.bst
%{_texmfdistdir}/bibtex/bst/abstyles/anotit.bst
%{_texmfdistdir}/bibtex/bst/abstyles/aplain.bst
%{_texmfdistdir}/bibtex/bst/abstyles/aunsnot.bst
%{_texmfdistdir}/bibtex/bst/abstyles/aunsrt.bst
%{_texmfdistdir}/tex/generic/abstyles/apreambl.tex
%doc %{_texmfdistdir}/doc/bibtex/abstyles/README
%doc %{_texmfdistdir}/doc/bibtex/abstyles/a4c.sty
%doc %{_texmfdistdir}/doc/bibtex/abstyles/a4c.tex
%doc %{_texmfdistdir}/doc/bibtex/abstyles/abstdok.pdf
%doc %{_texmfdistdir}/doc/bibtex/abstyles/abstdok.tex
%doc %{_texmfdistdir}/doc/bibtex/abstyles/apreambl.doc
%doc %{_texmfdistdir}/doc/bibtex/abstyles/btxabst.doc
%doc %{_texmfdistdir}/doc/bibtex/abstyles/docmac.doc
%doc %{_texmfdistdir}/doc/bibtex/abstyles/docmac.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}

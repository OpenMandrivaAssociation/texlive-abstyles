Name:		texlive-abstyles
Version:	20081126
Release:	1
Summary:	Adaptable BibTeX styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive//biblio/bibtex/contrib/abstyles
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstyles.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstyles.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A family of modifications of the standard BibTeX styles whose
behaviour may be changed by changing the user document, without
change to the styles themselves. The package is largely used
nowadays in its adaptation for working with Babel.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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

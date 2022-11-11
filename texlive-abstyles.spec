Name:		texlive-abstyles
Version:	15878
Release:	1
Summary:	Adaptable BibTeX styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/abstyles
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstyles.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abstyles.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bib/abstyles
%{_texmfdistdir}/bibtex/bst/abstyles
%{_texmfdistdir}/tex/generic/abstyles
%doc %{_texmfdistdir}/doc/bibtex/abstyles

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}

Name:		texlive-hep-float
Version:	67632
Release:	1
Summary:	Convenience package for float placement
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep-float
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-float.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-float.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-float.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hep-float package redefines some LaTeX float placement
defaults and defines convenience wrappers for floats. The
package is loaded with \usepackage{hep-float}.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hep-float
%{_texmfdistdir}/tex/latex/hep-float
%doc %{_texmfdistdir}/doc/latex/hep-float

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

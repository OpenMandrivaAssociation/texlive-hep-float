%global tl_name hep-float
%global tl_revision 76220

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Convenience package for float placement
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep-float
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-float.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-float.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-float.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The hep-float package redefines some LaTeX float placement defaults and
defines convenience wrappers for floats. The package is loaded with
\usepackage{hep-float}.


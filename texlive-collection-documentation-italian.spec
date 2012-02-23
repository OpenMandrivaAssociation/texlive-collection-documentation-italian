# revision 25218
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-italian
Version:	20120223
Release:	1
Summary:	Italian documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-italian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-amsldoc-it
Requires:	texlive-amsmath-it
Requires:	texlive-amsthdoc-it
Requires:	texlive-fancyhdr-it
Requires:	texlive-l2tabu-italian
Requires:	texlive-latex4wp-it
Requires:	texlive-lshort-italian
Requires:	texlive-psfrag-italian
Requires:	texlive-texlive-it
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-italian package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install

%define		module	shippinglabel
Summary:	Utilities for handling packages
Summary(pl.UTF-8):	Narzędzia do obsługi pakietów
Name:		python3-%{module}
Version:	2.3.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/shippinglabel/
Source0:	https://files.pythonhosted.org/packages/source/s/shippinglabel/%{module}-%{version}.tar.gz
# Source0-md5:	b9e5e336c47603efedea0b0127629f6b
URL:		https://pypi.org/project/shippinglabel/
BuildRequires:	python3-build
BuildRequires:	python3-hatch-requirements-txt
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for handling packages.

%description -l pl.UTF-8
Narzędzia do obsługi pakietów.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info

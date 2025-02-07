%define		module	shippinglabel
Summary:	Utilities for handling packages
Name:		python3-%{module}
Version:	2.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	c36a13a772708c18603e783bfd3a2c10
URL:		https://pypi.org/project/shippinglabel/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for handling packages.

%prep
%setup -q -n %{module}-%{version}

sed -i -e 's#<=67.1.0,##g' pyproject.toml

%build
%{__python3} -m build --wheel --no-isolation --outdir build-3

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} -m installer --destdir=$RPM_BUILD_ROOT build-3/*.whl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info

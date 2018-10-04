#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-rerunfailures
Version  : 4.2
Release  : 2
URL      : https://files.pythonhosted.org/packages/ff/36/8377e8a8520f0beb56ecd629628b1bf2760a06110703b1e3c27e9ded0b01/pytest-rerunfailures-4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/36/8377e8a8520f0beb56ecd629628b1bf2760a06110703b1e3c27e9ded0b01/pytest-rerunfailures-4.2.tar.gz
Summary  : pytest plugin to re-run tests to eliminate flaky failures
Group    : Development/Tools
License  : MPL-2.0
Requires: pytest-rerunfailures-python3
Requires: pytest-rerunfailures-license
Requires: pytest-rerunfailures-python
Requires: pytest
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
====================

%package license
Summary: license components for the pytest-rerunfailures package.
Group: Default

%description license
license components for the pytest-rerunfailures package.


%package python
Summary: python components for the pytest-rerunfailures package.
Group: Default
Requires: pytest-rerunfailures-python3 = %{version}-%{release}

%description python
python components for the pytest-rerunfailures package.


%package python3
Summary: python3 components for the pytest-rerunfailures package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest-rerunfailures package.


%prep
%setup -q -n pytest-rerunfailures-4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538660976
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pytest-rerunfailures
cp LICENSE %{buildroot}/usr/share/doc/pytest-rerunfailures/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/pytest-rerunfailures/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

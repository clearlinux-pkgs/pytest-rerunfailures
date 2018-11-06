#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-rerunfailures
Version  : 5.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/1a/47/8b22683e1622de92cbfed26361eec62f33a493c411704930232aa8298ec1/pytest-rerunfailures-5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1a/47/8b22683e1622de92cbfed26361eec62f33a493c411704930232aa8298ec1/pytest-rerunfailures-5.0.tar.gz
Summary  : pytest plugin to re-run tests to eliminate flaky failures
Group    : Development/Tools
License  : MPL-2.0
Requires: pytest-rerunfailures-license = %{version}-%{release}
Requires: pytest-rerunfailures-python = %{version}-%{release}
Requires: pytest-rerunfailures-python3 = %{version}-%{release}
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
%setup -q -n pytest-rerunfailures-5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541512690
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-rerunfailures
cp LICENSE %{buildroot}/usr/share/package-licenses/pytest-rerunfailures/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-rerunfailures/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

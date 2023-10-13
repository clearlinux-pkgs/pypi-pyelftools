#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pyelftools
Version  : 0.30
Release  : 35
URL      : https://files.pythonhosted.org/packages/84/05/fd41cd647de044d1ffec90ce5aaae935126ac217f8ecb302186655284fc8/pyelftools-0.30.tar.gz
Source0  : https://files.pythonhosted.org/packages/84/05/fd41cd647de044d1ffec90ce5aaae935126ac217f8ecb302186655284fc8/pyelftools-0.30.tar.gz
Summary  : Library for analyzing ELF files and DWARF debugging information
Group    : Development/Tools
License  : Unlicense
Requires: pypi-pyelftools-bin = %{version}-%{release}
Requires: pypi-pyelftools-license = %{version}-%{release}
Requires: pypi-pyelftools-python = %{version}-%{release}
Requires: pypi-pyelftools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==========
pyelftools
==========
.. image:: https://github.com/eliben/pyelftools/workflows/pyelftools-tests/badge.svg
:align: center
:target: https://github.com/eliben/pyelftools/actions

%package bin
Summary: bin components for the pypi-pyelftools package.
Group: Binaries
Requires: pypi-pyelftools-license = %{version}-%{release}

%description bin
bin components for the pypi-pyelftools package.


%package license
Summary: license components for the pypi-pyelftools package.
Group: Default

%description license
license components for the pypi-pyelftools package.


%package python
Summary: python components for the pypi-pyelftools package.
Group: Default
Requires: pypi-pyelftools-python3 = %{version}-%{release}

%description python
python components for the pypi-pyelftools package.


%package python3
Summary: python3 components for the pypi-pyelftools package.
Group: Default
Requires: python3-core
Provides: pypi(pyelftools)

%description python3
python3 components for the pypi-pyelftools package.


%prep
%setup -q -n pyelftools-0.30
cd %{_builddir}/pyelftools-0.30
pushd ..
cp -a pyelftools-0.30 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694100853
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyelftools
cp %{_builddir}/pyelftools-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyelftools/29a06f5b461ea380819c2914ac77ebcc6069a79b || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/readelf.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyelftools/29a06f5b461ea380819c2914ac77ebcc6069a79b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

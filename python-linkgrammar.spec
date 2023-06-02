Summary:	Python 2 binding for link-grammar library
Summary(pl.UTF-8):	Wiązanie Pythona 2 do biblioteki link-grammar
Name:		python-linkgrammar
Version:	5.7.0
Release:	1
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	http://www.nl.abisource.com/downloads/link-grammar/%{version}/link-grammar-%{version}.tar.gz
# Source0-md5:	69c51be8cba7a23bbea5b80e41b51891
Patch0:		link-grammar-modules.patch
Patch1:		%{name}-system-lib.patch
URL:		http://www.link.cs.cmu.edu/link/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gcc >= 6:4.7
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	link-grammar-devel >= 5.7.0
BuildRequires:	pcre2-8-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sqlite3-devel >= 3.0.0
BuildRequires:	swig-python >= 2.0.0
Requires:	link-grammar >= 5.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 binding for link-grammar library.

%description -l pl.UTF-8
Wiązanie Pythona 2 do biblioteki link-grammar.

%prep
%setup -q -n link-grammar-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-aspell \
	--disable-binreloc \
	--disable-editline \
	--disable-hunspell \
	--disable-java-bindings \
	--enable-python-bindings=2 \
	--disable-silent-rules

%{__make} -C bindings/python \
	python2dir=%{py_sitedir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C bindings/python install \
	DESTDIR=$RPM_BUILD_ROOT \
	python2dir=%{py_sitedir}

%{__rm}	$RPM_BUILD_ROOT%{py_sitedir}/linkgrammar/_clinkgrammar.la \
	$RPM_BUILD_ROOT%{py_sitedir}/linkgrammar/_clinkgrammar.a

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/linkgrammar
%attr(755,root,root) %{py_sitedir}/linkgrammar/_clinkgrammar.so
%{py_sitedir}/linkgrammar/*.py[co]

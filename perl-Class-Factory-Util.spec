#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Factory-Util
Summary:	Class::Factory::Util - provide utility methods for factory classes
Summary(pl):	Class::Factory::Util - dostarczanie metod narzêdziowych dla klas przemys³owych
Name:		perl-Class-Factory-Util
Version:	1.6
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	88b4471f9c22abcc1192f87be013cc18
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports a method that is useful for factory classes.

%description -l pl
Ten modu³ eksportuje metodê, która mo¿e byæ przydatna dla klas
przemys³owych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Class/Factory
%{perl_vendorlib}/Class/Factory/*.pm
%{_mandir}/man3/*

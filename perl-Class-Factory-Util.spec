#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Factory-Util
Summary:	Class::Factory::Util - provide utility methods for factory classes
Summary(pl.UTF-8):	Class::Factory::Util - dostarczanie metod narzędziowych dla klas przemysłowych
Name:		perl-Class-Factory-Util
Version:	1.7
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aebd79da361b676a7ecd3245fc3d1b3f
URL:		http://search.cpan.org/dist/Class-Factory-Util/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports a method that is useful for factory classes.

%description -l pl.UTF-8
Ten moduł eksportuje metodę, która może być przydatna dla klas
przemysłowych.

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

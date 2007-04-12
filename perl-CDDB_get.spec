%define	module	CDDB_get
%define name	perl-%{module}
%define version 2.23
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Read the CDDB entry for an audio CD in your drive	
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/CDDB_get/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module/script gets the CDDB info for an audio cd.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/cddb.pl
%{perl_vendorlib}/auto/CDDB_get
%{perl_vendorlib}/CDDB_get.pm
%{perl_vendorlib}/cddb.pl
%{_mandir}/*/*




%define	upstream_name	 CDDB_get
%define upstream_version 2.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Read the CDDB entry for an audio CD in your drive	
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CDDB_get/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module/script gets the CDDB info for an audio cd.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/cddb.pl
%{perl_vendorlib}/auto/CDDB_*
%{perl_vendorlib}/CDDB_*.pm
%{perl_vendorlib}/cddb.pl
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.270.0-2mdv2011.0
+ Revision: 680661
- mass rebuild

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.270.0-1mdv2011.0
+ Revision: 395035
- update to 2.27
- using %%perl_convert_version
- fixed license field

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.23-5mdv2009.0
+ Revision: 255611
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.23-3mdv2008.1
+ Revision: 131261
- kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.23-3mdv2007.0
+ Revision: 73346
- import perl-CDDB_get-2.23-3mdv2007.0

* Sat Jun 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.23-3mdv2007.0
- spec cleanup
- %%{1}mdv2007.1

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 2.23-2mdk
- rebuild

* Tue Jun 01 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.23-1mdk
- 2.23
- cosmetics


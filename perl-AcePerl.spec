%define upstream_name AcePerl
%define upstream_version 1.92

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Ace::Browser::LocalSiteDefs\\)'
%else
%define _requires_exceptions perl(Ace::Browser::LocalSiteDefs)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl interface for the ACEDB object-oriented database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Ace/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		%{name}.makefile.patch

BuildRequires:	perl-devel
BuildRequires:	perl(WeakRef)
BuildRequires:	perl(Cache::Cache)

%description
Designed specifically for use in genome sequencing projects, ACEDB
provides powerful modeling and management services for biological and
laboratory data. For others, it is a good open source introduction to
the world of object-oriented databases

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0

perl -pi -e 's|^#!/usr/local/bin/perl$|#!%{__perl}|' examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make COMPILER="gcc %{optflags} -fPIC -DACEDB4"

%install
%makeinstall_std

%check
# tests depends on a remote db to pass...
#make test

%files
%doc README README.ACEBROWSER DISCLAIMER.txt ChangeLog docs examples
%{_bindir}/*
%{perl_vendorarch}/GFF
%{perl_vendorarch}/Ace
%{perl_vendorarch}/Ace.pm
%{perl_vendorarch}/auto/Ace
%{_mandir}/*/*


%changelog
* Sun Feb 12 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1.920.0-5
+ Revision: 773598
- add perl(Cache::Cache) to buildrequires
- don't disable fortify flags
- cosmetics
- skip tests as they depend on a remote db to pass
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Funda Wang <fwang@mandriva.org>
    - mass rebuild
    - mass rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.920.0-2mdv2011.0
+ Revision: 555415
- rebuild

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.920.0-1mdv2010.0
+ Revision: 402089
- rebuild using %%perl_convert_version

* Fri Nov 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.92-1mdv2009.1
+ Revision: 303116
- update to new version 1.92

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.91-4mdv2009.0
+ Revision: 255233
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 1.91-2mdv2008.1
+ Revision: 151801
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Apr 23 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.91-1mdv2008.0
+ Revision: 17415
- New version 1.91


* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.89-6mdv2007.0
+ Revision: 86530
- Import perl-AcePerl

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.89-6mdv2007.0
- Rebuild

* Wed Apr 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.89-5mdk
- Fix BuildRequires using perl Policy

* Wed Apr 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.89-4mdk
- Fix BuildRequires

* Tue Apr 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.89-3mdk
- disable fortify, it breaks va_list use
- better source URL

* Wed Jun 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.89-2mdk 
- don't ship auto dir
- make test

* Tue Apr 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.89-1mdk
- new release
- spec cleanup
- better url
- fix interpreter path in exemples

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 1.87-4mdk
- fix compilation on x86_64

* Mon Nov 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.87-3mdk 
- rebuild for new perl

* Thu Jul 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.87-2mdk 
- rebuild

* Thu Apr 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.87-1mdk
- new version
- rpmbuildupdate aware


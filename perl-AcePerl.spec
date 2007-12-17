%define module	AcePerl
%define name	perl-%{module}
%define version 1.91
%define release %mkrel 1

%define _requires_exceptions perl(Ace::Browser::LocalSiteDefs)
%define _fortify_cflags %nil

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface for the ACEDB object-oriented database
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Ace/%{module}-%{version}.tar.bz2
Patch:		%{name}.makefile.patch
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:  perl(WeakRef)

%description
Designed specifically for use in genome sequencing projects, ACEDB
provides powerful modeling and management services for biological and
laboratory data. For others, it is a good open source introduction to
the world of object-oriented databases

%prep
%setup -q -n %{module}-%{version}
%patch

perl -pi -e 's|^#!/usr/local/bin/perl$|#!%{__perl}|' examples/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%make COMPILER="gcc %{optflags} -fPIC -DACEDB4"

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README README.ACEBROWSER DISCLAIMER.txt ChangeLog docs examples
%{_bindir}/*
%{perl_vendorarch}/GFF
%{perl_vendorarch}/Ace
%{perl_vendorarch}/Ace.pm
%{perl_vendorarch}/auto/Ace
%{_mandir}/*/*



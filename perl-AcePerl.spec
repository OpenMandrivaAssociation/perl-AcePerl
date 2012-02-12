%define upstream_name AcePerl
%define upstream_version 1.92

%define _requires_exceptions perl(Ace::Browser::LocalSiteDefs)

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl interface for the ACEDB object-oriented database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Ace/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		%{name}.makefile.patch

BuildRequires:	perl-devel
BuildRequires:	perl(WeakRef)

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
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
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

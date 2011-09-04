Name:           perl-PPI-HTML
Version:        1.07
Release:        7%{?dist}
Summary:        Generate syntax-highlighted HTML for Perl using PPI

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/PPI-HTML/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/PPI-HTML-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(CSS::Tiny)
BuildRequires:  perl(Params::Util) => 0.05
BuildRequires:  perl(PPI)
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
PPI::HTML converts Perl documents into syntax highlighted HTML pages.


%prep
%setup -q -n PPI-HTML-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{_bindir}/*
%{perl_vendorlib}/PPI/
%{_mandir}/man3/*.3pm*


%changelog
* Tue Feb 16 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.07-7
- make rpmlint happy
- Related: rhbz#543948

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.07-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-3
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-2
- rebuild for new perl

* Sat May 13 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.07-1
- First build.

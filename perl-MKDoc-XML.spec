#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pnam	MKDoc-XML
Summary:	MKDoc::XML - The MKDoc XML Toolkit
Summary(pl.UTF-8):	MKDoc::XML - zestaw narzędzi MKDoc XML
Name:		perl-MKDoc-XML
Version:	0.75
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BP/BPOSTLE/%{pnam}-%{version}.tar.gz
# Source0-md5:	bae96f16d2f55ac01f562d2e101b2824
URL:		http://search.cpan.org/dist/MKDoc-XML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MKDoc::XML - The MKDoc XML Toolkit.

%description -l pl.UTF-8
MKDoc::XML - zestaw narzędzi MKDoc XML.

%prep
%setup -q -n %{pnam}-%{version}

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
%doc Changes README
%dir %{perl_vendorlib}/MKDoc
%{perl_vendorlib}/MKDoc/*.pm
%{perl_vendorlib}/MKDoc/XML
%{_mandir}/man3/*

Summary:	PHP Development Tools framework for the Eclipse platform
Name:		eclipse-pdt
Version:	1.0
Release:	0.1
License:	EPL v1.0
Group:		Development/Tools
#Source0:	-
# Source0-md5:	593b56fce7d1f1f799e87365cafefbef
URL:		http://www.eclipse.org/pdt/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PDT project provides a PHP Development Tools framework for the
Eclipse platform. This project encompasses all development components
necessary to develop PHP and facilitate extensibility. It leverages
the existing Web Tools Project in providing developers with PHP
capabilities.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

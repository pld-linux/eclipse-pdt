# TODO
# - build from source
%define		buildid	R20070917
Summary:	PHP Development Tools framework for the Eclipse platform
Name:		eclipse-pdt
Version:	1.0
Release:	1
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/pdt/downloads/drops/%{buildid}/org.eclipse.php_feature-sdk-%{version}-%{buildid}.zip
# Source0-md5:	a3bcc6128a7fd283b1189b70008a66ae
URL:		http://www.eclipse.org/pdt/
#Requires:	eclipse-dtp >= 1.5
Requires:	eclipse-emf-sdo-xsd >= 2.3.0
Requires:	eclipse-gef >= 3.3
Requires:	eclipse >= 3.3
#Requires:	eclipse-test-framework >= 3.3
Requires:	eclipse-wtp >= 2.0
Requires:	jre >= 1.5
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

%description
The PDT project provides a PHP Development Tools framework for the
Eclipse platform. This project encompasses all development components
necessary to develop PHP and facilitate extensibility. It leverages
the existing Web Tools Project in providing developers with PHP
capabilities.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a eclipse/features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a eclipse/plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/org.eclipse.php*
%{eclipsedir}/plugins/org.eclipse.php*

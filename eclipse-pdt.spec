# TODO
# - build from source
%define		buildid	R20080103
Summary:	PHP Development Tools framework for the Eclipse platform
Summary(pl.UTF-8):	Szkielet narzędzi programistycznych PHP dla platformy Eclipse
Name:		eclipse-pdt
Version:	1.0.2
Release:	1
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/pdt/downloads/drops/%{buildid}/org.eclipse.php_feature-sdk-%{buildid}.zip
# Source0-md5:	b87d5fbdfb5f954190a42a326ad1a2ae
URL:		http://www.eclipse.org/pdt/
#Requires:	eclipse-dtp >= 1.5.1
Requires:	eclipse-emf-sdo-xsd >= 2.3.1
Requires:	eclipse-gef >= 3.3.1
Requires:	eclipse >= 3.3.1.1
#Requires:	eclipse-test-framework >= 3.3.1.1
Requires:	eclipse-wtp >= 2.0.2
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

%description -l pl.UTF-8
Projekt PDT (PHP Development Tools) udostępnia szkielet narzędzi
programistycznych PHP dla platformy Eclipse. Projekt ten obejmuje
wszystkie komponenty potrzebne do tworzenia kodu w PHP i ułatwiające
rozszerzalność. Wpływa na istniejący projekt narzędzi WWW (Web Tools
Project) udostępniając programistom elementy dla PHP.

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

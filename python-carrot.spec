%define module carrot

Name:           python-%{module}
Version:        0.10.7
Release:        2
Url:            http://github.com/ask/carrot/
Summary:        AMQP Messaging Framework for Python
License:        BSD
Group:          Development/Python
Source:         %{module}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-amqplib
Requires:       python-anyjson
BuildArch:      noarch

%description
An AMQP messaging queue framework. AMQP is the Advanced Message
Queuing Protocol, an open standard protocol for message orientation, queuing,
routing, reliability and security.

The aim of carrot is to make messaging in Python as easy as possible by
providing a high-level interface for producing and consuming messages. At the
same time it is a goal to re-use what is already available as much as possible.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changelog README TODO
%{python_sitearch}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.10.7-1mdv2011.0
+ Revision: 683244
- import python-carrot


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.10.7
- first release for Mandriva 


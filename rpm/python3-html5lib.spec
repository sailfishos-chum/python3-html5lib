Name:           python3-html5lib
Summary:        A python based HTML parser/tokenizer
Version:        1.1
Release:        0
Epoch:          1
License:        MIT
URL:            https://github.com/html5lib/html5lib-python
Source:         %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A python based HTML parser/tokenizer based on the WHATWG HTML5 
specification for maximum compatibility with major desktop web browsers.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

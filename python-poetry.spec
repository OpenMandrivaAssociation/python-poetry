Name:		python-poetry
Version:	1.8.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/poetry/poetry-%{version}.tar.gz
Summary:	Python dependency management and packaging made easy.
URL:		https://pypi.org/project/poetry/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildArch:	noarch

%description
Python dependency management and packaging made easy.

%prep
%autosetup -p1 -n poetry-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/poetry
%{py_sitedir}/poetry
%{py_sitedir}/poetry-*.dist-info

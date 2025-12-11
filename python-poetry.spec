Name:		python-poetry
Version:	2.2.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/poetry/poetry-%{version}.tar.gz
Source1000:	%{name}.rpmlintrc
Summary:	Python dependency management and packaging made easy
URL:		https://pypi.org/project/poetry/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(findpython)
BuildRequires:	python%{pyver}dist(pbs-installer)
BuildArch:	noarch

%patchlist

%description
Python dependency management and packaging made easy.

%files
%{_bindir}/poetry
%{py_sitedir}/poetry
%{py_sitedir}/poetry-*.dist-info

%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm_Livesearch
%define		_status		beta
%define		_pearname	HTML_QuickForm_Livesearch

Summary:	%{_pearname} - element for HTML_QuickForm to enable a suggest search
Summary(pl.UTF-8):	%{_pearname} - element HTML_QuickForm pozwalający na dołączenie sugestii do wyszukiwania
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	3
License:	PHP License 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	72069ad6852602f7ba17918afc6abb49
URL:		http://pear.php.net/package/HTML_QuickForm_Livesearch/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core
Requires:	php-pear-HTML_QuickForm > 3.2.4
Requires:	php-pear-HTML_AJAX > 0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package adds an element to the PEAR::HTML_QuickForm package to
dynamically create an HTML input text element that at every keypressed
javascript event, returns a list of options in a dynamic dropdown
select box(live dropdown select).

This element use AJAX (Communication from JavaScript to your browser
without reloading the page).

This type of livesearch is useful when you have a form with a dropdown
list with a large number of row.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dodaje do PEAR::HTML_QuickForm element pozwalający na
dynamicznie tworzenie pola input formularza HTML, który na każde
zdarzenie wciśnięcia klawisza zwraca listę opcji w dynamicznej liście
wyboru (live dropdown select).

Element ten korzysta z technologii AJAX (komunikacja z JavaScript bez
potrzeby przeładowania strony).

Ten tym 'żywego' wyszukiwania jest przydatny w przypadku formularza z
listą wyboru z dużą liczbą pozycji.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm/livesearch_select.php
%dir %{php_pear_dir}/data/HTML_QuickForm_Livesearch
%{php_pear_dir}/data/HTML_QuickForm_Livesearch/live.js

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch

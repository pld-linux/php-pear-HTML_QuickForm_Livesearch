%define		status		beta
%define		pearname	HTML_QuickForm_Livesearch
Summary:	%{pearname} - element for HTML_QuickForm to enable a suggest search
Summary(pl.UTF-8):	%{pearname} - element HTML_QuickForm pozwalający na dołączenie sugestii do wyszukiwania
Name:		php-pear-%{pearname}
Version:	0.4.1
Release:	1
License:	PHP License 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	985fa1324b7b8b60a2db6d45b1e5d9d3
URL:		http://pear.php.net/package/HTML_QuickForm_Livesearch/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-HTML_AJAX > 0.4.1
Requires:	php-pear-HTML_QuickForm > 3.2.4
Requires:	php-pear-PEAR-core
Obsoletes:	php-pear-HTML_QuickForm_Livesearch-tests
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet ten dodaje do PEAR::HTML_QuickForm element pozwalający na
dynamicznie tworzenie pola input formularza HTML, który na każde
zdarzenie wciśnięcia klawisza zwraca listę opcji w dynamicznej liście
wyboru (live dropdown select).

Element ten korzysta z technologii AJAX (komunikacja z JavaScript bez
potrzeby przeładowania strony).

Ten tym 'żywego' wyszukiwania jest przydatny w przypadku formularza z
listą wyboru z dużą liczbą pozycji.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/HTML_QuickForm_Livesearch/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log README
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm/livesearch_select.php
%dir %{php_pear_dir}/data/HTML_QuickForm_Livesearch
%{php_pear_dir}/data/HTML_QuickForm_Livesearch/live.js

%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm_Livesearch
%define		_status		alpha
%define		_pearname	HTML_QuickForm_Livesearch

Summary:	%{_pearname} - element for HTML_QuickForm to enable a suggest search
Summary(pl):	%{_pearname} - element HTML_QuickForm pozwalaj�cy na do��czenie sugestii do wyszukiwania
Name:		php-pear-%{_pearname}
Version:	0.1.5
Release:	1
License:	PHP License 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7d904e58771a70547d9e94f79368f280
URL:		http://pear.php.net/package/HTML_QuickForm_Livesearch/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR
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

%description -l pl
Pakiet ten dodaje do PEAR::HTML_QuickForm element pozwalaj�cy na
dynamicznie tworzenie pola input formularza HTML, kt�ry na ka�de
zdarzenie wci�ni�cia klawisza zwraca list� opcji w dynamicznej li�cie
wyboru (live dropdown select).

Element ten korzysta z technologii AJAX (komunikacja z JavaScript bez
potrzeby prze�adowania strony).

Ten tym '�ywego' wyszukiwania jest przydatny w przypadku formularza z
list� wyboru z du�� liczb� pozycji.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
%{php_pear_dir}/data/HTML_QuickForm_Livesearch/live.js

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch/example/auto_server.php
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch/example/index.php
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch/example/livesearch.class.php
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch/example/live.js
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch/example/style.css
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch/example/shadowAlpha.png
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch/example/shadow.gif
%{php_pear_dir}/tests/HTML_QuickForm_Livesearch/example/myfunction.php

%define		theme	LiquidWeatherPlus

Summary:	superkaramba - LiquidWeatherPlus theme
Summary(pl):	superkaramba - motyw LiquidWeatherPlus
Name:		superkaramba-theme-%{theme}
Version:	13.3
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.message.co.nz/~matt-sarah/lwp-%{version}.skz
# Source0-md5:	0db1cce1abf5fc6a0e44a4723ec6f8c1
Source1:	http://mirrors.borgnet.us/matt-lw/Glossy.tar.bz2
# Source1-md5:	f56593dccd5086a23f6b545c4663325f
Source2:	http://mirrors.borgnet.us/matt-lw/Kapsules.tar.bz2
# Source2-md5:	e7fcffa5f00914117926b963ca80095b
URL:		http://liquidweather.net/
Requires:	ImageMagick
Requires:	python-PyQt >= 3.13
Requires:	python-sip
Requires:	superkaramba >= 0.39
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_liquiddir	/themes/superkaramba/liquid_weather_plus

%description
LiquidWeatherPlus theme for superkaramba. Features:
 - Weather forecasts from weather.com or BBC for most cities worldwide.
 - Details of current conditions.
 - Daily forecasts and weather details for today and the following 4
   days.
 - Hourly forecasts for the next 12 hours, if using weather.com as a
   data source.
 - All sorts of different weather maps for all major world regions,
   including Antarctica.
 - View up to 5 web cams.
 - All data updates automatically every 1, 2 or 3 hours.
 - Multiple background and icon themes.
 - Gui configuration for everything through the configuration menu.

%description -l pl
Motyw LiquidWeatherPlus do superkaramby. Wy¶wietlane informacje:
 - Prognoza pogody z weather.com oraz BBC z wiêkszo¶ci miast ¶wiata.
 - Warunki pogodowe.
 - Zapowied¼ pogody oraz szczególy dla aktualnego dnia oraz nastêpnych
   czterech dni.
 - Przewidywanie pogody dla nastêpnych 12 godzin, je¿eli u¿ywamy
   weather.com jako ¼ród³o danych.
 - Wszystkie rodzaje ró¿nych map pogody dla wszystkich wa¿niejszych
   rejonów, równie¿ Antarktyki.
 - Widok z 5 kamer internetowych.
 - Wszystkie dane uaktualniane s± co 1, 2 lub 3 godziny.
 - Ró¿ne rodzaje t³a oraz motywy ikon.
 - Graficzna konfiguracja przez menu konfiguracyjne.

%package icons-Glossy
Summary:	Glossy icons set for Liquid Weather Plus theme
Summary(pl):	Ikony Glossy dla motywu Liquid Weather Plus
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description icons-Glossy
Glossy icons set for Liquid Weather Plus theme.

%description icons-Glossy -l pl
Ikony Glossy dla motywu Liquid Weather Plus.

%package icons-Kapsules
Summary:	Kapsules icons set for Liquid Weather Plus theme
Summary(pl):	Ikony Kapsules dla motywu Liquid Weather Plus
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description icons-Kapsules
Kapsules icons set for Liquid Weather Plus theme.

%description icons-Kapsules -l pl
Ikony Kapsules dla motywu Liquid Weather Plus.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}%{_liquiddir} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/{Glossy,Kapsules}/{large_icons,small_icons} \

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/lwp.skz

# install Glossy,Kapsules icons
cd  $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons
tar fvxj %{SOURCE1}
tar fvxj %{SOURCE2}
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%dir %{_datadir}%{_liquiddir}
%{_datadir}%{_liquiddir}/lwp.skz
%dir %{_datadir}%{_liquiddir}/icons

%files icons-Glossy
%defattr(644,root,root,755)
%{_datadir}%{_liquiddir}/icons/Glossy

%files icons-Kapsules
%defattr(644,root,root,755)
%{_datadir}%{_liquiddir}/icons/Kapsules

#$Revision: 1.17 $,  $Date: 2005-04-23 07:26:03 $

%define		theme	LiquidWeatherPlus

Summary:	superkaramba - LiquidWeatherPlus theme
Summary(pl):	superkaramba - motyw LiquidWeatherPlus
Name:		superkaramba-theme-%{theme}
Version:	4.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.message.co.nz/~matt-sarah/lwp-%{version}.tar.bz2
# Source0-md5:	ef354fb0ff94a3c8b2ff62ed3653e581
URL:		http://www.message.co.nz/~matt-sarah/
Requires:	superkaramba >= 0.35
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define _liquiddir /themes/superkaramba/liquid_weather_plus
 #directory in rpm
%define _lwp liquid_weather_plus
 #directory in source

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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}%{_liquiddir} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/{background,earthquake,fonts,translations} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/{flat,liquid,um,weather.com}/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/{flat,liquid}/{medium,strong,weak}
install %{_lwp}/*.{html,log,py*,png,theme,txt} $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}
install %{_lwp}/background/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/background
install %{_lwp}/earthquake/*.{html,css} $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/earthquake
install %{_lwp}/fonts/*.ttf $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/fonts
install %{_lwp}/translations/* $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/translations

for www in {flat,liquid,um,weather.com};
 do
install %{_lwp}/icons/$www/large_icons/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/$www/large_icons
install %{_lwp}/icons/$www/small_icons/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/$www/small_icons
done

for www in {medium,strong,weak};
 do
install %{_lwp}/wind_icons/flat/$www/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/flat/$www
install %{_lwp}/wind_icons/liquid/$www/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/liquid/$www
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{_datadir}%{_liquiddir}/

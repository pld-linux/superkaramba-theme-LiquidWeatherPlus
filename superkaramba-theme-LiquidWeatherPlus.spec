#$Revision: 1.10 $,  $Date: 2005-03-05 15:15:35 $

%define		theme	LiquidWeatherPlus

Summary:	superkaramba - LiquidWeatherPlus theme
Summary(pl):	superkaramba - motyw LiquidWeatherPlus
Name:		superkaramba-theme-%{theme}
Version:	3.7
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.message.co.nz/~matt-sarah/lwp-%{version}.tar.bz2
# Source0-md5:	ff1e63e67082f0ea043b4d8c6e10bafc
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
 - Weather forecasts from weather.com or BBC for most cities
   worldwide.
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
Motyw LiquidWeatherPlus do superkaramby. Wy�wietlane informacje:
 - Prognoza pogody z weather.com oraz BBC z wi�kszo�ci miast �wiata.
 - Warunki pogodowe.
 - Zapowied� pogody oraz szczeg�ly dla aktualnego dnia oraz nast�pnych
   czterech dni.
 - Przewidywanie pogody dla nast�pnych 12 godzin, je�eli u�ywamy
   weather.com jako �r�d�o danych.
 - Wszystkie rodzaje r�nych map pogody dla wszystkich wa�niejszych
   rejon�w, r�wnie� Antarktyki.
 - Widok z 5 kamer internetowych.
 - Wszystkie dane uaktualniane s� co 1, 2 lub 3 godziny.
 - R�ne rodzaje t�a oraz motywy ikon.
 - Graficzna konfiguracja przez menu konfiguracyjne.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}%{_liquiddir} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/{background,fonts,translations} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/icons/{flat,liquid,um,weather.com}/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/wind_icons/{flat,liquid}/{medium,strong,weak} 
#clean vim temorary files left by autor
rm %{_lwp}/*~
install %{_lwp}/*.* $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}
install %{_lwp}/fonts/*.ttf $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/fonts
install %{_lwp}/background/*.png $RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/background
install %{_lwp}/translations/* 	$RPM_BUILD_ROOT%{_datadir}%{_liquiddir}/translations

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
#%dir %{_datadir}{_liquiddir}
%{_datadir}%{_liquiddir}/

#$Revision: 1.7 $,  $Date: 2005-02-07 21:08:18 $

%define		theme	LiquidWeatherPlus

Summary:	superkaramba - LiquidWeatherPlus theme
Summary(pl):	superkaramba - motyw LiquidWeatherPlus
Name:		superkaramba-theme-%{theme}
Version:	3.6
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.message.co.nz/~matt-sarah/lwp-%{version}.tar.bz2
# Source0-md5:	f10827e1b03fd4a6ac0a55b7c7519f2c
URL:		http://www.message.co.nz/~matt-sarah/
Requires:	superkaramba >= 0.35
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Motyw LiquidWeatherPlus do superkaramby. Wy¶wietlane informacje:
 - Prognoza pogody z weather.com oraz BBC z wiêkszo¶ci miast ¶wiata.
 - Warunki pogodowe.
 - Zapowied¼ pogody oraz szczególy dla aktualnego dnia oraz nastêpnych
   czterech dni
 - Przewidywanie pogody dla nastêpnych 12 godzin, je¿eli u¿ywamy
   weather.com jako ¼ród³o danych 
 - Wszystkie rodzaje ró¿nych map pogody dla wszystkich wa¿niejszych
   rejonów, równie¿ Antarktyki 
 - Widok z 5 kamer internetowych 
 - Wszystkie dane uaktualniane s± co 1, 2 lub 3 godziny
 - Ró¿ne rodzaje t³a oraz motywy ikon 
 - Graficzna konfiguracja wszystkiego przez menu konfiguracyjne

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/{background,fonts,translations} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/flat/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/liquid/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/um/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/weather.com/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/{medium,weak,strong} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/{medium,weak,strong} \

install liquid_weather_plus/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus
install liquid_weather_plus/background/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/background
install liquid_weather_plus/fonts/*.ttf $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/fonts
install liquid_weather_plus/translations/* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/translations
install liquid_weather_plus/icons/flat/large_icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/flat/large_icons
install liquid_weather_plus/icons/flat/small_icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/flat/small_icons
install liquid_weather_plus/icons/liquid/large_icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/liquid/large_icons
install liquid_weather_plus/icons/liquid/small_icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/liquid/small_icons
install liquid_weather_plus/icons/um/large_icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/um/large_icons
install liquid_weather_plus/icons/um/small_icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/um/small_icons
install liquid_weather_plus/icons/weather.com/large_icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/weather.com/large_icons
install liquid_weather_plus/icons/weather.com/small_icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/weather.com/small_icons
install liquid_weather_plus/wind_icons/flat/medium/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/medium
install liquid_weather_plus/wind_icons/flat/strong/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/strong
install liquid_weather_plus/wind_icons/flat/weak/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/weak
install liquid_weather_plus/wind_icons/liquid/medium/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/medium
install liquid_weather_plus/wind_icons/liquid/strong/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/strong
install liquid_weather_plus/wind_icons/liquid/weak/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/weak

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%dir %{_datadir}/themes/superkaramba/liquid_weather_plus
%{_datadir}/themes/superkaramba/liquid_weather_plus/

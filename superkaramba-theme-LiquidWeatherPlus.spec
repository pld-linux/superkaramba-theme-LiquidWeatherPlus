#$Revision: 1.3 $,  $Date: 2005-01-22 22:02:02 $

%define		theme	LiquidWeatherPlus

Summary:	superkaramba - LiquidWeatherPlus theme
Summary(pl):	superkaramba - motyw LiquidWeatherPlus
Name:		superkaramba-theme-%{theme}
Version:	3.4.4
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.message.co.nz/~matt-sarah/lwp-%{version}.tar.bz2
# Source0-md5: 	5e3b5b9edd35d20e035a827aa6f1d793
URL:		http://kde-look.org/content/show.php?content=6384
Requires:	superkaramba
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
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/{background,fonts} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/flat/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/liquid/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/um/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/weather.com/{large_icons,small_icons} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/{medium,weak,strong} \
	$RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/{medium,weak,strong} \

install liquid_weather_plus/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus
install liquid_weather_plus/background/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/background
install liquid_weather_plus/fonts/*.ttf $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/liquid_weather_plus/fonts
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
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/background
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/fonts
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/icons/flat/large_icons
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/icons/flat/small_icons
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/icons/liquid/large_icons
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/icons/liquid/small_icons
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/icons/um/large_icons
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/icons/um/small_icons
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/icons/weather.com/large_icons
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/icons/weather.com/small_icons
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/medium
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/strong
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/weak
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/medium
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/strong
%dir %{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/weak
%{_datadir}/themes/superkaramba/liquid_weather_plus/*.png
%{_datadir}/themes/superkaramba/liquid_weather_plus/*.txt
%{_datadir}/themes/superkaramba/liquid_weather_plus/*.py*
%{_datadir}/themes/superkaramba/liquid_weather_plus/*.theme
#%{_datadir}/themes/superkaramba/liquid_weather_plus/*.timings
#%{_datadir}/themes/superkaramba/liquid_weather_plus/*.patch
%{_datadir}/themes/superkaramba/liquid_weather_plus/*.html
%{_datadir}/themes/superkaramba/liquid_weather_plus/background/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/fonts/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/flat/large_icons/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/flat/small_icons/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/liquid/large_icons/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/liquid/small_icons/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/um/large_icons/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/um/small_icons/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/weather.com/large_icons/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/icons/weather.com/small_icons/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/medium/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/strong/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/flat/weak/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/medium/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/strong/*
%{_datadir}/themes/superkaramba/liquid_weather_plus/wind_icons/liquid/weak/*

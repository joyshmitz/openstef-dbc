# SPDX-FileCopyrightText: 2017-2021 Alliander N.V. <korte.termijn.prognoses@alliander.com>
# SPDX-FileCopyrightText: 2021 2017-2021 Alliander N.V. <korte.termijn.prognoses@alliander.com>
#
# SPDX-License-Identifier: MPL-2.0

# Available featureset for optimization
FEATURESETS = {
    # 61 residential_features
    "A": [
        "clearSky_dlf",
        "clearSky_ulf",
        "clouds",
        "humidity",
        "mxlD",
        "pressure",
        "radiation",
        "rain",
        "snowDepth",
        "temp",
        "winddeg",
        "windspeed",
        "windspeed_100m",
        "sjv_E1A",
        "sjv_E1B",
        "sjv_E1C",
        "sjv_E2A",
        "sjv_E2B",
        "sjv_E3A",
        "sjv_E3B",
        "sjv_E3C",
        "sjv_E3D",
        "T-15min",
        "T-30min",
        "T-2160min",
        "T-2d",
        "T-3d",
        "T-4d",
        "T-5d",
        "T-6d",
        "T-7d",
        "T-8d",
        "T-9d",
        "T-10d",
        "T-11d",
        "T-12d",
        "T-13d",
        "T-14d",
        "IsWeekendDay",
        "IsSaturday",
        "IsSunday",
        "Month",
        "saturation_pressure",
        "vapour_pressure",
        "air_density",
        "dtemp_hour",
        "dtemp_day",
        "dtemp_week",
        "dwindspeed_quarter",
        "dwindspeed_day",
        "dwindspeed_week",
        "dwindspeed_100m_day",
        "dwindspeed_100m_week",
        "dwinddeg_day",
        "dwinddeg_week",
        "dpressure_day",
        "dpressure_week",
        "dhumidity_quarter",
        "dhumidity_day",
        "dhumidity_week",
        "dair_density_day",
    ],
    # 60 residential_solar_features
    "B": [
        "clearSky_dlf",
        "clearSky_ulf",
        "clouds",
        "humidity",
        "mxlD",
        "pressure",
        "radiation",
        "rain",
        "temp",
        "winddeg",
        "windspeed",
        "windspeed_100m",
        "sjv_E1A",
        "sjv_E1B",
        "sjv_E1C",
        "sjv_E2A",
        "sjv_E3A",
        "sjv_E3B",
        "sjv_E3C",
        "sjv_E3D",
        "T-900min",
        "T-780min",
        "T-15min",
        "T-30min",
        "T-60min",
        "T-2160min",
        "T-1d",
        "T-2d",
        "T-3d",
        "T-4d",
        "T-6d",
        "T-7d",
        "T-8d",
        "T-9d",
        "T-13d",
        "T-14d",
        "IsWeekDay",
        "Month",
        "saturation_pressure",
        "vapour_pressure",
        "air_density",
        "dtemp_quarter",
        "dtemp_hour",
        "dtemp_day",
        "dtemp_week",
        "dwindspeed_quarter",
        "dwindspeed_day",
        "dwindspeed_week",
        "dwindspeed_100m_hour",
        "dwindspeed_100m_week",
        "dwinddeg_day",
        "dwinddeg_week",
        "dpressure_hour",
        "dpressure_day",
        "dpressure_week",
        "dhumidity_hour",
        "dhumidity_day",
        "dhumidity_week",
        "dair_density_day",
        "dair_density_week",
    ],
    # 61 residential_wind_solar_features
    "C": [
        "clearSky_dlf",
        "clearSky_ulf",
        "clouds",
        "humidity",
        "mxlD",
        "pressure",
        "radiation",
        "rain",
        "snowDepth",
        "temp",
        "winddeg",
        "windspeed",
        "windspeed_100m",
        "sjv_E1A",
        "sjv_E1B",
        "sjv_E1C",
        "sjv_E2A",
        "sjv_E2B",
        "sjv_E3A",
        "sjv_E3B",
        "sjv_E3C",
        "sjv_E3D",
        "T-15min",
        "T-30min",
        "T-45min",
        "T-1200min",
        "T-2160min",
        "T-2d",
        "T-3d",
        "T-4d",
        "T-5d",
        "T-6d",
        "T-7d",
        "T-8d",
        "T-9d",
        "T-10d",
        "T-11d",
        "T-12d",
        "T-13d",
        "T-14d",
        "IsWeekendDay",
        "IsWeekDay",
        "windpowerFit_harm_arome",
        "saturation_pressure",
        "vapour_pressure",
        "air_density",
        "dtemp_day",
        "dtemp_week",
        "dwindspeed_week",
        "dwindspeed_100m_day",
        "dwindspeed_100m_week",
        "dwinddeg_day",
        "dwinddeg_week",
        "dpressure_hour",
        "dpressure_week",
        "dhumidity_hour",
        "dhumidity_day",
        "dhumidity_week",
        "dair_density_hour",
        "dair_density_day",
        "dair_density_week",
    ],
    # 59 wind_features
    "D": [
        "clearSky_dlf",
        "clearSky_ulf",
        "clouds",
        "humidity",
        "mxlD",
        "pressure",
        "radiation",
        "rain",
        "temp",
        "winddeg",
        "windspeed",
        "windspeed_100m",
        "sjv_E1A",
        "sjv_E2A",
        "sjv_E2B",
        "sjv_E3A",
        "sjv_E3B",
        "T-15min",
        "T-30min",
        "T-1440min",
        "T-45min",
        "T-2880min",
        "T-2160min",
        "T-2d",
        "T-3d",
        "T-4d",
        "T-5d",
        "T-6d",
        "T-7d",
        "T-10d",
        "T-11d",
        "T-12d",
        "T-13d",
        "T-14d",
        "IsMonday",
        "IsSaturday",
        "windpowerFit_harm_arome",
        "saturation_pressure",
        "vapour_pressure",
        "air_density",
        "dtemp_week",
        "dwindspeed_hour",
        "dwindspeed_day",
        "dwindspeed_week",
        "dwindspeed_100m_quarter",
        "dwindspeed_100m_hour",
        "dwindspeed_100m_day",
        "dwindspeed_100m_week",
        "dwinddeg_quarter",
        "dwinddeg_hour",
        "dwinddeg_day",
        "dwinddeg_week",
        "dpressure_quarter",
        "dpressure_week",
        "dhumidity_quarter",
        "dhumidity_day",
        "dhumidity_week",
        "dair_density_day",
        "dair_density_week",
    ],
    # 58 tuinders_features
    "E": [
        "clearSky_dlf",
        "clearSky_ulf",
        "clouds",
        "humidity",
        "mxlD",
        "pressure",
        "radiation",
        "rain",
        "temp",
        "winddeg",
        "windspeed",
        "windspeed_100m",
        "sjv_E1A",
        "sjv_E1B",
        "sjv_E1C",
        "sjv_E2B",
        "sjv_E3A",
        "sjv_E3B",
        "sjv_E3D",
        "T-15min",
        "T-30min",
        "T-45min",
        "T-2160min",
        "T-2d",
        "T-3d",
        "T-4d",
        "T-5d",
        "T-6d",
        "T-7d",
        "T-8d",
        "T-9d",
        "T-10d",
        "T-11d",
        "T-12d",
        "T-13d",
        "T-14d",
        "IsWeekendDay",
        "Month",
        "saturation_pressure",
        "vapour_pressure",
        "air_density",
        "dtemp_quarter",
        "dtemp_week",
        "dwindspeed_quarter",
        "dwindspeed_hour",
        "dwindspeed_day",
        "dwindspeed_100m_week",
        "dwinddeg_hour",
        "dwinddeg_day",
        "dwinddeg_week",
        "dpressure_day",
        "dpressure_week",
        "dhumidity_hour",
        "dhumidity_day",
        "dhumidity_week",
        "dair_density_hour",
        "dair_density_day",
        "dair_density_week",
    ],
    # 64 industry_features
    "F": [
        "clearSky_dlf",
        "clearSky_ulf",
        "clouds",
        "humidity",
        "mxlD",
        "pressure",
        "radiation",
        "rain",
        "snowDepth",
        "temp",
        "winddeg",
        "windspeed",
        "windspeed_100m",
        "sjv_E1A",
        "sjv_E1B",
        "sjv_E1C",
        "sjv_E3A",
        "sjv_E3B",
        "sjv_E3C",
        "sjv_E3D",
        "T-900min",
        "T-15min",
        "T-30min",
        "T-45min",
        "T-180min",
        "T-2880min",
        "T-240min",
        "T-2d",
        "T-3d",
        "T-4d",
        "T-5d",
        "T-6d",
        "T-7d",
        "T-8d",
        "T-9d",
        "T-10d",
        "T-11d",
        "T-12d",
        "T-13d",
        "T-14d",
        "windspeed_100mExtrapolated",
        "windpowerFit_harm_arome",
        "saturation_pressure",
        "vapour_pressure",
        "dewpoint",
        "air_density",
        "dtemp_hour",
        "dtemp_day",
        "dtemp_week",
        "dwindspeed_quarter",
        "dwindspeed_hour",
        "dwindspeed_day",
        "dwindspeed_100m_day",
        "dwindspeed_100m_week",
        "dwinddeg_quarter",
        "dwinddeg_hour",
        "dwinddeg_week",
        "dpressure_quarter",
        "dpressure_hour",
        "dpressure_day",
        "dpressure_week",
        "dhumidity_day",
        "dhumidity_week",
        "dair_density_week",
    ],
    # 77 all_groups_features
    "G": [
        "clearSky_dlf",
        "clearSky_ulf",
        "clouds",
        "humidity",
        "mxlD",
        "pressure",
        "radiation",
        "rain",
        "snowDepth",
        "temp",
        "winddeg",
        "windspeed",
        "windspeed_100m",
        "sjv_E1A",
        "sjv_E1B",
        "sjv_E1C",
        "sjv_E2A",
        "sjv_E2B",
        "sjv_E3A",
        "sjv_E3B",
        "sjv_E3C",
        "sjv_E3D",
        "T-900min",
        "T-15min",
        "T-30min",
        "T-45min",
        "T-2880min",
        "T-2160min",
        "T-2d",
        "T-3d",
        "T-4d",
        "T-5d",
        "T-6d",
        "T-7d",
        "T-8d",
        "T-9d",
        "T-10d",
        "T-11d",
        "T-12d",
        "T-13d",
        "T-14d",
        "IsWeekendDay",
        "IsWeekDay",
        "IsSunday",
        "Month",
        "windspeed_100mExtrapolated",
        "windpowerFit_harm_arome",
        "saturation_pressure",
        "vapour_pressure",
        "air_density",
        "dtemp_quarter",
        "dtemp_hour",
        "dtemp_day",
        "dtemp_week",
        "dwindspeed_quarter",
        "dwindspeed_hour",
        "dwindspeed_day",
        "dwindspeed_week",
        "dwindspeed_100m_quarter",
        "dwindspeed_100m_hour",
        "dwindspeed_100m_day",
        "dwindspeed_100m_week",
        "dwinddeg_quarter",
        "dwinddeg_hour",
        "dwinddeg_day",
        "dwinddeg_week",
        "dpressure_quarter",
        "dpressure_hour",
        "dpressure_day",
        "dpressure_week",
        "dhumidity_quarter",
        "dhumidity_hour",
        "dhumidity_day",
        "dhumidity_week",
        "dair_density_hour",
        "dair_density_day",
        "dair_density_week",
    ],
    # empty feature set
    "N": None,
}
FEATURESET_NAMES = list(FEATURESETS.keys())

from mysql import connector
if __name__ == '__main__':
	db = connector.connect(host = "6.tcp.ngrok.io", port = 18706, user = "root", password = "ahmad123")
	cursor = db.cursor(buffered=True)
	cursor.execute("use platoon_db_02_23")
	cursor.execute("DROP TABLE IF EXISTS weatherbit_daily_weather_forecast_properties")
	cursor.execute("DROP VIEW IF EXISTS weatherbit_daily_weather_forecast")
	cursor.execute("""CREATE VIEW weatherbit_daily_weather_forecast AS
						SELECT DISTINCT 
						daily_weather_forecasts.lat as lat, 
						daily_weather_forecasts.lon as lon, 
						daily_weather_forecasts.city_name as city_name,
						daily_weather_forecasts.weather_description as weather_description, 
						daily_weather_forecasts.max_dhi as max_dhi,
						daily_weather_forecasts.wind_cdir as wind_cdir, 
						daily_weather_forecasts.wind_dir as wind_dir, 
						daily_weather_forecasts.wind_cdir_full as wind_cdir_full,
						daily_weather_forecasts.low_temp as low_temp,
						daily_weather_forecasts.uv as uv,
						daily_weather_forecasts.vis as vis,
						daily_weather_forecasts.wind_gust_spd as wind_gust_spd,
						daily_weather_forecasts.app_max_temp as app_max_temp,
						daily_weather_forecasts.clouds as clouds,
						daily_weather_forecasts.snow_depth as snow_depth,
						daily_weather_forecasts.dewpt as dewpt,
						daily_weather_forecasts.clouds_hi as clouds_hi,
						daily_weather_forecasts.pop as pop,
						daily_weather_forecasts.moonset_ts as moonset_ts,
						daily_weather_forecasts.slp as slp,
						daily_weather_forecasts.moonrise_ts as moonrise_ts,
						daily_weather_forecasts.app_min_temp as app_min_temp,
						daily_weather_forecasts.rh as rh,
						daily_weather_forecasts.wind_spd as wind_spd,
						daily_weather_forecasts.ozone as ozone,
						daily_weather_forecasts.high_temp as high_temp,
						daily_weather_forecasts.clouds_low as clouds_low,
						daily_weather_forecasts.temp as temp,
						daily_weather_forecasts.max_temp as max_temp,
						daily_weather_forecasts.snow as snow,
						daily_weather_forecasts.min_temp as min_temp,
						daily_weather_forecasts.precip as precip,
						daily_weather_forecasts.sunrise_ts as sunrise_ts,
						daily_weather_forecasts.clouds_mid as clouds_mid,
						daily_weather_forecasts.pres as pres,
						daily_weather_forecasts.sunset_ts as sunset_ts,
						REPLACE(daily_weather_forecasts.datetime, ' ', 'T') as datetime
						FROM daily_weather_forecasts""")
	cursor.execute("DROP TABLE IF EXISTS weatherbit_hourly_weather_forecast_properties")
	cursor.execute("DROP VIEW IF EXISTS weatherbit_hourly_weather_forecast")
	cursor.execute("""CREATE VIEW weatherbit_hourly_weather_forecast AS
						SELECT DISTINCT 
						hourly_weather_forecasts.lat as lat, 
						hourly_weather_forecasts.lon as lon, 
						hourly_weather_forecasts.city_name as city_name,
						hourly_weather_forecasts.weather_description as weather_description,
						hourly_weather_forecasts.dhi as dhi,
						hourly_weather_forecasts.wind_spd as wind_spd,
						hourly_weather_forecasts.temp as temp,
						hourly_weather_forecasts.app_temp as app_temp,
						hourly_weather_forecasts.clouds_low as clouds_low,
						hourly_weather_forecasts.uv as uv,
						hourly_weather_forecasts.pres as pres,
						hourly_weather_forecasts.clouds as clouds,
						hourly_weather_forecasts.pop as pop,
						hourly_weather_forecasts.clouds_mid as clouds_mid,
						hourly_weather_forecasts.slp as slp,
						hourly_weather_forecasts.rh as rh,
						hourly_weather_forecasts.snow as snow,
						hourly_weather_forecasts.dewpt as dewpt,
						hourly_weather_forecasts.vis as vis,
						hourly_weather_forecasts.precip as precip,
						hourly_weather_forecasts.clouds_hi as clouds_hi,
						hourly_weather_forecasts.wind_gust_spd as wind_gust_spd,
						hourly_weather_forecasts.dni as dni,
						hourly_weather_forecasts.snow_depth as snow_depth,
						hourly_weather_forecasts.solar_rad as solar_rad,
						hourly_weather_forecasts.ghi as ghi,
						hourly_weather_forecasts.wind_dir as wind_dir,
						hourly_weather_forecasts.wind_cdir_full as wind_cdir_full,
						hourly_weather_forecasts.wind_cdir as wind_cdir,
						hourly_weather_forecasts.ozone as ozone,
						REPLACE(hourly_weather_forecasts.timestamp_local, ' ', 'T') as timestamp_local, 
						REPLACE(hourly_weather_forecasts.timestamp_utc, ' ', 'T') as timestamp_utc
						FROM hourly_weather_forecasts""")
	cursor.execute("DROP TABLE IF EXISTS weather_observations_properties")
	cursor.execute("DROP VIEW IF EXISTS weather_observation_data")
	cursor.execute("""CREATE VIEW weather_observation_data AS
						SELECT DISTINCT 
						weather_observations.lat as lat, 
						weather_observations.lon as lon, 
						weather_observations.station as station,
						weather_observations.weather_description as weather_description,
						weather_observations.elev_angle as elev_angle,
						weather_observations.dhi as dhi,
						weather_observations.app_temp as app_temp,
						weather_observations.dni as dni,
						weather_observations.rh as rh,
						weather_observations.temp as temp,
						weather_observations.h_angle as h_angle,
						weather_observations.snow as snow,
						weather_observations.sunset as sunset,
						weather_observations.slp as slp,
						weather_observations.solar_rad as solar_rad,
						weather_observations.vis as vis,
						weather_observations.dewpt as dewpt,
						weather_observations.sunrise as sunrise,
						weather_observations.precip as precip,
						weather_observations.wind_cdir as wind_cdir,
						weather_observations.wind_dir as wind_dir,
						weather_observations.wind_cdir_full as wind_cdir_full,
						weather_observations.uv as uv,
						weather_observations.clouds as clouds,
						weather_observations.wind_spd as wind_spd,
						weather_observations.pres as pres,
						REPLACE(weather_observations.ob_time, ' ', 'T') as ob_time
						FROM weather_observations""")
cursor.execute("DROP VIEW IF EXISTS wind_farm_observation_w")
cursor.execute("""CREATE VIEW wind_farm_observation_w AS
					SELECT DISTINCT 
			           CAST(plants.id AS CHAR(20)) AS plant_id,
			           CAST(systems.id AS CHAR(20))  AS system_id,
			           systems.name AS genUnitName,
			           country.country_code AS ccode,
			           plants.name AS plant_name,
			           assets.asset_name as asset_name,
			          weather_locations.city AS city,
			          weather_locations.lat AS lat,
			          weather_locations.lon AS lon
			       FROM `systems`
			           JOIN system_types ON systems.system_type_id = system_types.id
			           JOIN plants ON systems.plant_id = plants.id
			           JOIN weather_locations ON plants.weather_location_id = weather_locations.id
			           JOIN assets ON assets.id = plants.asset_id
			           JOIN organization ON assets.organization_id = organization.id
			           JOIN country ON country.id = organization.country_id
			           JOIN eic_functions ON assets.eic_function_id = eic_functions.id
			        WHERE
			           system_types.system_group = 'GeneratingUnit' AND 
			           eic_functions.eic_type_function_acronym = 'RES-W'""")
cursor.execute("DROP VIEW IF EXISTS wind_farm_observation_pv")
cursor.execute("""CREATE VIEW wind_farm_observation_pv AS
					SELECT DISTINCT 
			           CAST(plants.id AS CHAR(20)) AS plant_id,
			           CAST(systems.id AS CHAR(20))  AS system_id,
			           systems.name AS genUnitName,
			           country.country_code AS ccode,
			           plants.name AS plant_name,
			           assets.asset_name as asset_name,
			          weather_locations.city AS city,
			          weather_locations.lat AS lat,
			          weather_locations.lon AS lon
			       FROM `systems`
			           JOIN system_types ON systems.system_type_id = system_types.id
			           JOIN plants ON systems.plant_id = plants.id
			           JOIN weather_locations ON plants.weather_location_id = weather_locations.id
			           JOIN assets ON assets.id = plants.asset_id
			           JOIN organization ON assets.organization_id = organization.id
			           JOIN country ON country.id = organization.country_id
			           JOIN eic_functions ON assets.eic_function_id = eic_functions.id
			        WHERE
			           system_types.system_group = 'GeneratingUnit' AND 
			           eic_functions.eic_type_function_acronym = 'RES-PV'""")
cursor.execute("DROP VIEW IF EXISTS wind_farm_production_forecast")
cursor.execute("""CREATE VIEW wind_farm_production_forecast AS
					SELECT DISTINCT 
			            systems.name as genUnitName,
			            CAST(systems.id AS CHAR(20)) as system_id,
			            REPLACE(timestamp_start, ' ', 'T') as timestamp_start,  
			            REPLACE(timestamp_end, ' ', 'T') as timestamp_end,
			            value,
			            wind_plant_energy_production_forecast.id as id
			          FROM wind_plant_energy_production_forecast
			            JOIN systems ON systems.id = wind_plant_energy_production_forecast.system_id""")
cursor.execute("DROP VIEW IF EXISTS wind_farm_production")
cursor.execute("""CREATE VIEW wind_farm_production AS
					SELECT DISTINCT 
			            systems.name as genUnitName,
			            CAST(systems.id AS CHAR(20)) as system_id,
			            REPLACE(timestamp_start, ' ', 'T') as timestamp_start,  
			            REPLACE(timestamp_end, ' ', 'T') as timestamp_end,
			            value,
			            wind_plant_energy_production.id as id
			          FROM wind_plant_energy_production
			            JOIN systems ON systems.id = wind_plant_energy_production.system_id""")
cursor.execute("DROP VIEW IF EXISTS wind_plant_production_forecast")
cursor.execute("""CREATE VIEW wind_plant_production_forecast AS
					SELECT DISTINCT 
						id, 
						system_id, 
						value, 
						REPLACE(timestamp_start, ' ', 'T') as timestamp_start,  
						REPLACE(timestamp_end, ' ', 'T') as timestamp_end 
					FROM wind_plant_energy_production_forecast""")
cursor.execute("DROP VIEW IF EXISTS wind_plant_production")
cursor.execute("""CREATE VIEW wind_plant_production AS
					SELECT DISTINCT 
						id, 
						system_id, 
						value, 
						REPLACE(timestamp_start, ' ', 'T') as timestamp_start,  
						REPLACE(timestamp_end, ' ', 'T') as timestamp_end 
					FROM wind_plant_energy_production""")
cursor.execute("DROP VIEW IF EXISTS wind_farm_observation_data")
cursor.execute("""CREATE VIEW wind_farm_observation_data AS
					SELECT DISTINCT
		                plants.id AS plant_id,
		                plants.name AS plant_name,
		                weather_locations.city AS city,
		                assets.asset_name AS asset_name
		            FROM
		                `plants`
		                JOIN weather_locations ON plants.weather_location_id = weather_locations.id
		                JOIN assets ON plants.asset_id = assets.id
		                JOIN organization ON assets.organization_id = organization.id
		                JOIN country ON organization.country_id = country.id
		                JOIN eic_functions ON assets.eic_function_id = eic_functions.id
		            WHERE
		                eic_functions.eic_type_function_acronym = 'RES-W'""")
cursor.execute("DROP VIEW IF EXISTS wind_farm_observation_property")
cursor.execute("""CREATE VIEW wind_farm_observation_property AS
					SELECT DISTINCT 
			              plants.name as plant_name,  
			              wind_plant_weather_data.plant_id as plant_id,
			              REPLACE(wind_plant_weather_data.timestamp, ' ', 'T') as timestamp,
			              weather_locations.lon as lon,
			              weather_locations.lat as lat,
			              weather_locations.city as city,
			              assets.asset_name as asset_name
			          FROM `plants`     
			              JOIN wind_plant_weather_data 
			                ON plants.id = wind_plant_weather_data.plant_id 
			              JOIN weather_locations 
			                ON plants.weather_location_id = weather_locations.id
			              JOIN assets 
			                ON plants.asset_id = assets.id""")
cursor.execute("DROP VIEW IF EXISTS wind_farm_observation_evaluation")
cursor.execute("""CREATE VIEW wind_farm_observation_evaluation AS
					SELECT DISTINCT 
						REPLACE(timestamp, ' ', 'T') as timestamp, 
						plant_id, 
						out_temperature,
						pressure,
						wind_dir,
						wind_spd
					FROM wind_plant_weather_data""")
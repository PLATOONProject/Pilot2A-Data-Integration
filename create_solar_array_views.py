from mysql import connector
from rdfizer import semantify
import sys
import os
if __name__ == '__main__':
	i = 1
	os.system("rm rdf-dump/pilot2a-RES-PROD-solar_array.nt")
	cursor.execute("DROP VIEW IF EXISTS solar_array_observation")
	while (1000000*(i-1))+1 < 35000000:
		db = connector.connect(host = "6.tcp.ngrok.io", port = 18706, user = "root", password = "XXX")
		cursor = db.cursor(buffered=True)
		cursor.execute("use platoon_db_02_23")
		print("Part " + str(i))
		cursor.execute("DROP VIEW IF EXISTS solar_array_observation_part" + str(i))
		cursor.execute("DROP VIEW IF EXISTS solar_array_observation")
		create = "CREATE VIEW solar_array_observation AS\n"
		create +="""SELECT DISTINCT 
					  plants.name as plant_name,  
					  CAST(pv_plant_weather_data.plant_id AS CHAR(20)) as plant_id,
					  REPLACE(pv_plant_weather_data.timestamp, ' ', 'T') as timestamp,
					  weather_locations.lon as lon,
					  weather_locations.lat as lat,
					  weather_locations.city as city,
					  assets.asset_name as asset_name
					FROM `plants`     
					  JOIN pv_plant_weather_data 
					    ON plants.id = pv_plant_weather_data.plant_id 
					  JOIN weather_locations 
					    ON plants.weather_location_id = weather_locations.id
					  JOIN assets 
					    ON plants.asset_id = assets.id """
		create += "WHERE pv_plant_weather_data.id " + str((1000000*(i-1))+1) + " AND " + str(1000000*i)
		cursor.execute(create)
		cursor.execute("DROP VIEW IF EXISTS solar_array_observation_data_part"+ str(i))
		cursor.execute("DROP VIEW IF EXISTS solar_array_observation_data")
		create = "CREATE VIEW solar_array_observation_data AS\n"
		create += """SELECT DISTINCT 
						plant_id,
						out_temperature,
						insolation,
						panel_temperature,
						wind_spd,
						wind_dir,
						REPLACE(timestamp, ' ', 'T') as timestamp
						FROM pv_plant_weather_data """
		create += "WHERE id" + str((1000000*(i-1))+1) + " AND " + str(1000000*i)
		cursor.execute(create)
		semantify("config_solar_array.ini")
		os.system("cat solar_array.nt >> pilot2a-RES-PROD-solar_array.nt")
		i += 1
	print("Part 36")
	db = connector.connect(host = "6.tcp.ngrok.io", port = 18706, user = "root", password = "ahmad123")
	cursor = db.cursor(buffered=True)
	cursor.execute("use platoon_db_02_23")
	cursor.execute("DROP VIEW IF EXISTS solar_array_observation")
	cursor.execute("""CREATE VIEW solar_array_observation AS
						SELECT DISTINCT 
						  plants.name as plant_name,  
						  CAST(pv_plant_weather_data.plant_id AS CHAR(20)) as plant_id,
						  REPLACE(pv_plant_weather_data.timestamp, ' ', 'T') as timestamp,
						  weather_locations.lon as lon,
						  weather_locations.lat as lat,
						  weather_locations.city as city,
						  assets.asset_name as asset_name
						FROM `plants`     
						  JOIN pv_plant_weather_data 
						    ON plants.id = pv_plant_weather_data.plant_id 
						  JOIN weather_locations 
						    ON plants.weather_location_id = weather_locations.id
						  JOIN assets 
						    ON plants.asset_id = assets.id
						    WHERE pv_plant_weather_data.id BETWEEN 35000001 and 35314742""")
	cursor.execute("DROP VIEW IF EXISTS solar_array_observation_data")
	cursor.execute("""CREATE VIEW solar_array_observation_data AS
						SELECT DISTINCT 
						plant_id,
						out_temperature,
						insolation,
						panel_temperature,
						wind_spd,
						wind_dir,
						REPLACE(timestamp, ' ', 'T') as timestamp
						FROM pv_plant_weather_data
						WHERE id BETWEEN 35000001 and 35314742""")
	semantify("config_solar_array.ini")
	os.system("cat solar_array.nt >> pilot2a-RES-PROD-solar_array.nt")
	os.system("rm solar_array.nt")
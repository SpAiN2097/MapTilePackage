import arcpy, os
from arcpy import mp

project = arcpy.mp.ArcGISProject("CURRENT")
map = project.listMaps("MSR") [0]

# Cursor para acessar tabela de setores 
# for row in arcpy.SearchCursor(r"Database Connections\wsqlprd10v.vitor.sde\geodatabase." + r'"IBGE\VITOR"' + ".T_LM_SETORES"):
for row in arcpy.SearchCursor(r"G:\BaseTerritorial\Atendimentos\2PP_CensoAgro\SaoMiguelArcanjo\LimitesSetoresPP.shp"):
	map.extent = row.SHAPE.extent # ajusta a extensao do dataframe a extensao do setor
	# map.scale = map.scale * 1.1 # ajusta a escala para dar uma margem maior ao setor no mapa
	# arcpy.RefreshActiveView()
	geocodigo =  row.getValue("cd_geocodi")
	project.save()
	print("Salvando pacote de mapa do setor  " + geocodigo)
	if row.getValue("cd_situaca") == "8":
		arcpy.CreateMapTilePackage_management( project, "ONLINE", "G:/BaseTerritorial/Atendimentos/2PP_CensoAgro/MapTilePackages/" + geocodigo + ".tpk", "JPEG", "18", "#", "Teste para a Segunda Prova Piloto do Censo Agropecuário. Tile Package com mapa do setor", "Censo Agropecuário, IBGE, teste")
	else:
		print("Salvando pacote de mapa do setor  " + geocodigo)
		arcpy.CreateMapTilePackage_management( project, "ONLINE", "G:/BaseTerritorial/Atendimentos/2PP_CensoAgro/MapTilePackages/" + geocodigo + ".tpk", "JPEG", "20", "#", "Teste para a Segunda Prova Piloto do Censo Agropecuário. Tile Package com mapa do setor", "Censo Agropecuário, IBGE, teste")
		
		
# Runtime error 
# Traceback (most recent call last):
  # File "<string>", line 19, in <module>
  # File "c:\program files (x86)\arcgis\desktop10.2\arcpy\arcpy\management.py", line 7170, in CreateMapTilePackage
    # raise e
# RuntimeError: Object: Error in executing tool
# -*- #################
# ---------------------------------------------------------------------------
# export_MPKG_PRO.py
# Created on: 2016-04-06
# Author: Vitor França (vitor.franca@ibge.gov.br)
# Description: Create tile packages for IBGE data collection using "ArcGIS Runtime/Android SDK" enabled mobile devices.
# ---------------------------------------------------------------------------
import arcpy, os
from arcpy import mp

prj = arcpy.mp.ArcGISProject("CURRENT")
map = prj.listMaps() [0]
lyr = map.listLayers("T_LM_SETORES")[0]
lyt = prj.listLayouts()[0]
mf = lyt.listElements()[0]

# Cursor para acessar tabela de setores 
for row in arcpy.SearchCursor(lyr):
	geocodigo =  row.getValue("cd_geocodigo")
	if row.getValue("cd_situacao") == "8":
		print("Salvando pacote de mapa do setor  " + geocodigo)
		map.name = "Setor_" + geocodigo
		output_package =  r"G:\BaseTerritorial\MapTilePackages\mapa_setor_" + geocodigo + ".tpk"
		# ajusta a escala para dar uma margem maior ao setor no mapa
		extent = row.getValue("SHAPE").extent 
		mf.camera.setExtent(extent) 
		mf.camera.scale = mf.camera.scale * 1.1
		prj.save()
		print (extent.JSON)
		arcpy.CreateMapTilePackage_management(map.name, "ONLINE", output_package, "JPEG", "15", "#", "Prova de Conceito para geração automática de pacotes de mapa para o Censo Agropecuário" , "Censo Agropecuário, IBGE, teste")
	else:
		print("Pulando setor  " + geocodigo)
		# print (extent.JSON)
		# arcpy.CreateMapTilePackage_management(map, "ONLINE", "G:/BaseTerritorial/Atendimentos/2PP_CensoAgro/MapTilePackages/" + geocodigo + ".tpk", "JPEG", "20", "#", "Teste para a Segunda Prova Piloto do Censo Agropecuário. Tile Package com mapa do setor", "Censo Agropecuário, IBGE, teste")
	
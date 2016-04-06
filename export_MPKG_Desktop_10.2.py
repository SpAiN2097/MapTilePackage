import arcpy, os, time
import arcpy.mapping

mxd = arcpy.mapping.MapDocument('CURRENT')
df = arcpy.mapping.ListDataFrames(mxd, "Layers") [0]
layer = r"Database Connections\wsqlprd10v.vitor.sde\geodatabase." + r'"IBGE\VITOR"' + ".T_LM_SETORES"

# Cursor para acessar tabela de t_lm_setores 
for row in arcpy.SearchCursor(layer):
	df.extent = row.SHAPE.extent # ajusta a extensao do dataframe a extensao do setor
	df.scale = df.scale * 1.1 # ajusta a escala para dar uma margem maior ao setor no mapa
	geocodigo =  row.getValue("cd_geocodigo")
	# arcpy.MakeFeatureLayer_management (layer, "setor")
	# arcpy.SelectLayerByAttribute_management (layer, "NEW_SELECTION", "[cd_geocodigo] = geocodigo")
	# df.zoomToSelectedFeatures()	
	arcpy.RefreshActiveView()
	mxd.save()
	# exportacao da view ajustada a extensao de cada setor
	# Exporta PDF
	pdf_name = geocodigo + ".pdf"
	print("Imprimindo mapa  " + pdf_name)
	arcpy.mapping.ExportToPDF(mxd, pdf_name)
	time.sleep(1) # Wait 1 Seconds
	
	
	

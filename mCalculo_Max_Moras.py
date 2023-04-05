import json
import pandas as pd
import numpy as np


def Calculo_Max_Mora(gender, edad, provincia, jefe, EC, hijos, ans_bin_hijos, sede, grado, 
                     carrera, materias, monto_fin, monto_couta, laboral, patrono, 
                     propiedades, vehiculos, hipoteca, ingreso, por_beca, por_matricula, 
                     monto_beca, monto_matricula):
    
    with open('pesos_latina.json', encoding='utf-8-sig') as f:
        data = json.load(f)    
    intercept = float(data[0]['Intercept'])
    
    #GENERO
    w_gender = float(data[0]["Genero" + gender])      
    
    #EDAD 
    edad_int = [pd.Interval(left=20, right=21, closed='left'), 
                pd.Interval(left=22, right=25, closed='left'), 
                pd.Interval(left=25, right=31, closed='left'), 
                pd.Interval(left=31, right=71, closed='left'),
                pd.Interval(left=0, right=20, closed='left')]
    
    wh_edad = np.arange(len(edad_int))[[edad in x for x in edad_int]][0]
    w_edad = float(data[0]["q_Edad_"+ str(wh_edad)])
    
    #PROVINCIA
    w_provincia = float(data[0]["Provincia" + provincia])
    
    #JEFE
    w_jefe = float(data[0]["jefehogar" + str(int(jefe))])
    
    #ESTADO CIVIL
    w_EC = float(data[0]["EstadoCivil" + EC])
    
    #HIJOS
    w_hijos = 0
    if ans_bin_hijos != "No registra":
        w_hijos = float(data[0]["hijos"])*hijos
        
    #SEDE
    w_sede = float(data[0]["SEDE" + sede])
    
    #GRADO
    w_grado = float(data[0]["Grado" + grado])
    
    #Carrera
    w_carrera = float(data[0]["Carrera" + carrera])
    
    #Materias
    w_materias = float(data[0]["`Materias matriculadas`"])*materias
    
    #monto_fin
    monto_fin_int = [pd.Interval(left=1.87e+05, right=2.43e+05, closed='left'), 
                    pd.Interval(left=2.43e+05, right=3.1e+05, closed='left'), 
                    pd.Interval(left=3.1e+05, right=4.31e+05, closed='left'), 
                    pd.Interval(left=4.31e+05, right=3.62e+06, closed='left'),
                    pd.Interval(left=0, right=1.87e+05, closed='left')]
    
    wh_monto_fin = np.arange(len(monto_fin_int))[[monto_fin in x for x in monto_fin_int]][0]
    w_monto_fin = float(data[0]["q_monto_financiado_"+ str(wh_monto_fin)])

    #monto_couta
    monto_couta_int = [pd.Interval(left=0, right=5.74e+04, closed='left'), 
                    pd.Interval(left=5.74e+04, right=7.64e+04, closed='left'), 
                    pd.Interval(left=7.64e+04, right=9.76e+04, closed='left'), 
                    pd.Interval(left=9.76e+04, right=1.38e+05, closed='left'),
                    pd.Interval(left=1.38e+05, right=1.14e+06, closed='left')]
    
    wh_monto_couta = np.arange(len(monto_couta_int))[[monto_couta in x for x in monto_couta_int]][0]
    w_monto_couta = float(data[0]["q_monto_cuota_"+ str(wh_monto_couta)])
    
    #Estatus Laboral + Tipo Patrono
    w_laboral = 0
    w_patrono = float(data[0]["Tipo_PatronoNo Trabaja"])
    if laboral == "SI":
        w_laboral = float(data[0]["status_lab1"])
        w_patrono = float(data[0]["Tipo_Patrono"+ patrono])
        
    #Propiedades
    w_propiedades = float(data[0]["propiedades"])*propiedades
    
    #Vehiculos
    w_vehiculos = float(data[0]["vehiculos"])*vehiculos
        
    #Vehiculos
    w_hipoteca = float(data[0]["Hipoteca1"])*hipoteca
    
    #INGRESO
    ingreso_int = [pd.Interval(left=0, right=4e+05, closed='left'), 
                    pd.Interval(left=4e+05, right=5.12e+05, closed='left'), 
                    pd.Interval(left=5.12e+05, right=6.7e+05, closed='left'), 
                    pd.Interval(left=6.7e+05, right=1.25e+06, closed='left'),
                    pd.Interval(left=1.25e+06, right=4.96e+06, closed='left')]
    
    wh_ingreso = np.arange(len(ingreso_int))[[ingreso in x for x in ingreso_int]][0]
    w_ingreso = float(data[0]["q_ingreso_"+ str(wh_ingreso)])
    
    
    #PORCENTAJE BECA
    por_beca_int = [pd.Interval(left=-10, right=0, closed='left'), 
                    pd.Interval(left=0, right=20, closed='left'), 
                    pd.Interval(left=20, right=35, closed='left'), 
                    pd.Interval(left=35, right=100, closed='left')]
    
    wh_por_beca = np.arange(len(por_beca_int))[[por_beca in x for x in por_beca_int]][0]
    w_por_beca = float(data[0]["q_beca_"+ str(wh_por_beca)])
    
    #PORCENTAJE MATRICULA
    por_matricula_int = [pd.Interval(left=-10, right=0, closed='left'), 
                    pd.Interval(left=0, right=15, closed='left'), 
                    pd.Interval(left=15, right=20, closed='left'), 
                    pd.Interval(left=20, right=35, closed='left'),
                    pd.Interval(left=35, right=100, closed='left')]
    
    wh_por_matricula = np.arange(len(por_matricula_int))[[por_matricula in x for x in por_matricula_int]][0]
    w_por_matricula = float(data[0]["q_descuentoMat_"+ str(wh_por_matricula)])
    
    #Descuento Matricula
    w_monto_beca = float(data[0]["DescMat"])*monto_beca
        
    #Descuento Colegiatura
    w_monto_matricula = float(data[0]["DescCol"])*monto_matricula
    
    
    max_dias = sum([w_monto_matricula, w_monto_beca, w_por_matricula, w_por_beca,
                    w_ingreso, w_hipoteca, w_vehiculos, w_propiedades, w_patrono,
                    w_laboral, w_monto_couta, w_monto_fin, w_materias, w_carrera,
                    w_grado, w_sede, w_hijos, w_EC, w_jefe, w_provincia, w_edad,
                    w_gender, intercept])    
    
    
    result = int(max_dias)
    
    if int(max_dias) < 0:
        result = 0
    
    return result
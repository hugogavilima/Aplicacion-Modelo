import streamlit as st
from PIL import Image
from io import BytesIO
from PIL import Image
from mCalculo_Max_Moras import*

 
    
st.set_page_config(layout="wide", page_title="Máximo Días de Mora")


st.write("# Máximo Días de Mora")
st.sidebar.write("### Calculadora")
st.sidebar.write(
    "Esta aplicación te permite calcular el máximo días de mora de una persona dada su información académica, civil y financiera. Además, toma en cuenta si el estudiante tiene algún tipo de descuento tanto en su colegiatura o matricula del semestre en cuestión."
    )

opciones = ['Universidad Latina de Costa Rica', 'Universidad Americana']
ans_box = st.sidebar.selectbox('Por favor elija la universidad correspondiente:', opciones)

if ans_box == opciones[0]:
    image = Image.open("Universidad Latina de Costa Rica.png")
    
if ans_box == opciones[1]:
    image = Image.open("Universidad Americana.png")
    
    
##Steamos correctamente la imagen

width, height = image.size
max_width = 300
if width > max_width:
    height *= max_width / width
    width = max_width
image = image.resize((int(width), int(height)))
x_offset = 20
y_offset = 20

# Añadir la imagen a la aplicación
st.sidebar.image(image, 
                use_column_width=False, 
                clamp=True, 
                width=width, 
                caption=ans_box, 
                output_format='PNG', 
                channels='RGB')

col1, col2, col3 = st.columns(3)

# Agregamos tres cajas de selección a la primera columna


##Opciones para cada variable
gender = ['Femenino', 'Masculino', 'No registra']
sede = ['Heredia', 'Cañas', 'San Pedro', 'Ciudad Neily', 'Grecia',
       'Guápiles', 'Pérez Zeledón', 'Santa Cruz']
provincia = ['HEREDIA', 'ALAJUELA', 'PUNTARENAS', 'SAN JOSE', 'No registra',
       'LIMON', 'CARTAGO', 'GUANACASTE']
patrono = ['Gobierno', 'Privado', 'Independiente']
EC = ['Divorciado(a)', 'Casado(a)', 'Soltero(a)', 'Viudez']
hijos = [ "NO", "SI", "No registra"]
bin_lab = [ "NO","SI", "No registra"]
ans_bin_hijos = "No registra"
ans_bin_lab = "No registra"
carrera = ['RELACIONES PÚBLICAS', 'INGENIERÍA INDUSTRIAL', 'TERAPIA FÍSICA',
       'ENFERMERÍA', 'ARQUITECTURA', 'ARQUITECTURA Y URBANISMO',
       'INGENIERÍA ELECTROMECÁNICA', 'SEGURIDAD INFORMÁTICA',
       'INGENIERÍA CIVIL', 'INGENIERÍA EN SISTEMAS COMPUTACIONALES',
       'LA ENSEÑANZA DEL INGLÉS', 'ADMINISTRACIÓN DE NEGOCIOS', 'DERECHO',
       'OPTOMETRÍA', 'MEDICINA Y CIRUGÍA', 'ODONTOLOGÍA',
       'DISEÑO GRÁFICO', 'COMUNICACIÓN DIGITAL', 'TRABAJO SOCIAL',
       'PERIODISMO', 'PUBLICIDAD', 'ADMINISTRACIÓN DE EMPRESAS HOTELERAS',
       'PSICOLOGÍA', 'INGENIERÍA ELECTRÓNICA',
       'DISEÑO Y DECORACIÓN DE INTERIORES', 'CONTADURÍA',
       'INGENIERÍA MECÁNICA Y ADMINISTRACIÓN', 'ANIMACIÓN DIGITAL',
       'GASTRONOMÍA', 'CIENCIAS DE LA EDUCACIÓN PREESCOLAR', 'FARMACIA',
       'COMUNICACIÓN DE MERCADEO',
       'TECNOLOGÍAS DE INFORMACIÓN PARA LA GESTIÓN DE LOS NEGOCIOS',
       'CIENCIAS BIOLÓGICAS', 'CIENCIAS DE LA EDUCACIÓN',
       'CONTADURÍA PÚBLICA', 'INGENIERÍA EN ELECTROMEDICINA',
       'INGENIERÍA EN TELEMÁTICA', 'ECONOMÍA',
       'INGENIERÍA DE SISTEMAS INFORMÁTICOS', 'TURISMO SOSTENIBLE',
       'CIENCIAS DE LA COMUNICACIÓN COLECTIVA', 'INGENIERÍA DEL SOFTWARE',
       'NUTRICIÓN', 'RELACIONES INTERNACIONALES',
       'INGENIERÍA DE SISTEMAS',
       'INGENIERÍA ELECTRÓNICA Y COMUNICACIONES',
       'ADMINISTRACIÓN DE LA HOSPITALIDAD']
grado = ['BACHILLERATO', 'LICENCIATURA']

with col1:
    st.write("### Civil")
    ans_gender = st.selectbox('Género', gender)
    ans_edad = st.slider('Edad', 18, 100)
    ans_provincia = st.selectbox('Provincia', provincia)
    st.write("")
    ans_jefe = st.checkbox('Es jefe de hogar')
    st.write("")
    ans_EC = st.selectbox('Estado Civil', EC)
    ans_bin_hijos = st.selectbox('Tiene hijos', hijos)
    ans_hijos = 0
    
    if ans_bin_hijos == "SI":
        ans_hijos = st.slider('Numero de Hijos', 0, 5)
        

    
     
    


# Agregamos tres cajas de selección a la segunda columna
with col2:
    st.write("### Académica")
    ans_sede = st.selectbox('SEDE', sede)
    ans_grado =st.selectbox('Grado mayor alcanzado', grado)
    ans_carrera = st.selectbox('Carrera en Curso', carrera)
    ans_materias = st.slider('Materias Matriculadas', 0, 7)
    ans_monto_fin = st.number_input('Escriba el monto financiado: ', min_value=0.0, max_value=1e7, step=0.1)
    ans_monto_couta = st.number_input('Escriba el valor de la couta: ', min_value=0.0, max_value=1e7, step=0.1)
       
    
    
with col3:
    st.write("### Financiera")
    ans_bin_lab = st.selectbox('Actualmente trabaja', bin_lab)
    ans_patrono = "No trabaja"
    
    if ans_bin_lab == "SI":
        ans_patrono = st.selectbox('Empleador', patrono)
    
    ans_propiedades = st.slider('Numero de Propiedades', 0, 20)
    ans_vehiculos = st.slider('Numero de Vehiculos', 0, 40)
    st.write("")
    ans_hipoteca = st.checkbox('Tiene un Credito Hipotecario')
    st.write("")
    ingreso = st.number_input('Escriba el ingreso estimado: ', min_value=0.0, max_value=1e15, step=0.1)

st.write("### Descuentos")
ans_beca = st.slider('Porcentaje de Descuento Colegiatura ', 0, 100)
ans_matricula_porc = st.slider('Porcentaje de Descuento Matricula ', 0, 100)
ans_beca_monto = st.number_input('Escriba el valor total del descuento en la colegiatura: ', min_value=0.0, max_value=1e7, step=0.1)
ans_matricula_monto = st.number_input('Escriba el valor total del descuento en la matricula: ', min_value=0.0, max_value=1e7, step=0.1)

if st.button('Calculo de Días de Mora'):
    max_days = Calculo_Max_Mora(ans_gender, ans_edad, ans_provincia, ans_jefe, ans_EC, ans_hijos, ans_bin_hijos, ans_sede, ans_grado, 
                                ans_carrera, ans_materias, ans_monto_fin, ans_monto_couta, ans_bin_lab, ans_patrono, 
                                ans_propiedades, ans_vehiculos, ans_hipoteca, ingreso, ans_beca, ans_matricula_porc, 
                                ans_beca_monto, ans_matricula_monto)
    st.markdown(
        f"""
        <div style='background-color:#ff3333; padding:20px; border-radius: 10px; '>
            <span style='color:white; font-size: 30px'>{"El usuario tendrá un máximo de "}</span><br>
            <span style='color:white; font-size: 200px'>{max_days}</span>
            <span style='color:white; font-size: 89px'>{" días mora"}</span>
        </div>
        """,
        unsafe_allow_html=True
    )



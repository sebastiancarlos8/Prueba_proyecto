import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf
from libreria_clases_proyecto1 import Empleado

st.sidebar.image("DMC.png", width = 100)
st.sidebar.title("Contenido")
modulos = st.sidebar.selectbox("Seleccione un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":
  st.title("Trabajo Práctico - Módulo Python Fundamentals")
  st.image("Python_logo.png", width = 500)
  st.subheader("Módulo: Especialización en Python for Analytics")
  st.write("**Año:** 2026")
  st.subheader("Elaborado por")
  st.write("**Nombre completo:** David Sebastian Carlos Ipanaque")
  st.subheader("Información general")
  st.markdown("""Egresado de la carrera de Ingeniería Industrial, con experiencia en analítica de datos en el sector retail, consumo masivo y seguros, dentro del área comercial y de recursos humanos. \nApasionado por la lógica, recursos humanos, uso de datos masivos y programación.""")
  st.subheader("Descripción del proyecto")
  st.markdown("""Portafolio de ejercicios que muestran los conocimientos aplicados en Python, mediante casuísticas de la vida cotidiana que implique el uso respecto a listas, registros con NumPy, arrays, DataFrame, librerías externas y clases.""")
  st.subheader("🛠️ Tecnologías utilizadas")
  st.markdown("""Para el presente proyecto, se utilizaron las siguientes tecnologías.\n- 🔗 GitHub\n- 🎨 Streamlit\n- 🐍 Google Colab - Python\n- 🔢 NumPy\n- 🐼 Pandas\n- 📚 Librerías externas\n- 🧩 Programación Orientada a Objetos(POO)""")
  
elif modulos == "Ejercicio 1":
  st.title("💰 Ejercicio 1 – Flujo de caja con listas")

  st.markdown("""Este ejercicio registra movimientos financieros utilizando una lista.\nCada movimiento contiene un concepto, tipo de movimiento y monto.
  
  \nFinalmente, la aplicación calcula los ingresos, gastos y saldo final e indica si el flujo de caja se encuentra a favor, en contra o equilibrado.""")

  # -------------------------
  # Registro del movimiento
  # -------------------------

  if "flujos" not in st.session_state:
    st.session_state.flujos = []

  # Variables

  st.subheader("📝 Registro del movimiento")
  
  Concepto = st.text_input("Concepto")
  Tipo = st.selectbox("Tipo de movimiento",["Ingreso","Gasto"])
  Monto = st.number_input("Monto",min_value=0.0, step = 0.01, format="%.2f")
  
  if st.button("➕ Registrar movimiento"):

  # Validación de variables

    if Concepto.strip() == "":
      st.error("⚠️ Debe ingresar un concepto.")

    elif Monto <= 0:
      st.error("⚠️ El monto debe ser mayor que S/ 0.00.")

    else:
      
      flujo = {
        "Concepto": Concepto,
        "Tipo": Tipo,
        "Monto": Monto
      }

      st.session_state.flujos.append(flujo)

      st.success("✅ Movimiento registrado correctamente.")

  # -------------------------
  # Cálculos
  # -------------------------

  total_ingresos = sum(
    flujo["Monto"]
    for flujo in st.session_state.flujos
    if flujo["Tipo"] == "Ingreso"
  )

  total_gastos = sum(
    flujo["Monto"]
    for flujo in st.session_state.flujos
    if flujo["Tipo"] == "Gasto"
  )

  saldo_final = total_ingresos - total_gastos

  # Resumen de flujos
  
  st.subheader("📊 Resumen del flujo de caja")

  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric("Total ingresos", f"S/ {total_ingresos:.2f}")

  with col2:
      st.metric("Total gastos", f"S/ {total_gastos:.2f}")

  with col3:
      st.metric("Saldo final", f"S/ {saldo_final:.2f}")

  if saldo_final > 0:
      st.success("🟢 El flujo de caja está a favor.")
  elif saldo_final < 0:
      st.error("El flujo de caja está en contra.")
  else:
      st.info("El flujo de caja está equilibrado.")

  st.subheader("📋 Flujos realizados")
  
  if len(st.session_state.flujos) > 0:
        st.dataframe(
          st.session_state.flujos,
          use_container_width=True,
          hide_index=True
      )
  
  else:
    st.info("ℹ️ No hay movimientos registrados.")


elif modulos == "Ejercicio 2":
  
  st.title("📦 Ejercicio 2 – NumPy, Arrays y DataFramee")

  st.markdown("""En este ejercicio se registrarán productos utilizando widgets de Streamlit. La información será almacenada en arreglos de NumPy y posteriormente convertida en un DataFrame de pandas para mostrar los registros actualizados.""")
  
  if "nombres" not in st.session_state:
      st.session_state.nombres = np.array([])
  
  if "categorias" not in st.session_state:
      st.session_state.categorias = np.array([])
  
  if "precios" not in st.session_state:
      st.session_state.precios = np.array([])
  
  if "cantidades" not in st.session_state:
      st.session_state.cantidades = np.array([])
  
  if "totales" not in st.session_state:
      st.session_state.totales = np.array([])
  
  # Registro de formulario
  
  st.subheader("Registro de producto")
  
  Nombre_producto = st.text_input("Nombre del producto")
  Categoria = st.selectbox("Categoría",["Computación","Accesorios","Electrónica", "Oficina", "Otros"])
  Precio = st.number_input(
      "Precio",
      min_value=0.0,
      step=0.01,
      format="%.2f"
  )
  
  Cantidad = st.number_input(
      "Cantidad",
      min_value=1,
      step=1
  )
  
  # Botón para agregar producto
  
  if st.button("Agregar producto"):
    
    if Nombre_producto.strip() == "":
      st.error("Debe ingresar el nombre del producto.")
  
    elif Precio <= 0:
      st.error("El precio debe ser mayor que 0.")
  
    elif Cantidad <= 0:
      st.error("La cantidad debe ser mayor que 0.")
  
    else:
      total = Precio * Cantidad
  
      # Agregar información a los arrays
  
      st.session_state.nombres = np.append(st.session_state.nombres,Nombre_producto)
      st.session_state.categorias = np.append(st.session_state.categorias,Categoria)
      st.session_state.precios = np.append(st.session_state.precios,Precio)
      st.session_state.cantidades = np.append(st.session_state.cantidades,Cantidad)
      st.session_state.totales = np.append(st.session_state.totales,total)
      st.success("Producto agregado correctamente.")
  
      
      
  df = pd.DataFrame({
        "Nombre del producto": st.session_state.nombres,
        "Categoría": st.session_state.categorias,
        "Precio": st.session_state.precios,
        "Cantidad": st.session_state.cantidades,
        "Total": st.session_state.totales
  })
      
      
    # --------------------------------------------------
    # Mostrar DataFrame
    # --------------------------------------------------
      
  st.subheader("Registros actualizados")
  if not df.empty:
      st.dataframe(
         st.style.format({
            "Precio": "S/ {:.2f}",
            "Total": "S/ {:.2f}"
         }),
         use_container_width=True,
         hide_index=True
      )
  else:
    st.info("Aún no hay datos registrados.")

elif modulos == "Ejercicio 3":
  st.title("📈 Ejercicio 3 – Funciones externas")

  st.markdown("""En este ejercicio se utiliza una función de una librería externa para calcular el valor futuro de una inversión mediante interés compuesto.\nEl resultado de cada cálculo se almacena en un histórico.""")

  funcion = st.selectbox(
    "Seleccione la función:",
    ["calcular_valor_futuro"]
  )

  if "historico_inversion" not in st.session_state:
      st.session_state.historico_inversion = []
   
  st.subheader("📝 Datos de la inversión")
  monto_inicial = st.number_input(
    "Monto inicial ($)",
    min_value=0.01,
    value=1000.00,
    step=100.00
  )

  tasa_anual_pct = st.number_input(
      "Tasa anual (%)",
      min_value=0.01,
      value=5.00,
      step=0.5
  )
  
  anios = st.number_input(
      "Número de años",
      min_value=0.1,
      value=5.0,
      step=0.5
  )
  
  capitalizaciones_por_anio = st.number_input(
      "Capitalizaciones por año",
      min_value=1,
      value=12,
      step=1
  )
  
  
  if st.button("📈 Calcular valor futuro"):

    try:

      if funcion == "calcular_valor_futuro":

        resultado = lf.calcular_valor_futuro(
            monto_inicial,
            tasa_anual_pct,
            anios,
            capitalizaciones_por_anio
        )

        # Mostrar resultado
        st.success("✅ Cálculo realizado correctamente")

        st.subheader("💰 Resultado")

        st.write(
            f"**Valor futuro:** ${resultado['valor_futuro']:,.2f}"
        )

        st.write(
            f"**Interés ganado:** ${resultado['interes_ganado']:,.2f}"
        )

        # Guardar resultado en el historial
        registro = {
            "Monto inicial": monto_inicial,
            "Tasa anual (%)": tasa_anual_pct,
            "Años": anios,
            "Capitalizaciones/año": capitalizaciones_por_anio,
            "Valor futuro": resultado["valor_futuro"],
            "Interés ganado": resultado["interes_ganado"]
        }

        st.session_state.historico_inversion.append(registro)

    except ValueError as e:
       st.error(f"⚠️ {e}")
  
  st.subheader("📊 Histórico de resultados")
    
  if len(st.session_state.historico_inversion) > 0:
  
      df_historial = pd.DataFrame(st.session_state.historico_inversion)
  
      st.dataframe(
          df_historial,
          use_container_width=True,
          hide_index=True
      )
  
  else:
      st.info("ℹ️ Todavía no se han realizado cálculos.")
  
else:
 st.title("👤 Ejercicio 4 – Clases externas y CRUD")

 st.markdown("""Este ejercicio implementa un CRUD utilizando la clase 'Empleado' desde una librería externa (librería de clases).\nLa aplicación permite crear, consultar, actualizar y eliminar
    empleados, utilizando los atributos y métodos definidos en la clase.
    """)

 if "empleados" not in st.session_state:
   st.session_state.empleados = []

 if "contador_empleados" not in st.session_state:
    st.session_state.contador_empleados = 0

 opcion = st.selectbox("Seleccione una operación:",["Crear empleado", "Ver empleados", "Actualizar empleado", "Eliminar empleado"])
 
 # Opción Crear

 if opcion == "Crear empleado":

   st.header("➕ Crear empleado")

   nombre = st.text_input(
        "Nombre del empleado"
   )

   salario_base = st.number_input(
        "Salario base",
        min_value=0.01,
        value=1000.00,
        step=100.00
   )

   porcentaje_bono = st.number_input(
        "Porcentaje de bono (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
   )

   porcentaje_descuento = st.number_input(
        "Porcentaje de descuento (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
   )

   if st.button("💾 Crear empleado"):

       if nombre.strip() == "":
           st.error("⚠️ Debes ingresar el nombre del empleado.")

       else:

           try:

               nuevo_empleado = Empleado(
                    nombre=nombre.strip(),
                    salario_base=salario_base,
                    porcentaje_bono=porcentaje_bono,
                    porcentaje_descuento=porcentaje_descuento
               )

               st.session_state.contador_empleados += 1

               nuevo_registro = {"id": st.session_state.contador_empleados, "empleado": nuevo_empleado}

               # Guarda el registro
               
               st.session_state.empleados.append(
                    nuevo_registro
               )

               st.success(
                    f"✅ El empleado {nombre.strip()} "
                    "fue creado correctamente."
               )

           except ValueError as e:
               st.error(f"⚠️ {e}")

 # Opción Leer

 elif opcion == "Ver empleados":

   st.header("📋 Lista de empleados")

   if len(st.session_state.empleados) == 0:

       st.info("ℹ️ No hay empleados registrados.")

   else:

       registros = []

       for registro in st.session_state.empleados:

           empleado = registro["empleado"]
           resumen = empleado.resumen()
           registros.append({
                    "ID": registro["id"],
                    "Nombre": resumen["nombre"],
                    "Salario base": resumen["salario_base"],
                    "Bono": resumen["bono"],
                    "Descuento": resumen["descuento"],
                    "Salario neto": resumen["salario_neto"]
           })

       df_empleados = pd.DataFrame(
                registros
       )

       st.dataframe(
            df_empleados,
            use_container_width=True,
            hide_index=True
       )

 # Opción Actualizar

 elif opcion == "Actualizar empleado":

   st.header("✏️ Actualizar empleado")

   if len(st.session_state.empleados) == 0:

       st.info("ℹ️ No hay empleados registrados para actualizar.")

   else:
     
     opciones_empleados = {
                f"ID {registro['id']} - "
                f"{registro['empleado'].nombre}": registro["id"]
                for registro in st.session_state.empleados
     }

     empleado_seleccionado = st.selectbox("Seleccione el empleado:", list(opciones_empleados.keys()))

     id_seleccionado = opciones_empleados[empleado_seleccionado]
     
     registro = next(
            registro
            for registro in st.session_state.empleados
            if registro["id"] == id_seleccionado
     )

     empleado = registro["empleado"]
     
     nuevo_nombre = st.text_input(
         "Nombre",
         value=empleado.nombre
       )

     nuevo_salario = st.number_input(
         "Salario base",
         min_value=0.01,
         value=float(empleado.salario_base),
         step=100.00,
         format="%.2f"
     )

     nuevo_bono = st.number_input(
         "Porcentaje de bono (%)",
         min_value=0.0,
         max_value=100.0,
         value=float(empleado.porcentaje_bono),
         step=1.0
     )

     nuevo_descuento = st.number_input(
         "Porcentaje de descuento (%)",
         min_value=0.0,
         max_value=100.0,
         value=float(empleado.porcentaje_descuento),
         step=1.0
     )

     if st.button("💾 Actualizar empleado"):

         if nuevo_nombre.strip() == "":
             st.error("⚠️ El nombre no puede estar vacío.")

         else:

           try:
                
                empleado_actualizado = Empleado(
                       nombre=nuevo_nombre.strip(),
                       salario_base=nuevo_salario,
                       porcentaje_bono=nuevo_bono,
                       porcentaje_descuento=nuevo_descuento
                )

                # Reemplazar únicamente el empleado correspondiente al ID seleccionado

                for i, registro in enumerate(
                     st.session_state.empleados
                ):
                  
                  if registro["id"] == id_seleccionado:
                    
                    st.session_state.empleados[i] = {
                                 "id": registro["id"],
                                 "empleado": empleado_actualizado
                    }

                    break
                   
                st.success("✅ Empleado actualizado correctamente.")

                st.rerun()

           except ValueError as e:
                 st.error(f"⚠️ {e}")

 # Opción eliminar

 elif opcion == "Eliminar empleado":

   st.header("🗑️ Eliminar empleado")

   if len(st.session_state.empleados) == 0:

       st.info("ℹ️ No hay empleados registrados para eliminar.")

   else:
       
       opciones_empleados = {
                f"ID {registro['id']} - "
                f"{registro['empleado'].nombre}": registro["id"]
                for registro in st.session_state.empleados
            }

            empleado_seleccionado = st.selectbox(
                "Seleccione el empleado:",
                list(opciones_empleados.keys())
            )

            id_eliminar = opciones_empleados[
                empleado_seleccionado
            ]

            # Obtener nombre para mostrar el mensaje
            registro_eliminar = next(
                registro
                for registro in st.session_state.empleados
                if registro["id"] == id_eliminar
            )

            nombre_eliminar = (
                registro_eliminar["empleado"].nombre
            )

            if st.button("🗑️ Eliminar empleado"):

                st.session_state.empleados = [
                    registro
                    for registro in st.session_state.empleados
                    if registro["id"] != id_eliminar
                ]

                st.success(
                    f"✅ El empleado {nombre_eliminar} "
                    "fue eliminado correctamente."
                )

                st.rerun()

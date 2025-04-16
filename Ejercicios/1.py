

curso_actual = 1.5
curso_minimo_otros = 2.5
curso_maximo = 7.0
tiempo_promedio = 4.0

porcentaje_curso_actual = (curso_actual * 100) / curso_maximo
print(porcentaje_curso_actual)

porcentaje_curso_lento = (curso_minimo_otros * 100) / curso_maximo
print(porcentaje_curso_lento)

diferencia_actual_promedio = (tiempo_promedio * 100) / curso_maximo
# Declarar los personajes
define e = Character("Ellie", image="Ellie_neutral")
define l = Character("Lucy", image="Lucy_neutral")
define h = Character("Henry")
define c = Character("?")

# Variable para guardar las decisiones
default tomar_foto = False
default camino = False
default puerta = False
default cap2_decisiones = True
default termina_investigacion_cuarto = 0

# Declarar las imágenes de los personajes
image Ellie_neutral = im.Scale("Ellie.png", 350, 650) # Declara el tamaño de las imágenes, 350=ancho(x), 650=largo(y)
image Lucy_neutral = im.Scale("Lucy.png", 350, 700)
image muneca = im.Scale("muñeca.png", 400, 200)

# Declaración de las imágenes de fondo
image bg Henry_1 = im.Scale("Henry_1.png", 1280, 720) # Declara la resolución de los fondos
image bg fondo_bosque = im.Scale("fondo_bosque.png", 1450, 800)
image bg Henry_2 = im.Scale("Henry2.png", 1280, 720)
image bg bosque_intro = im.Scale("bosque_intro.png", 1280, 720)
image bg oficina = im.Scale("oficina.jpeg", 1280, 720)
image bg auto1 = im.Scale("auto1.jpeg", 1280, 720)
image bg sendero2caminos = im.Scale("sendero2caminos.jpeg", 1280, 720)
image bg sendero_izquierdo_velas = im.Scale("sendero_izquierdo_velas.jpeg", 1280, 720)
image bg sendero_derecho_munecas = im.Scale("sendero_derecho_munecas.jpeg", 1280, 720)
image bg muneca_piso = im.Scale("muñeca_piso.png", 1280, 720)
image bg ritual_velas = im.Scale("ritual.jpeg", 1280, 720)
image bg casa_tenebrosa_exterior = im.Scale("casa_afuera.jpeg", 1280, 720)
image bg ritual_velas_apagadas = im.Scale("ritual_apagado.jpg", 1280, 720)
image bg cuarto_ellie = im.Scale("cuarto_ellie.jpeg", 1280, 720)
image bg ellie_sentada_cama = im.Scale("ellie_sentada_cama.jpeg", 1280, 720)
image bg ellie_despertando = im.Scale("ellie_despertando.jpeg", 1280, 720)
image bg coleccionista_mesa = im.Scale("coleccionista_mesa.jpeg", 1280, 720)
image bg coleccionista_entrando = im.Scale("coleccionista_entrando.jpeg", 1280, 720)
image bg ventana_cuarto = im.Scale("Ventana_cuarto.jpeg", 1280, 720) 
image bg puerta_entreabierta = im.Scale("puerta_entreabierta.jpg", 1280, 720) 
image bg mesita_de_luz = im.Scale("mesita_de_luz.jpeg", 1280, 720) 
image bg ellie_balcon = im.Scale("ellie_balcon.jpeg", 1280, 820)
image bg ellie_balcon_sum = im.Scale("ellie_balcon_sum.jpeg", 1280, 720) 
image bg puerta_derecha_carta1 = im.Scale("puerta_derecha_carta1.jpeg", 1280, 720) 
image bg puerta_izquierda_muneca1 = im.Scale("puerta_izquierda_muneca1.jpeg", 1280, 720) #FALTA IMAGEN de la puerta izquierda
image bg puerta_derecha_carta2 = im.Scale("puerta_derecha_carta2.jpeg", 1280, 720) 
image bg puerta_izquierda_muneca2 = im.Scale("puerta_izquierda_muneca2.jpeg", 1280, 720) #FALTA IMAGEN de dentro de la habitacion izq (la muñeca tiene el codigo
image bg ellie_bajando_escaleras = im.Scale("ellie_bajando_escaleras.jpeg", 1280, 720) #F
image bg ellie_viendo_mesa = im.Scale("ellie_viendo_mesa.jpeg", 1280, 720) 
image bg mesa = im.Scale("mesa.jpeg", 1280, 720) 

image bg ventanas = im.Scale("puertas.jpeg", 1280, 720) 
image bg puertas = im.Scale("puertas.jpeg", 1580, 720)

image bg puerta_derecha_abriendo = im.Scale("puerta_derecha_abriendo.jpeg", 1280, 720)
image bg puerta_izquierda_abriendo = im.Scale("puerta_izquierda_abriendo.jpeg", 1280, 720)
image bg puerta_derecha = im.Scale("puerta_derecha.jpeg", 1280, 720)
image bg puerta_izquierda = im.Scale("puerta_izquierda.jpeg", 1280, 720)
image bg puerta_derecha2 = im.Scale("puerta_derecha2.jpeg", 1280, 720)
image bg puerta_izquierda2 = im.Scale("puerta_izquierda22.jpg", 1280, 720)

image foto = im.Scale("foto.png", 400, 600)
image bg nota = im.Scale("nota.jpeg", 1280, 720)
image bg ellie_sentada = im.Scale("ellie_sentada.jpeg", 1280, 720)
image bg coleccionista = im.Scale("coleccionista.jpeg", 1280, 720)
image bg caja_fuerte_abierta = im.Scale("caja_fuerte_abierta.jpeg", 1280, 720)



# Declaración de sonidos personalizados
define sonido_afuera = "audio/sonido_afuera.mp3"
define puerta_auto = "audio/puerta_auto.mp3"
define sonido_tomar_foto = "audio/tomar_foto.mp3"
define viento = "audio/viento_fuerte.mp3"
define musica_inicio = "audio/inicio_miedo.mp3"
define oficina = "audio/office.mp3"
define cerrar_puertas = "audio/cerrar_puerta.mp3"
define despacho = "audio/despacho_henry.mp3"
define sendero_izquierdo_musica = "audio/sendero_izquiero_musica.mp3"
define sendero_der_musica = "audio/sendero_derecho_musica.mp3"

define puerta_abriendo = "audio/puerta_abriendo.mp3"
define cuarto_vacio = "audio/cuarto_vacio.mp3"
define cama_rechinar = "audio/cama_rechinar.mp3"
define abrir_cajon = "audio/abrir_cajon.mp3"

# Transición personalizada: disuelve la imagen en 3 segundos
define fundido_lento = Dissolve(3.0) 

label start: #Eleccion de capitulos

label cap1: # Empieza el juego

    jump capitulo2

    # muestra un fondo negro con el prólogo
    scene black #fondo negro
    window hide # Oculta la caja de texto
    #centra el texto, size=el tamaño del texto, "i" es la tipografia del texto, en este caso, tipo cursiva y se pone al inicio del texto y al finlal se cierra con /
    play music musica_inicio
    scene bg bosque_intro with fade
    show expression Solid("#00000080") as sombra
   
    centered """
    {size=20}{i}Durante años, varios jóvenes desaparecieron en el bosque cerca de las montañas...{/i}{/size}


    {size=20}{i}En las búsquedas, nunca se encontraron cuerpos ni sospechosos...{/i}{/size}
    """
    centered """
    {size=20}{i}Con el tiempo, el caso terminó convirtiéndose en una leyenda urbana.{/i}{/size}"""


    centered "{size=20}{i}Pero todo cambió con una nueva desaparición, donde se le asigna a Ellie Carter investigar el bosque y hallar un responsable...,{/i}{/size}"
    centered "{size=20}{i}antes de que alguien más...,{/i}{/size} "
    centered "{size=20}{i}Desaparezca.,{/i}{/size}"
    stop music fadeout 5.0

    scene black
    centered """
    {size=70}{b}CAPITULO 1:{/b}{/size}

    {size=130}{i}{b}La mision sin rastros{/b}{/i}{/size}
   
    """
    play music oficina fadein 2.0

    scene bg oficina with fade

    centered """
    {size=20}{i}Ellie está trabajando tranquilamente en unos informes, cuando de repente la llama su jefe a su oficina{/i}{/size}


    {size=50}{i}¡CARTER. Mové el culo y vení para acá!{/i}{/size}


    {size=20}{i}El despacho de Henry es oscuro, persianas bajas, una única luz cálida ilumina el cuarto, el humo y la mala vibra son visibles a simple vista.{/i}{/size}
   
    {size=20}{i}Ellie va para la oficina...{/i}{/size}
    """

    window show # Muestra la caja de texto

    scene bg Henry_1 with fundido_lento #aparece henry en su oficina de fondo

    e "Sí, jefe?"

    h "¿Cuántas veces tengo que decirte que cierres la maldita puerta?"
    play sound cerrar_puertas
    stop music fadeout 4.0

    scene bg Henry_2 with fade

    play music despacho fadein 2.0

    e "¿Qué pasó jefe?"

    h "Estamos jodidos... "

    h "después de 2 años, hubo otra desaparición en ese bosque... "

    h "ese maldito bosque que la gente dice que está embrujado..."

    h "puras estupideces"

    h "Encima ya se hizo público, la prensa está encima mío buscando respuestas."

    h "Necesito urgente una solución, y como sabrás, la detective Lucy está en una misión bastante lejana..."

    h "No me queda de otra que mandarte..."

    e "¿A mí?"

    h "Sí, a vos."

    h "Andate ya, en tu escritorio van a estar los datos del caso y las llaves del auto."

    h "No te mandes ninguna cagada..."

    stop music fadeout 2.0

    play music oficina fadein 2.0

    scene bg oficina with fade

    show Ellie_neutral at center with moveinleft

    e "No lo puedo creer, mi primer caso sola..."

    e "Y es muy importante, Lucy ya me había contado de esto mientras hacía mis prácticas con ella."

    e "Será mejor no atrasarme más, ya está oscureciendo..."

    scene black with fade
    centered """
    {size=20}{i}Ellie, apurada y un tanto nerviosa, agarra sus cosas, sube al auto y va directo al lugar de investigación.{/i}{/size}
    """
    stop music fadeout 2.0

    window hide # Oculta la caja de texto

    scene bg auto1 with fade

    #M:falta el chat con Lucy (la imagen) y tambien una imagen donde se pueda ver en un costado partes de muñeca
    #creo que es mejor hacer que llegue al lugar primero y que vea las partes de muñeca cuando baje del auto
    #asi ahi le da la opcion al jugador de mandarselo a Lucy o no
    #j:de una melany, me encanto la idea jojojo
    
    play music sonido_afuera

    centered "{size=20}{i}En el camino, Ellie se sentía muy incómoda...{/i}{/size}"

    centered "{size=20}{i}Incapaz de recordar bien lo que había aprendido en sus prácticas.{/i}{/size}"

    centered "{size=20}{i}Después de dos horas conduciendo, llegó a su destino:{/i}{/size}"

    centered "{size=20}{i}Las entradas del bosque...{/i}{/size}"

    centered "{size=20}{i}Donde había sido visto por última vez el desaparecido.{/i}{/size}"

    play sound puerta_auto

    centered "{size=20}{i}Pero al bajar del auto...{/i}{/size}"

    centered "{size=20}{i}Se encontró con algo que la dejó desconcertada...{/i}{/size}"

    scene bg muneca_piso with fundido_lento

    pause 1.0

    e "una muñeca?"

    e "parece como si me estuviera esperando..."

    #foto de la muñeca en el piso
    #opcion para que el jugador elija si mandarle foto a Lucy o no
    window hide # Oculta la caja de texto

    menu:

        "Deberia sacarle una foto?":
            $ tomar_foto = True
            play sound sonido_tomar_foto

            e "Creo que podria servir para la investigación..."

            "Ellie manda la foto a Lucy"

            e "Deberia seguir investigando, aunque..."

            e "Esto me da muy mala espina."

        "Qué extraño...debería seguir investigando":
            $ tomar_foto = False

            e "Este bosque me pone los pelos de punta, no entiendo como Lucy quiso retomar este caso."

            e "No voy a dejar que mis nervios me ganen."

            e "Voy a seguir investigando por mi cuenta."

    # Fundido a negro
    scene bg fondo_bosque with fade
    show Ellie_neutral at center with moveinright
    e "Ya llevo mucho tiempo caminando..."
    e "no estoy segura si debería volver"
    e "pero no puedo fallar en mi primera misión oficial, tengo que seguir"

    hide Ellie_neutral
    scene black with fade
  
    centered "{size=20}{i}Después de caminar bastante...{/i}{/size}"
    play sound viento
    centered "{size=20}{i}El viento sopló como nunca, moviendo con brutalidad ramas y hojas{/i}{/size}"
    centered "{size=20}{i}Revelando así unos carteles que antes estaban escondidos.{/i}{/size}"
    centered "{size=20}{i}Estos carteles señalaban caminos lejanos en direcciones contrarias...{/i}{/size}"

    scene bg sendero2caminos with fade
    #show Ellie_neutral at center

    e "Qué?"
    e "como es que nunca habían visto esto antes?"
    e "Qué... raro"
    e "Uno se ve extrañamente iluminado"
    e "Mientras que otro tiene una oscuridad sombría"
    "por donde debería ir?"

    menu:

        "Debería ir a la Izquierda?":
            e "Creo que debería ir por el camino más iluminado, tal vez pueda encontrar cosas que sirvan para la investigación"
            scene black with Dissolve(3.0)
            jump sendero_izquierdo

        "o a la derecha?":
            e "Creo que debería ir por el camino más oscuro, tal vez pueda encontrar cosas que sirvan para la investigación"
            scene black with Dissolve(3.0)
            jump sendero_derecho

label sendero_izquierdo:
    $ camino = True 
    stop music fadeout 2.5
    play music sendero_izquierdo_musica fadein 1.5

    scene bg sendero_izquierdo_velas with fade
    show Ellie_neutral at center

    e "..."

    e "Cada vez hay menos luz..."

    e "Ya casi no distingo el camino."

    hide Ellie_neutral

    centered "{size=20}{i}Ellie avanzó con pasos pequeños, intentando no pisar las ramás secas que crujían bajo sus botas.{/i}{/size}"

    show Ellie_neutral at center

    e "Estas velas... siguen encendidas."

    e "Eso no me gusta nada."

    hide Ellie_neutral

    centered "{size=20}{i}La débil luz de las llamás apenas alcanzaba a romper la oscuridad entre los árboles.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "¿Quién vendría hasta acá a hacer esto?"

    e "No... no quiero pensar en eso."

    hide Ellie_neutral

    centered "{size=20}{i}El viento comenzó a deslizarse entre las ramás con un murmullo bajo y constante.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "Hay algo más adelante."

    hide Ellie_neutral

    centered "{size=20}{i}Ellie siguió caminando, cada vez más despacio, hasta llegar a un pequeño claro oculto entre los árboles.{/i}{/size}"

    scene bg ritual_velas with dissolve
    show Ellie_neutral at center

    centered "{size=20}{i}En el centro del claro había un círculo marcado en el suelo.{/i}{/size}"

    centered "{size=20}{i}Alrededor, varias velas seguían encendidas, temblando con una luz débil y amarillenta.{/i}{/size}"

    centered "{size=20}{i}Pedazos de muñecas estaban esparcidos entre la tierra húmeda, como si hubieran sido dejados allí a propósito.{/i}{/size}"

    e "..."

    e "Pedazos de muñecas..."

    e "Y ese círculo..."

    e "¿Eso es sangre?"

    hide Ellie_neutral

    centered "{size=20}{i}Ellie tragó saliva. El aire parecía haberse vuelto más pesado de golpe.{/i}{/size}"

    show Ellie_neutral at center

    e "No debería tocar nada..."

    e "Pero esto sí parece importante."

    hide Ellie_neutral

    centered "{size=20}{i}Se acercó un poco más, inclinando apenas la cabeza para mirar mejor el suelo.{/i}{/size}"

    show Ellie_neutral at center

    e "¿Un ritual...?"

    e "No, no... tal vez solo sea una broma horrible..."

    e "..."

    e "Ni en pedo."

    hide Ellie_neutral

    centered "{size=20}{i}Una ráfaga de viento cruzó el claro con fuerza, agitándose entre los árboles como un suspiro violento.{/i}{/size}"

    play sound "audio/viento_fuerte.mp3"
    with hpunch

    show Ellie_neutral at center

    e "!"

    e "..."

    e "¿Qué fue eso?"

    hide Ellie_neutral

    centered "{size=20}{i}Ellie levantó la vista de inmediato, apretando la linterna con más fuerza.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "No hay nadie."

    e "O... no debería haber."

    hide Ellie_neutral

    centered "{size=20}{i}El sonido del viento creció y las llamás de las velas comenzaron a inclinarse al mismo tiempo.{/i}{/size}"

    play sound "audio/viento_fuerte.mp3"
    with vpunch

    show Ellie_neutral at center

    e "¡Ah!"

    e "Esto no está bien..."

    hide Ellie_neutral

    centered "{size=20}{i}Algo se movió entre los árboles. No lo suficiente para verse con claridad, pero sí lo bastante para hacerla retroceder un paso.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "¿Hay alguien ahí?"

    hide Ellie_neutral

    centered "{size=20}{i}No hubo respuesta. Solo ramás crujiendo y el viento arrastrándose por el claro.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "No... no, no."

    e "Estoy imaginando cosas."

    hide Ellie_neutral

    centered "{size=20}{i}Ellie giró apenas sobre sí misma, intentando ubicar de dónde había venido aquel movimiento.{/i}{/size}"

    show expression Solid("#00000020") as sombra with dissolve

    hide Ellie_neutral

    centered "{size=20}{i}Las velas siguieron temblando, pero ahora parecían iluminar menos. Mucho menos.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "¿Por qué siento que..."

    e "No."

    e "Nada."

    hide Ellie_neutral

    centered "{size=20}{i}El bosque respondió con un silencio repentino, demásiado limpio, demásiado tenso.{/i}{/size}"

    play sound "audio/viento_fuerte.mp3"
    with vpunch

    show Ellie_neutral at center

    e "¡!"

    hide Ellie_neutral

    centered "{size=20}{i}Todas las velas se apagaron al mismo tiempo.{/i}{/size}"

    stop music fadeout 1.0

    scene black with fade

    pause 0.5

    scene bg ritual_velas_apagadas with fade
    show Ellie_neutral at center

    e "..."

    e "No veo nada..."

    e "..."

    e "¿Hola?"

    hide Ellie_neutral

    centered "{size=20}{i}La oscuridad del claro era casi total. Apenas quedaba una mínima silueta de los árboles alrededor.{/i}{/size}"

    play sound "audio/pasos_lejanos.mp3"

    show Ellie_neutral at center

    e "..."

    e "Escuché algo."

    e "No, no fue nada."

    hide Ellie_neutral

    centered "{size=20}{i}Un ruido seco sonó detrás de ella.{/i}{/size}"

    play sound "audio/rama_ruptura.mp3"

    show Ellie_neutral at center

    e "!"

    e "¿Qué...?"

    hide Ellie_neutral

    centered "{size=20}{i}Ellie se dio la vuelta de golpe, levantando la linterna con manos temblorosas.{/i}{/size}"

    with hpunch
    play sound "audio/golpe.mp3"
    with vpunch

    show Ellie_neutral at center

    e "¡Agh!"

    hide Ellie_neutral

    scene black with vpunch

    centered "{size=30}{i}Todo se volvió negro de inmediato.{/i}{/size}"

    centered "{size=20}{i}Ellie cayó al suelo sin comprender qué había pasado.{/i}{/size}"

    pause 1.5

    jump fin_capitulo


label sendero_derecho:
    $ camino = False
    stop music fadeout 2.5
    play music sendero_derecho_musica fadein 1.5

    scene bg sendero_derecho_munecas with fade
    show Ellie_neutral at center

    e "..."

    e "Hay pedazos de muñecas por todos lados..."

    e "No deberían estar tan repartidos así..."

    hide Ellie_neutral

    centered "{size=20}{i}Ellie siguió caminando con pasos cortos, mirando el suelo cada pocos segundos y luego volviendo a levantar la vista hacia los árboles.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "Cada vez está más oscuro."

    e "Hace un rato todavía se veía algo mejor..."

    hide Ellie_neutral

    centered "{size=20}{i}El sendero parecía extenderse sin terminar nunca, como si el bosque quisiera llevarla cada vez más adentro.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "No me gusta esto."

    e "Nada."

    hide Ellie_neutral

    centered "{size=20}{i}Los fragmentos de muñecas seguían apareciendo entre las hojas y el barro, como pequeñas marcas dejadas en el camino.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "Siento que ya me alejé demasiado."

    e "Pero volver ahora sería peor..."

    hide Ellie_neutral

    centered "{size=20}{i}Ellie apretó los dedos dentro de los guantes, intentando calmarse mientras continuaba avanzando.{/i}{/size}"

    show Ellie_neutral at center

    e "No tengo que ponerme nerviosa..."

    e "Solo tengo que seguir..."

    hide Ellie_neutral

    centered "{size=20}{i}Entonces, entre la niebla, una estructura enorme comenzó a dibujarse al fondo del sendero.{/i}{/size}"

    scene bg casa_tenebrosa_exterior with dissolve
    show Ellie_neutral at center

    e "..."

    e "¿Una casa?"

    e "Es enorme..."

    e "Y está muy vieja..."

    hide Ellie_neutral

    centered "{size=20}{i}La casa parecía abandonada desde hacía años. La madera estaba oscura, las paredes desgastadas, pero habia luz...{/i}{/size}"

    show Ellie_neutral at center

    e "¿Cómo llegó una casa hasta acá?"

    e "No recuerdo que esto apareciera en ningún informe..."

    hide Ellie_neutral

    centered "{size=20}{i}Ellie dio unos pasos más, con cuidado, como si acercarse demásiado pudiera empeorar las cosas.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "Ya está..."

    e "Estoy muy cerca."

    hide Ellie_neutral

    centered "{size=20}{i}Una presión extraña comenzó a crecerle en la cabeza. Al principio fue leve, apenas una molestia.{/i}{/size}"

    show Ellie_neutral at center

    e "Ah..."

    e "¿Qué...?"

    e "Me duele un poco..."

    hide Ellie_neutral

    centered "{size=20}{i}La sensación fue empeorando mientras observaba la casa en silencio.{/i}{/size}"

    show Ellie_neutral at center

    e "No... no me siento bien."

    hide Ellie_neutral

    centered "{size=20}{i}Ellie intentó respirar hondo, pero el aire del bosque parecía más denso que antes.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "Tengo que seguir mirando."

    hide Ellie_neutral

    centered "{size=20}{i}Rodeó la casa con lentitud, sin perder de vista las ventanas rotas del frente.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "¿Hay sombras ahí?"

    e "No..."

    e "Tal vez solo sean las ramás."

    hide Ellie_neutral

    centered "{size=20}{i}Pero cuanto más observaba, más figuras parecía distinguir detrás de los vidrios sucios.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "No puedo estar segura."

    e "Me duele más la cabeza..."

    hide Ellie_neutral

    centered "{size=20}{i}El dolor se volvió más fuerte, como si algo le presionara las sienes desde adentro.{/i}{/size}"

    play sound "audio/zumbido.mp3"

    show Ellie_neutral at center

    e "Ah..."

    e "No, no..."

    e "Tengo que... concentrarme..."

    hide Ellie_neutral

    centered "{size=20}{i}Las sombras comenzaron a moverse de un lado a otro, rodeando la casa y recortándose entre los árboles.{/i}{/size}"

    show Ellie_neutral at center

    e "..."

    e "Eso no estaba ahí antes."

    hide Ellie_neutral

    centered "{size=20}{i}Ellie retrocedió un paso. Después otro.{/i}{/size}"

    show Ellie_neutral at center

    e "..."
    with hpunch
    e "No..."

    e "No estoy bien."

    hide Ellie_neutral

    centered "{size=20}{i}La presión en su cabeza se volvió insoportable.{/i}{/size}"

    play sound "audio/zumbido_fuerte.mp3"
    with hpunch

    show Ellie_neutral at center

    e "¡Ah!"

    hide Ellie_neutral

    centered "{size=20}{i}Las sombras parecían cerrarse a su alrededor, cubriéndolo todo.{/i}{/size}"

    show Ellie_neutral at center
    with hpunch
    e "No puedo ver..."
    with hpunch
    e "No puedo..."

    hide Ellie_neutral

    with hpunch

    centered "{size=20}{i}Ellie intentó sostenerse, pero sus piernas cedieron lentamente.{/i}{/size}"

    scene black with fade

    centered "{size=30}{i}La oscuridad la envolvió por completo.{/i}{/size}"

    centered "{size=20}{i}Ellie perdió el conocimiento frente a la casa.{/i}{/size}"

    pause 1.5

    jump fin_capitulo


label fin_capitulo:

    stop music fadeout 3.0
    scene black with fade

    centered """
    {size=70}{b}FIN DEL CAPÍTULO 1{/b}{/size}

    {size=30}{i}Continuará...{/i}{/size}
    """

    pause 3.0
    scene black with Dissolve(3.0)
    jump capitulo2



label capitulo2:
    centered """
    {size=70}{b}CAPÍTULO 2:{/b}{/size}

    {size=50}{i}{b}La noche aún no acaba...{/b}{/i}{/size}
    """

    play music cuarto_vacio fadein 1.5

    scene bg ellie_despertando with fundido_lento

    centered "{size=20}{i}Ellie se despertó en un cuarto desconocido con una iluminación muy tenue.{/i}{/size}"
    centered "{size=20}{i}Solo había una lampara prendida sobre la mesa de luz.{/i}{/size}"

    play sound cama_rechinar
    scene bg ellie_sentada_cama with fundido_lento

    pause 1.0

    e "Qué…"

    e "¿Dónde estoy?"

    centered "{size=20}{b}Observa el cuarto desconcertada.{/b}{/size}"

    if camino == True:
        e "Lo último que recuerdo es que estaba…"
        e "¿En un ritual en el bosque?"
    else:
        e "Lo último que recuerdo es que estaba…"
        e "¿En las afueras de la mansión abandonada?"

    e "No tengo ninguna pertenencia... Creo que debería ver qué onda con este lugar, re creepy."

    #e "¿Qué debería investigar primero?"

    while termina_investigacion_cuarto != 3:
        menu:
            e "¿Qué debería investigar?"
            ###
            "Investigar la mesa de luz":
                scene bg ellie_sentada_cama
                e "Hay una lamparaS sobre ella, creo que el cajón está abierto."
                e "Debería ver qué hay"
                play sound abrir_cajon
                scene bg mesita_de_luz with fade
                e "No puede ser..."
                e "Esta niña de la foto... soy yo, pero, ¿dónde está la otra mitad?"
                e "Además hay una llave... ¿de qué será? Me la llevo."
                $ termina_investigacion_cuarto += 1 
            ###    
            "Investigar la ventana":
                scene bg ventana_cuarto with fade
                e "Está bloqueada con maderas, apenas puedo ver del otro lado."
                e "Creo estar en lo alto de una mansión."
                e "No creo poder salir por acá, mejor voy a investigar otra manera."
                $ termina_investigacion_cuarto += 1 
            ###
            "Investigar la puerta":
                scene bg puerta_entreabierta with fade
                e "Está entreabierta..."
                e "Qué raro..."
                e "Me da mucho miedo ir, pero necesito investigar."
                $ termina_investigacion_cuarto += 1 
            ###

    centered "{size=20}{b}Ellie termina de investigar el cuarto y sale al balcón.{/b}{/size}"

    scene bg ellie_balcon with fade
    #show Ellie_neutral at center

    e "¿Y esto qué es?"

    e "No veo a nadie cerca."

    e "Pero veo dos puertas... ¿será que puedo usar la llave para alguna de ellas?"

    hide Ellie_neutral
    scene bg puertas with fade

    menu:
        "Abrir la puerta derecha":
            jump puerta_derecha

        "Abrir la puerta izquierda":
            jump puerta_izquierda


label puerta_derecha:
    $ puerta = True

    play sound puerta_abriendo
    scene bg puerta_derecha_abriendo with fade

    e "Mi intuición me dice que esta es la correcta."

    scene bg puerta_derecha with fade

    e "Pero qué son todas estas muñecas tan horribles..."

    e "Esa muñeca de la cama... tiene algo."

    scene bg puerta_derecha2 with fade

    e "¿Es una carta?"

    scene black with Dissolve(2.0)

    centered "{size=20}{b}Ellie abre la carta y lee:{/b}{/size}"

    centered "{size=20}{b}Mi querida Ellie...{/b}{/size}"

    centered "{size=20}{b}Si estás leyendo esto, significa que finalmente llegaste hasta aquí.{/b}{/size}"

    centered "{size=20}{b}Todavía recuerdo aquel día como si hubiera ocurrido ayer.{/b}{/size}"

    centered "{size=20}{b}Dos números iguales marcaron el calendario...{/b}{/size}"

    centered "{size=20}{b}Y otros dos iguales volvieron a repetirse justo después.{/b}{/size}"

    centered "{size=20}{b}Fue entonces cuando nuestra pequeña familia dejó de ser la misma.{/b}{/size}"

    centered "{size=20}{b}El día en que UNA niña se nos unio...11/11{/b}{/size}"

    centered "{size=20}{b}Tu hermanita llegó a nosotros.{/b}{/size}"

    centered "{size=20}{b}Hay recuerdos que jamás deberían olvidarse.{/b}{/size}"


    scene bg puerta_derecha2 with fade

    e "¿Qué...?"

    e "No lo puedo creer..."

    e "El psicópata que me trajo hasta acá..."

    e "tiene que ver con la muerte de mi hermana..."

    e "Lo voy a matar."

    e "Encima la llave de mierda se rompió."

    e "Que cagada"

    e "Ahora no puedo ver la otra habitación."

    e "No puedo dejar que esto siga asi..."

    e "tengo que seguir investigando y de alguna forma salir de aca."    

    jump capitulo2_mesa

label puerta_izquierda:
    e "Mi intuición me dice que esta es la correcta."
    jump puerta_izquierdaz

label puerta_izquierdaz:
    $ puerta = False

    play sound puerta_abriendo
    scene bg puerta_izquierda_abriendo with fade

    e "Espero no equivocarme."

    scene bg puerta_izquierda with fade

    e "Pero qué son todas estas muñecas tan horribles..."

    e "Esa muñeca de la cama... tiene algo escrito."

    scene bg puerta_izquierda2 with fade

    e "¿Es un número?"

    e "Pero... ¿por qué es la fecha en la que ella..."
    
    e "Briana."
    
    e "Por qué es la fecha en la que Briana murió?"

    e "Mi hermana... ¿quién está detrás de todo esto?"

    e "Lo voy a hacer pagar."

    e "Encima la llave de mierda se rompió."

    e "Ahora no puedo ver la otra habitación."

    jump capitulo2_mesa


label capitulo2_mesa:
    centered "{size=20}{b}Tras investigar la habitacion, Ellie vuelve al balcón y mira el salón principal desde arriba.{/b}{/size}"

    scene bg ellie_balcon_sum with fade

    e "¿Por qué hay una mesa ahí abajo?"

    e "¿Esas de ahí son... personas?"

    e "No... no pueden ser."

    e "¿Acaso son muñecas?"

    scene bg ellie_bajando_escaleras with fade

    e "No..."

    e "Tengo que bajar."

    scene bg ellie_viendo_mesa with fade

    e "Qué asco..."

    e "Todas se ven..."
    
    e "Extrañamente igual que ella."

    e "Briana, estaras aqui?"

    e "Rezo todos los dias para que aquella caida de las montañas..."

    e "No te haya matado."

    "En ese momento emotivo, ellie ve algo que le llama la atencion"

    scene bg mesa with fade

    e "Eso es una caja fuerte..."

    e "Necesita un código de 4 dígitos..."

    e "No me digas que va a ser..."

    jump caja_fuerte


label caja_fuerte:
    $ codigo = renpy.input("Código de 4 dígitos:", length=4)
    $ codigo = codigo.strip() 

    if not codigo.isdigit():
        e "Solo puedo introducir números."
        jump caja_fuerte

    elif codigo == "1111":
        e "Es la fecha en la que mi hermana..."
        e "*llora*"

        scene bg caja_fuerte_abierta with fade

        e "Esto es... la otra mitad de la foto de la mesita de luz."

        show foto


        e "Es... ¡es mi hermanita!"

        e "No lo puedo creer..."

        e "Ni siquiera me acordaba de que así se veía..."

        e "Hay algo más en la caja fuerte... ¿qué es?"

        e "es una nota. Quiero saber quién está detrás de todo esto..."

        "De pronto, el sonido de una campana rompió el silencio."

        "Desde la mesa principal, una voz que Ellie conocía demasiado bien susurró:"

        "Ven a comer..."

        "No dejes que se enfríe."

        jump ver_coleccionista

    else:
        e "Me equivoqué..."
        e "Capaz el código estaba en la habitación que investigué."
        jump caja_fuerte

label ver_coleccionista:
    
    scene bg ellie_sentada with fade

    e "Esa voz..."

    e "Hace tiempo no escuchaba algo asi."

    e "No será-"

    centered "{size=20}{b}Antes de que Ellie termine la frase, las puertas del salon principal se abrieron de par en par...{/b}{/size}"
    scene bg coleccionista_entrando with fade
    centered "{size=20}{b}pero ahora...{/b}{/size}"
    centered "{size=20}{b}había alguien más en la mesa con Ellie...{/b}{/size}"
    scene bg coleccionista_mesa with fade

    "..."

    c "Tanto tiempo..."

    c "ELLie..."

    c "Nuestro plan está por empezar..."

    window hide 

    centered "{size=80}{b}EL COLECCIONISTA{/b}{/size}"

    scene black with Dissolve(3.0)
    jump final_capitulo2

label final_capitulo2:
    centered "{size=20}{b}Ellie se quedó completamente paralizada.{/b}{/size}"
    centered "{size=20}{b}No pudo mover ni un músculo...{/b}{/size}"

    
    centered "{size=80}{b}EL COLECCIONISTA SIGUE ATORMENTANDO MUÑECAS...{/b}{/size}"

    scene black with Dissolve(3.0)
    return

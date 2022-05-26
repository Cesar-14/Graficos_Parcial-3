import OpenGL.GL as gl
import glfw
import numpy as np
from Shader import *
from Modelo import *
from Jugador import Jugador
from Fondo import Fondo
from Enemigos import *
from Ganar import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

fondo = None
modelo = None
enemigo = None
enemigo2 = None
enemigo3 = None
enemigo4 = None
enemigo5 = None
ganar = None
window = None

tiempo_anterior = 0.0

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def actualizar():
    global tiempo_anterior
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    global window
    estado_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    if estado_arriba == glfw.PRESS:
        modelo.mover(modelo.ARRIBA, tiempo_delta)
    if estado_abajo == glfw.PRESS:
        modelo.mover(modelo.ABAJO, tiempo_delta)
    if estado_derecha == glfw.PRESS:
        modelo.mover(modelo.DERECHA, tiempo_delta)
    if estado_izquierda == glfw.PRESS:
        modelo.mover(modelo.IZQUIERDA, tiempo_delta)

    enemigo.actualizar(tiempo_delta)
    enemigo2.actualizar(tiempo_delta)
    enemigo3.actualizar(tiempo_delta)
    enemigo4.actualizar(tiempo_delta)
    enemigo5.actualizar(tiempo_delta)
    ganar.actualizar(tiempo_delta)

    
    if modelo.colisionando(enemigo):
        glfw.set_window_should_close(window, 1)

    if modelo.colisionando(enemigo2):
        glfw.set_window_should_close(window, 1)
    
    if modelo.colisionando(enemigo3):
        glfw.set_window_should_close(window, 1)

    if modelo.colisionando(enemigo4):
        glfw.set_window_should_close(window, 1)

    if modelo.colisionando(enemigo5):
        glfw.set_window_should_close(window, 1)

    if modelo.colisionando(ganar):
        glfw.set_window_should_close(window, 1)

    tiempo_anterior = tiempo_actual

def colisionando():
    colisionando = False
    return colisionando
    
def dibujar():
    global modelo
    global fondo
    global enemigo
    global enemigo2
    global enemigo3
    global enemigo4
    global enemigo5
    global ganar

    fondo.dibujar()
    enemigo.dibujar()
    enemigo2.dibujar()
    enemigo3.dibujar()
    enemigo4.dibujar()
    enemigo5.dibujar()
    ganar.dibujar()
    modelo.dibujar()

def main():
    global modelo
    global fondo
    global window
    global enemigo 
    global enemigo2
    global enemigo3
    global enemigo4
    global enemigo5
    global ganar

    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

   
    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")
    color_id = gl.glGetAttribLocation(shader.shader_program, "color")
    
    transformaciones_id = gl.glGetUniformLocation(
            shader.shader_program, "transformations")

    fondo = Fondo(shader,
            posicion_id, color_id, transformaciones_id)

    modelo = Jugador(shader, 
            posicion_id, color_id, transformaciones_id)

    enemigo = Enemigo(shader, posicion_id, color_id, transformaciones_id)

    enemigo2 = Enemigo2(shader, posicion_id, color_id, transformaciones_id)

    enemigo3 = Enemigo3(shader, posicion_id, color_id, transformaciones_id)

    enemigo4 = Enemigo4(shader, posicion_id, color_id, transformaciones_id)

    enemigo5 = Enemigo5(shader, posicion_id, color_id, transformaciones_id)

    ganar = Ganar(shader, posicion_id, color_id, transformaciones_id)


    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(0.6,0.7,1,1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        dibujar()
        actualizar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar memoria
    modelo.borrar()
    fondo.borrar()
    enemigo.borrar()
    enemigo2.borrar()
    enemigo3.borrar()
    enemigo4.borrar()
    enemigo5.borrar()
    ganar.borrar()
    shader.borrar()

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()


import math
from Modelo import *
import glm

class Jugador(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05
        self.velocidad = 0.4
        self.posicion = glm.vec3(-0.65,0.58,0.0)
        self.vertices = np.array(
            [
                0.055, 0.125,0,1.0,   1,0,0,1.0, 
                -0.055, 0.125,0,1.0,  1,0,0,1.0,  
                0.055, 0.01,0,1.0,    1,0,0,1.0,
                -0.055, 0.01,0,1.0,   1,0,0,1.0
            ], dtype="float32"
        )


        #crear una matriz identidad
        super().__init__(shader, posicion_id, color_id, transformaciones_id)
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    def mover(self, direccion, tiempo_delta):
        cantidad_movimiento = self.velocidad * tiempo_delta
        if direccion == self.ARRIBA:
           self.posicion.y  = self.posicion.y + cantidad_movimiento
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - cantidad_movimiento
        elif direccion == self.DERECHA:
            self.posicion.x = self.posicion.x + cantidad_movimiento       
        elif direccion == self.IZQUIERDA:
            self.posicion.x = self.posicion.x - cantidad_movimiento
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)
        
        
        if self.posicion.x > 1.05: 
            self.posicion.x = -1.0
        if self.posicion.x < -1.05: 
            self.posicion.x = 1.0
            
        if self.posicion.y > 1.05: 
            self.posicion.y = -1.0   
        if self.posicion.y < -1.05: 
            self.posicion.y = 1.0  

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id, 1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()


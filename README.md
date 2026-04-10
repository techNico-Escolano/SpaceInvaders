# Space Invaders
# 👾 SPACE INVADERS - Python Game

¡Bienvenido a **SPACE INVADERS 👽**! Este proyecto es un divertido clon del clásico juego de arcade *Space Invaders*, desarrollado completamente en **Python** utilizando la librería **Pygame**. 

Es un proyecto ideal para demostrar conceptos fundamentales de la programación de videojuegos en 2D.

## ✨ Características Principales

* **Bucle de Juego (Game Loop):** Funciona a unos estables 60 FPS (Frames Per Second).
* **Mecánicas Clásicas:** * Movimiento lateral fluido de la nave espacial usando las flechas del teclado.
  * Sistema de disparo único (una bala activa a la vez en pantalla).
* **Enemigos Dinámicos:** Los aliens se mueven de lado a lado y descienden progresivamente al tocar los bordes de la pantalla.
* **Detección de Colisiones:** El juego utiliza `pygame.Rect` para calcular impactos precisos entre el láser y los enemigos, reapareciéndolos mágicamente al ser destruidos.
* **Sistema de Puntuación:** Un marcador en tiempo real en la esquina superior izquierda que registra cada alienígena eliminado.

## 🛠️ Requisitos del Sistema

Para ejecutar este juego, necesitas:
* **Python 3.x** instalado en tu sistema.
* La librería **Pygame**.

## 🚀 Instalación y Ejecución

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/tu-repositorio-space-invaders.git](https://github.com/tu-usuario/tu-repositorio-space-invaders.git)
   cd tu-repositorio-space-invaders

package com.acalio;

public class Ejercicio1 {

    public static void main(String[] args) {
        suma(20, 40, 60);

        Coche miCoche = new Coche();
        miCoche.sumarPuertas();
        System.out.println("El número de puertas es: " + miCoche.numeroDePuertas);

    }

    public static void suma(int a, int b, int c){
        int resultado;
        resultado = a + b + c;
        System.out.println(resultado);
    }
}

class Coche {
    public int numeroDePuertas = 4;

    public void sumarPuertas(){
        this.numeroDePuertas++;
    }
}

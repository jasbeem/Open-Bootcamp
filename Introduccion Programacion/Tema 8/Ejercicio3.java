package com.acalio;

public class Ejercicio3 {

    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setNombre("Jose");
        System.out.println("Mi nombre es " + persona.getNombre());
        persona.setEdad(20);
        System.out.println("Tengo " + persona.getEdad() + " años");
        persona.setTelefono("658788788");
        System.out.println("Mi teléfono es " + persona.getTelefono());
    }
}

class Persona {
    private String nombre;
    private int edad;
    private String telefono;

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return nombre;
    }

    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad() {
        return edad;
    }

    public void setTelefono(String telefono){
        this.telefono = telefono;
    }
    public String getTelefono() {
        return telefono;
    }
}
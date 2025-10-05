/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clases;

import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 *
 * @author Luna Caes
 */
public class Usuarios {
    
    private final Conector con;
    
    public Usuarios(){
        con = new Conector();
    }
    
    public void insertarUsuarios(String nombre, String apellido, String email, String username, String clave, String rol) throws SQLException{
        
        String sql = "INSERT INTP usuarios (nombre, apellido, email, username, clave, rol) VALUES (?,?,?,?,?,?)";
        
       try(PreparedStatement ps = con.prepararStatement(sql)){
        ps.setString(1, nombre);
        ps.setString(2, apellido);
        ps.setString(3, email);
        ps.setString(4, username);
        ps.setString(5, clave);
        ps.setString(6, rol);
        ps.execute();
        
        System.out.println("Usuarios registrado exitosamente");
    } catch(SQLException e){
        System.out.println("Error al insertar usuario");
    } finally{
           con.desconectar();
       }
}
}

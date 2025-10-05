/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Clases;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


/**
 *
 * @author Luna Caes
 */
public class Conector {
    
 private static final String URL = "jdbc:mysql://127.0.0.1:3307/tecnar_app";
    private static final String USER = "root";
    private static final String PASSWORD = "";
    
    private Connection conexion;
    
    public Connection conectar(){
    
        try{
            conexion = DriverManager.getConnection(URL,USER,PASSWORD);
            System.out.println("Correcta Conexion");
            
        }catch(SQLException e){
            System.out.println("Error en la conexion: " +e.getMessage());
        }
        return conexion;
    }
    
    public PreparedStatement prepararStatement(String sql) throws SQLException{
        
        Connection conn = conectar();
        return conn.prepareStatement(sql);
    }

    
    public ResultSet ejecutarConsulta(PreparedStatement ps) throws SQLException{
        return ps.executeQuery();
    
    }

    public int ejecutarUpdate(PreparedStatement ps) throws SQLException{
        return ps.executeUpdate();
    }
    
    public void desconectar(){
        try{
            if(conexion !=null && !conexion.isClosed()){
                conexion.close();
                System.out.println("Cierre de Conexion");
            }
        }catch(SQLException e){
            System.out.println("Error al desconectar"+ e.getMessage());
        }
    }
}

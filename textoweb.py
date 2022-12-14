myHTML = """

<!DOCTYPE html>
<html lang="es">
<head>
    <!-- <meta content="text/html" charset="UTF-8"> -->
    {{ mm }}
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estadillo diario</title>
    <link rel="stylesheet" href="style.css">
</head>
<!-- <body style="text-align:center;"> -->
    <body style="font-size: 12px;">
    <header>
        <div style="text-align:right; font-size: 14px">
            <img src="{{ imagen }}" alt="Escudo" width="60" height="60">
            <h3>Estadillo diario {{ fecha }}</h3>
        </div>
    </header>
    <!-- Tablas de situación -->
    <div class="grid-container1">
        <div class="content grid-item1" style="text-align: center;">
            <div style="text-align: center; background-color: rgb(189, 189, 196); width: 39.7vw; ">SITUACIÓN PERSONAL</div>
            <div class="fila">
                <table border="1">
                   
                    <thead>
                        <tr>
                            <th>Situacion</th>
                            <th>Cantidad</th>                  
                        </tr>
                    </thead>
                    <tbody>
                        <tr><th>POLICIAS</th></tr>
                        {% for key, value in listado_personal['Policias'].items() %}
                            <tr>
                                <td>{{ key }}</td>
                                <td>{{ value }}</td>
                            </tr>
                        
                        {% endfor %} 
                    </tbody>
                </table>
                <table border="1">
                    
                    <thead>
                        <tr>
                            <th>Situacion</th>
                            <th>Cantidad</th>                  
                        </tr>
                    </thead>
                    <tbody>
                        <tr><th>OFICIALES</th></tr>
                        {% for key, value in listado_personal['Oficial'].items() %}
                            <tr>
                                <td>{{ key }}</td>
                                <td>{{ value }}</td>
                            </tr>
                        
                        {% endfor %}     
                    </tbody>
                </table>
            </div>
        </div>
    
        <!-- Tabla Plantilla -->
        <div class="content grid-item2">   
            <div style="text-align: center; background-color: rgb(189, 189, 196); width: 19.2vw; ">PLANTILLA</div>  
            <table border="1" style="text-align:center">
                
                <thead>
                    <tr>
                        <th>Cargo</th>
                        <th>N&uacute;mero</th>                
                    </tr>
                </thead>
                <tbody>
                    
                        <tr>
                            <td>&nbsp;Polic&iacute;a/s&nbsp;</td>
                            <td>{{ personal[0] }}</td>
                        </tr>
                        <tr>
                            <td>&nbsp;Oficial/es&nbsp;</td>
                            <td>{{ personal[1] }}</td>                   
                        </tr>
                        <tr>
                            <td>&nbsp;Subinspector/es&nbsp;</td>
                            <td>{{ personal[2] }}</td>
                        </tr>
                        <tr>
                            <td>&nbsp;Inspector/es&nbsp;</td>
                            <td>{{ personal[3] }}</td>                   
                        </tr>
                        <tr>
                            <td>&nbsp;Intendente&nbsp;</td>
                            <td>{{ personal[4] }}</td>
                        </tr>                
                </tbody>        
            </table>       
        </div>
    </div>

    <div class="grid-container2">
        
        
        <div class="columna-2">

            <div class="bajas grid-item-d1" style="margin-top:3vh; text-align:center;">
                <table>
                    <caption>AGENTES DE BAJA</caption>
                    <thead>
                        <tr>
                            <th>Numero profesional</th>
                            <th>Fecha desde</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for baja in bajas %}
                            <tr>
                                <td>{{ baja[0] }}</td>
                                <td>{{ baja[1] }}</td>
                            </tr>
                        {% endfor%}
                    </tbody>
                </table>
            </div>
            
            <div class="ayto" style="margin-top:3vh; text-align:center;">
                <table>
                    <caption>DENUNCIAS</caption>
                    <thead>
                        <tr>
                            <th>AYUNTAMIENTO</th>
                            <th>Cantidad</th>
                        </tr>                
                    </thead>
                    <tbody>                
                        <tr>
                            <td>{{ ayto[0][0] }}</td>
                            <td>{{ ayto[0][1] }}</td>
                        </tr>               
                    </tbody>
                    <thead>
                        <tr>
                            <th>JPT</th>
                            <th>Cantidad</th>
                        </tr>                
                    </thead>
                    <tbody>                
                        <tr>
                            <td>{{ jpt[0][0] }}</td>
                            <td>{{ jpt[0][1] }}</td>
                        </tr>               
                    </tbody>
                    
                    <thead>
                        <tr>
                            <th>RADAR</th>
                            <th>Cantidad</th>
                        </tr>                
                    </thead>
                    <tbody>                
                        <tr>
                            <td>{{ radar[0][0] }}</td>
                            <td>{{ radar[0][1] }}</td>
                        </tr>               
                    </tbody>
                    <thead>
                        <tr>
                            <th>CAM</th>
                            <th>Cantidad</th>
                        </tr>                
                    </thead>
                    <tbody>                
                        <tr>
                            <td>{{ cam[0][0] }}</td>
                            <td>{{ cam[0][1] }}</td>
                        </tr>               
                    </tbody>
                </table>
            </div>
        
            <div class="deposito" style="margin-top:3vh; text-align:center;">
                <table>
                    <caption>ENTRADAS EN DEP&Oacute;SITO</caption>
                    <thead>
                        <tr>
                            <th>Fecha</th>
                            <th>Cantidad</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{{ radar[0][0] }}</td>
                            <td>{{ radar[0][1] }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        
            <div class="deposito" style="margin-top:3vh; text-align:center;">
                <table>
                    <caption>ENTRADAS POR TIPO DE VEH&Iacute;CULO EN DEP&Oacute;SITO</caption>
                    <thead>
                        <tr>
                            <th>Fecha</th>
                            <th>Tipo</th>
                            <th>Cantidad</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{{ tvd[0][0] }}</td>
                            <td>{{ tvd[0][2] }}</td>                    
                            <td>{{ tvd[0][1] }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- -->
                <div class="deposito" style="margin-top:3vh; text-align:center; ">
            <table>
                <caption>DATOS REGISTRO DE ENTRADA</caption>
                <thead>                
                    <tr>
                        <th>Fecha</th>
                        <th>Tipo</th>
                        <th>Cantidad</th>
                    </tr>
                </thead>
                <tbody>
                    {% for re in reg_ent %}
                    <tr>
                        <td>{{ re[0] }}</td>
                        <td>{{ re[1] }}</td>                    
                        <td>{{ re[2] }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
            <!-- -->


        </div>

    </div>

    <div class="entrada-firma" style="float:left">
        <!--
        <div class="entrada" style="margin-top:3vh;">
            <table>
                <caption>DATOS REGISTRO DE ENTRADA</caption>
                <thead>                
                    <tr>
                        <th>Fecha</th>
                        <th>Tipo</th>
                        <th>Cantidad</th>
                    </tr>
                </thead>
                <tbody>
                    {% for re in reg_ent %}
                    <tr>
                        <td>{{ re[0] }}</td>
                        <td>{{ re[1] }}</td>                    
                        <td>{{ re[2] }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        -->
        <div class="firma" style="margin-top: 3vh; text-align:left">
            <div class="responsable">
                <p>La Oficial responsable de la UA de Polic&iacute;a Local</p>
            </div>
            <div class="intendente"  style="margin-top: 12vh;">
                <p>El Intendente Jefe de Polic&iacute;a Local</p>
            </div>
        </div>        
    </div>
    
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        .content, table, .deposito{
           
            vertical-align:top;         
        }
        .grid-container1, .grid-container2{
            display: grid;            
            grid-template-columns: auto auto auto auto auto;
        }
        .entrada-firma{
            display: grid;
            grid-template-columns: auto auto auto;
        }
        .entrada{
            grid-column-start: 1;
  	        grid-column-end: 2;
        }
        .firma{
            grid-column-start: 2;
  	        grid-column-end: 3;
        }

        .grid-container2{
            row-gap: 25px;
        }
        .columna-2 {
            grid-column-start: 1;
            grid-column-end: 5;
        }
        .columna-2{
            display: flex;
            
            gap: 5px;
            flex-direction: row;
        }
        .grid-item1{
            grid-column-start: 1;
  	        grid-column-end: 3;
        }
        .grid-item2{
            grid-column-start: 3;
  	        grid-column-end: 4;
        }
       
        .fila{
            display: flex;
            flex-direction: row;
            justify-content:flex-start;
            gap: 30px;
            margin-right: 2vw;
        }
        .bajas{
            grid-column-start: 1;
  	        grid-column-end: 2;
        }
        .columna-2{
            margin-left: 6vw;
            grid-column-start: 4;
  	        grid-column-end: 5;
        }
    </style>

</body>
</html>
"""

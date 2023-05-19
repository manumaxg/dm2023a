#Ensemble de arboles de decision
#utilizando el naif metodo de Arboles Azarosos
#entreno cada arbol utilizando un subconjunto distinto de atributos del dataset

#Para detener el script y mostrar el stack ante un error
options(error = function() { 
  traceback(20); 
  options(error = NULL); 
  stop("\nAbortando luego de un error fatal en el script.\n") 
})


#limpio la memoria
rm( list=ls() )  #Borro todos los objetos
gc()   #Garbage Collection

require("data.table")
require("rpart")

# INICIO parametros experimento

PARAM <- list()

PARAM$experimento  <- 3220
PARAM$semilla  <- 158771      #Establezco la semilla aleatoria, cambiar por SU primer semilla

#parameetros rpart
PARAM$rpart_param   <- list( "cp"=          -0.5,
                              "minsplit"=  500,
                              "minbucket"=  100,

                              "maxdepth"=   14 )

#parametros  arbol
PARAM$feature_fraction  <- 0.5  #entreno cada arbol con solo 50% de las variables variables
PARAM$num_trees_max  <- 500 #voy a generar 500 arboles, a mas arboles mas tiempo de proceso y MEJOR MODELO, pero ganancias marginales

# FIN parametros experimento
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#Aqui comienza el programa

setwd("C:\\Users\\mmgma\\OneDrive\\Escritorio\\Data Mining\\exp\\KA2001\\dm2023a")  #Establezco el Working Directory

#cargo los datos
dataset  <- fread("./datasets/dataset_pequeno.csv")

#using datatable, find the distinct values in fotomes
print(dataset[, unique(foto_mes)])

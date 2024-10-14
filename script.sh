#!/bin/bash

# Vetor com o número de threads
threads=( "1" "2" "4" "8" )
# Vetores com valores de X e Y
X=("1000" "10000" "100000")
Y=("1000" "10000" "100000")

# Cria o arquivo CSV e adiciona o cabeçalho apenas uma vez
echo "numero_threads,intervalo_x,intervalo_y,resultado,tempo" > resultado.csv

# Itera sobre cada conjunto de valores no vetor
for th in "${threads[@]}"; do
    for x in "${X[@]}"; do
        for y in "${Y[@]}"; do
            # Executa o programa em C com os valores da iteração atual
            output=$(./programa "$th" "$x" "$y")

            # Extrai o resultado e o tempo de execução do output
            resultado=$(echo "$output" | grep -oP '(?<=Resultado da integral: )[-+]?[0-9]*\.?[0-9]+')
            tempo=$(echo "$output" | grep -oP '(?<=Tempo de execução: )[-+]?[0-9]*\.?[0-9]+')

            # Verifica se os valores não estão vazios e grava no CSV
            if [ -n "$resultado" ] && [ -n "$tempo" ]; then
                echo "$th,$x,$y,$resultado,$tempo" >> resultado.csv
                echo "Valores salvos em resultado.csv para $th threads, x = $x e y = $y"
                echo "$th threads, x = $x e y = $y, Resultado: $resultado, Tempo: $tempo, DONE" >> log.txt
            else
                echo "Erro na iteração para $th threads, x = $x e y = $y"
                echo "$th threads, x = $x e y = $y, ERROR" >> log.txt
            fi
        done
    done
done

echo "Execução finalizada"
echo "Execução finalizada" >> log.txt

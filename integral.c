#include <math.h>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

// Função para ser integrada
double func(double x, double y)
{
    return sin(x * x + y * y);
}

// Função que calcula a integral dupla usando o método dos trapézios
double integral_dupla(int nx, int ny, int num_threads)
{
    double a = 0.0, b = 1.5; // limites de integração para x e y
    double hx = (b - a) / nx; // passo em x
    double hy = (b - a) / ny; // passo em y
    double soma = 0.0;

#pragma omp parallel for reduction(+ : soma) num_threads(num_threads)
    for (int i = 0; i < nx; i++) {
        for (int j = 0; j < ny; j++) {
            double x = a + i * hx;
            double y = a + j * hy;
            double fx = func(x, y);

            // Peso do trapézio: 1 no centro, 1/2 nas bordas
            if ((i == 0 || i == nx - 1) && (j == 0 || j == ny - 1)) {
                soma += fx * hx * hy * 0.25;
            } else if (i == 0 || i == nx - 1 || j == 0 || j == ny - 1) {
                soma += fx * hx * hy * 0.5;
            } else {
                soma += fx * hx * hy;
            }
        }
    }
    return soma;
}

int main(int argc, char* argv[])
{
    if (argc < 4) {
        printf("Uso: %s <numero_threads> <nx> <ny>\n", argv[0]);
        return 1;
    }

    int num_threads = atoi(argv[1]);
    int nx = atoi(argv[2]);
    int ny = atoi(argv[3]);

    double inicio = omp_get_wtime();
    double resultado = integral_dupla(nx, ny, num_threads);
    double fim = omp_get_wtime();

    printf("Resultado da integral: %f\n", resultado);
    printf("Tempo de execução: %f segundos\n", fim - inicio);

    return 0;
}

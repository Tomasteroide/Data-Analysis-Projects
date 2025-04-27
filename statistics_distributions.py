# Cuaderno de Repaso: Distribuciones de Probabilidad

# Librerias
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Función de apoyo para graficar

def plot_distribution(dist, params={}, size=1000, discrete=False, title=""):
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    if discrete:
        x = np.arange(dist.ppf(0.001, **params), dist.ppf(0.999, **params) + 1)
        pmf = dist.pmf(x, **params)
        ax[0].bar(x, pmf, alpha=0.7)
    else:
        x = np.linspace(dist.ppf(0.001, **params), dist.ppf(0.999, **params), 1000)
        pdf = dist.pdf(x, **params)
        ax[0].plot(x, pdf)

    ax[0].set_title(f"Densidad/PMF de {title}")

    samples = dist.rvs(size=size, **params)
    sns.histplot(samples, kde=True, ax=ax[1], stat="density", bins=30)
    ax[1].set_title(f"Muestras simuladas de {title}")

    plt.show()

# -----------------
# DISTRIBUCIONES CONTINUAS
# -----------------

# Normal
plot_distribution(stats.norm, params={"loc":0, "scale":1}, title="Normal")

# Exponencial
plot_distribution(stats.expon, params={"scale":1}, title="Exponencial")

# Uniforme
plot_distribution(stats.uniform, params={"loc":0, "scale":1}, title="Uniforme")

# Gamma
plot_distribution(stats.gamma, params={"a":2}, title="Gamma")

# Beta
plot_distribution(stats.beta, params={"a":2, "b":5}, title="Beta")

# Log-Normal
plot_distribution(stats.lognorm, params={"s":0.954}, title="Log-Normal")

# Chi-cuadrado
plot_distribution(stats.chi2, params={"df":3}, title="Chi-cuadrado")


# -----------------
# DISTRIBUCIONES DISCRETAS
# -----------------

# Bernoulli
# Resultado de un experimento con dos posibles salidas (éxito o fracaso)
plot_distribution(stats.bernoulli, params={"p":0.3}, discrete=True, title="Bernoulli")

# Binomial
# Número de éxitos en n ensayos independientes
plot_distribution(stats.binom, params={"n":10, "p":0.5}, discrete=True, title="Binomial")

# Poisson
# Número de eventos en un intervalo fijo
plot_distribution(stats.poisson, params={"mu":3}, discrete=True, title="Poisson")

# Geométrica
# Número de intentos hasta el primer éxito
plot_distribution(stats.geom, params={"p":0.3}, discrete=True, title="Geométrica")

# Hipergeométrica
# Número de éxitos en una muestra sin reemplazo
plot_distribution(stats.hypergeom, params={"M":20, "n":7, "N":12}, discrete=True, title="Hipergeométrica")


# -----------------
# EJEMPLOS DE USO DE PDF, CDF, PPF y RVS
# -----------------

# Normal estándar
normal = stats.norm(loc=0, scale=1)

# Densidad en x=0
print("PDF en x=0:", normal.pdf(0))

# Probabilidad acumulada hasta x=1
print("CDF en x=1:", normal.cdf(1))

# Simular 5 valores
print("5 muestras aleatorias:", normal.rvs(size=5))

# Valor que deja 95% de probabilidad a la izquierda
print("PPF en q=0.95:", normal.ppf(0.95))

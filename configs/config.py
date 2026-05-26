# ======================================
# CONFIGURACIÓN GRUPO H - WORLD CUP 2026
# ======================================

from pathlib import Path

# ======================================
# RUTA BASE DEL PROYECTO
# ======================================

BASE_DIR = Path(__file__).resolve().parents[1]

# ======================================
# DIRECTORIOS
# ======================================

RAW_DIR = BASE_DIR / "data/raw"
PROCESSED_DIR = BASE_DIR / "data/processed"
FINAL_DIR = BASE_DIR / "data/final"

HTML_DIR = RAW_DIR / "html"

REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# ======================================
# CONFIGURACIÓN GENERAL
# ======================================

LAST_N_MATCHES = 10

# ======================================
# EQUIPOS DEL GRUPO H
# ======================================

TEAMS = {
    "Spain": [
        HTML_DIR / "spain.html",
        HTML_DIR / "spain_2025.html",
    ],

    "Cape Verde": [
        HTML_DIR / "cape_verde.html",
        HTML_DIR / "cape_verde_2025.html",
    ],

    "Saudi Arabia": [
        HTML_DIR / "saudi_arabia.html",
        HTML_DIR / "saudi_arabia_2025.html",
    ],

    "Uruguay": [
        HTML_DIR / "uruguay.html",
        HTML_DIR / "uruguay_2025.html",
    ],
}

# ======================================
# ARCHIVOS DE SALIDA
# ======================================

CLEAN_DATA_FILE = (
    PROCESSED_DIR / "grupo_h_last_10_clean.csv"
)

SUMMARY_FILE = (
    FINAL_DIR / "group_h_summary.csv"
)

TABLEAU_FILE = (
    FINAL_DIR / "group_h_tableau.csv"
)
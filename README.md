# 🚀 TaskBoard DevOps- Thiago Lovey Castelan


Proyecto demostrativo DevOps Junior con FastAPI, Docker, AWS y GitHub Actions.

## 🧠 Tecnologías usadas
- FastAPI
- Docker
- GitHub Actions (CI/CD)
- AWS EC2 (deploy automático)
- AWS S3 (archivos estáticos)
- GHCR (GitHub Container Registry)

## ⚙️ Flujo del pipeline
Archivo: .github/workflows/ci.yaml
 1.Se ejecuta automáticamente cuando hay un push a main.
 2.Construye la imagen Docker de la aplicación.
 3.Ejecuta los tests (si existen).
 4.Publica la imagen en GitHub Container Registry (GHCR).
Resultado:
→ La imagen queda almacenada en ghcr.io/falconerr88/taskboard-fastapi:latest

2. CD (Despliegue Continuo)
Archivo: .github/workflows/cd.yaml
 1.Espera a que el CI se ejecute correctamente.
 2.Se conecta por SSH a tu instancia EC2.
 3.Descarga la última imagen desde GHCR.
 4.Detiene el contenedor anterior (si existe) y lanza el nuevo.
 5.Sincroniza los archivos estáticos con S3.
Resultado:
→ La aplicación se actualiza automáticamente en tu servidor EC2.
→ Se suben los archivos estaticos a S3.



## 📸 Arquitectura


GitHub Actions → EC2 (Docker)
               ↳ S3 (archivos estático)  

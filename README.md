# 🚀 TaskBoard DevOps

Proyecto demostrativo DevOps Junior con FastAPI, Docker, AWS y GitHub Actions.

## 🧠 Tecnologías usadas
- FastAPI
- Docker
- GitHub Actions (CI/CD)
- AWS EC2 (deploy automático)
- AWS S3 (archivos estáticos)
- GHCR (GitHub Container Registry)

## ⚙️ Flujo del pipeline
1. GitHub Actions construye la imagen Docker
2. Sube la imagen a GHCR
3. Sube los archivos estáticos a S3
4. Se conecta por SSH a EC2
5. Detiene el contenedor anterior
6. Despliega la nueva versión automáticamente

## 🌐 Endpoints principales
- `/` → Health check
- `/upload` → Sube archivo a S3
- `/tasks` → Lista de tareas

## 📸 Arquitectura


GitHub Actions → EC2 (Docker)
               ↳ S3 (archivos estáticos)

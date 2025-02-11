from .main import app
from .routes.admin import router as admin_router
from .routes.student import router as student_router

app.include_router(admin_router)
app.include_router(student_router)
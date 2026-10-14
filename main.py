from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Job Search Tracker API",
    description="An API for tracking job applications and their statuses.",
    version="0.1.0"
)
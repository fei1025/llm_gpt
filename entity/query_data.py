from pydantic import BaseModel


class query_pdf(BaseModel):
    token: str
    messages: []

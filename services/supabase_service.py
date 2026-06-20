import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()


class SupabaseService:
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")

        if not url or not key:
            raise ValueError("Supabase não configurado corretamente")

        self.client = create_client(url, key)

    def buscar_contatos(self, limite=3):
        response = (
            self.client
            .table("contacts")
            .select("*")
            .limit(limite)
            .execute()
        )

        return response.data
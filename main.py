import logging
from services.supabase_service import SupabaseService
from services.whatsapp_service import WhatsAppService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    supabase = SupabaseService()
    whatsapp = WhatsAppService()

    try:
        logging.info("Buscando contatos...")
        contatos = supabase.buscar_contatos(limite=3)

        if not contatos:
            logging.warning("Nenhum contato encontrado")
            return

        for contato in contatos:
            try:
                nome = contato.get("nome")
                telefone = contato.get("telefone")

                if not nome or not telefone:
                    logging.warning(f"Contato inválido: {contato}")
                    continue

                mensagem = f"Olá, {nome} tudo bem com você?"

                whatsapp.enviar_mensagem(telefone, mensagem)

                logging.info(f"Mensagem enviada para {nome}")

            except Exception as e:
                logging.error(f"Erro ao enviar para {contato}: {e}")

        logging.info("Processo finalizado com sucesso")

    except Exception as e:
        logging.error(f"Erro geral: {e}")


if __name__ == "__main__":
    main()
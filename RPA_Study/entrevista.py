import cv2
import pytesseract
import re
import psycopg2
import logging

# --- CONFIGURAÇÕES ---
documento = "emails.png"

db_nome = "entrevista"
db_user = "postgres"
db_senha = "postgres"
db_host = "localhost"
db_port = "5432"

# logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()] #envia o código para terminal FileHandler() para arquivo, etc
)

# OCR (OpenCV + Pytesseract)
def extrair_emails(image_path):
    img = cv2.imread(image_path)

    if img is None:
        logging.error(f"Arquivo não encontrado: {image_path}")
        return []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # OCR com configuração extra
    texto = pytesseract.image_to_string(thresh, config="--psm 6")

    # Regex para capturar emails
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)

    # Normalizar: strip + lower, remover duplicatas
    emails = [e.strip().lower() for e in emails]
    emails = list(dict.fromkeys(emails))

    return emails

# PostgreSQL
def salvar_emails_postgres(emails):
    try:
        with psycopg2.connect(
            dbname=db_nome,
            user=db_user,
            password=db_senha,
            host=db_host,
            port=db_port
        ) as conn:
            with conn.cursor() as cur:
                # Criar tabela
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS emails (
                        id SERIAL PRIMARY KEY,
                        email TEXT UNIQUE
                    );
                """)

                # Inserir emails
                for email in emails:
                    try:
                        cur.execute(
                            "INSERT INTO emails (email) VALUES (%s) ON CONFLICT DO NOTHING;",
                            (email,)
                        )
                        logging.info(f"Email inserido: {email}")
                    except Exception as e:
                        logging.error(f"Erro ao inserir {email}: {e}")

                conn.commit()

                # Mostrar todos os emails armazenados
                cur.execute("SELECT * FROM emails;")
                registros = cur.fetchall()
                logging.info("Emails na tabela:")
                for r in registros:
                    logging.info(f"ID={r[0]} | Email={r[1]}")

        logging.info("Finalizado. Emails salvos no PostgreSQL.")

    except Exception as e:
        logging.error(f"Erro de conexão com o banco: {e}")


if __name__ == "__main__":
    emails = extrair_emails(documento)

    if emails:
        logging.info(f"Emails detectados no OCR: {emails}")
        salvar_emails_postgres(emails)
    else:
        logging.warning("Nenhum email detectado.")
